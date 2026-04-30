#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小红书发布器 — 独立 Playwright 模式（持久化 profile）

登录一次扫码，登录态保存在 xhs_profiles/default/ 中，
后续发布自动复用，不再弹出浏览器窗口。

用法:
  python3 publisher.py login        # 首次扫码登录（弹一次窗口）
  python3 publisher.py note ...    # 后续发布无窗口
  python3 publisher.py video ...
  python3 publisher.py draft ...

前置条件:
  - Playwright: pip install playwright && playwright install chromium
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
import time
import uuid
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
XHS_PROFILES_DIR = SKILL_DIR / "xhs_profiles"
XHS_DRAFTS_FILE = SKILL_DIR / "xhs_drafts.json"
UPLOAD_DIR = Path("/tmp/openclaw/uploads")

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}
VIDEO_EXTENSIONS = {".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv", ".m4v"}
PUBLISH_URL = "https://creator.xiaohongshu.com/publish/publish?from=menu"


class XHSError(Exception):
    pass


def _profile_path(profile_name: str = "default") -> Path:
    return XHS_PROFILES_DIR / profile_name


def _ensure_playwright():
    try:
        from playwright.async_api import async_playwright
        return async_playwright
    except ImportError:
        raise XHSError("Playwright 未安装。运行: pip install playwright && playwright install chromium")


async def _check_logged_in(page) -> bool:
    if "login" in page.url.lower():
        return False
    for sel in [
        "input[type='file']",
        "button:has-text('发布')", ".publishBtn",
        "button:has-text('上传视频')", "button:has-text('上传图文')",
        "text=上传图文", "text=上传视频", "text=发布笔记",
    ]:
        if await page.locator(sel).count() > 0:
            return True
    return False


async def _switch_to_image_tab(page):
    """切换到上传图文 tab — 页面初始默认在视频 tab。"""
    # 精确点击可见的上传图文 tab（小红书多层 tab 结构，只有 zIndex=auto position=relative 的可点击）
    switched = await page.evaluate("""() => {
        const divs = document.querySelectorAll('div.creator-tab');
        for (const d of divs) {
            const span = d.querySelector('span.title');
            if (span && span.textContent.includes('上传图文')) {
                const style = getComputedStyle(d);
                if (style.position === 'relative') {
                    d.click();
                    return true;
                }
            }
        }
        return false;
    }""")
    await page.wait_for_timeout(2000)
    return switched


async def _upload_image(page, image_path: str):
    """通过 JS 触发上传，因为小红书 file input 是隐藏的。"""
    src = Path(image_path)
    if not src.exists():
        raise XHSError(f"图片不存在: {image_path}")

    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    dest = UPLOAD_DIR / f"xhs_{uuid.uuid4().hex[:8]}{src.suffix}"
    shutil.copy(str(src), str(dest))

    # 确保文件存在
    fi = page.locator("input[type='file']")
    if await fi.count() == 0:
        raise XHSError("未找到文件上传控件。")

    # 小红书 file input 是隐藏的，但 set_input_files 可以处理隐藏 input
    await fi.first.set_input_files(str(dest))
    await page.wait_for_timeout(3000)
    return True


async def _fill_title(page, title: str):
    """填写标题。"""
    # 页面切换到图文 tab 后标题输入框会出现
    for sel in ["[placeholder*='标题']", "textarea[placeholder*='标题']",
                 "input[placeholder*='标题']", ".d-text"]:
        loc = page.locator(sel).first
        if await loc.count() > 0:
            try:
                await loc.fill("")
                await page.wait_for_timeout(200)
                await loc.fill(title)
            except Exception:
                await loc.click()
                await loc.evaluate("el => { el.value = ''; el.dispatchEvent(new Event('input', {bubbles: true})) }")
                await page.keyboard.type(title, delay=20)
            return True
    return False


async def _fill_body(page, body: str):
    """填写正文。"""
    for sel in [".ql-editor", "[contenteditable='true']",
                "textarea[placeholder*='正文']", "textarea"]:
        loc = page.locator(sel).first
        if await loc.count() > 0:
            await loc.click()
            await page.wait_for_timeout(500)
            # 先清空
            await loc.evaluate('el => { el.focus(); el.innerHTML = ""; }')
            await page.wait_for_timeout(300)
            # 用 keyboard.type 逐字输入，避免转义问题
            await page.keyboard.type(body, delay=10)
            await page.wait_for_timeout(1000)
            return True
    return False


async def _click_publish(page):
    """点击底部的"发布"按钮（不是顶部的 tab 标题）。
    页面底部发布栏有两个按钮："暂存离开" 和 "发布"。
    真正的发布按钮在底部，用 <button> 内的 "发布" 文本定位。
    """
    # 底部发布栏有两个按钮：暂存离开 + 发布。点击真正的发布按钮
    for sel in [
        "button:has-text('发布'):not(:has-text('暂存')):not(:has-text('笔记'))",
        "//button[text()='发布']",
        "button.d-text:has-text('发布')",
        "button:has-text('发布')",
    ]:
        loc = page.locator(sel).first
        if await loc.count() > 0 and await loc.is_visible():
            try:
                await loc.click(timeout=5000)
            except Exception:
                await loc.evaluate("el => el.closest('button')?.click() || el.click()")
            await page.wait_for_timeout(8000)
            return True
    raise XHSError("未找到发布按钮。")


# ====================================================================
# 登录
# ====================================================================

async def cmd_login(timeout_seconds: int = 300) -> dict:
    pw = _ensure_playwright()
    profile_dir = _profile_path("default")

    async with pw() as playwright:
        context = await playwright.chromium.launch_persistent_context(
            str(profile_dir),
            headless=False,
            viewport={"width": 1440, "height": 960},
            args=["--disable-blink-features=AutomationControlled", "--no-sandbox"],
        )
        page = context.pages[0] if context.pages else await context.new_page()
        await page.goto(PUBLISH_URL, wait_until="domcontentloaded")
        await page.wait_for_timeout(3000)

        if await _check_logged_in(page):
            print("✅ 已登录小红书创作者中心。")
            await context.close()
            return {"verified": True, "status": "ready", "message": "已登录。"}

        print(f"🔓 浏览器已打开，请扫码登录小红书（{timeout_seconds}s 超时）...")
        deadline = time.monotonic() + timeout_seconds
        verified = False
        while time.monotonic() < deadline:
            if page.is_closed():
                break
            if await _check_logged_in(page):
                verified = True
                break
            await page.wait_for_timeout(2000)

        print("✅ 登录态已保存至 persistent profile" if verified else "⏰ 登录超时")
        await context.close()

    result = {
        "verified": verified,
        "profile_dir": str(profile_dir),
        "status": "ready" if verified else "pending",
        "message": "✅ 登录成功，后续发布自动复用登录态。" if verified else "⏰ 登录超时。",
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return result


# ====================================================================
# 发布
# ====================================================================

async def _cmd_note_async(images, title, body, tags, dry_run):
    for p in images:
        if not Path(p).exists():
            raise XHSError(f"图片不存在: {p}")
    if not title.strip() or not body.strip():
        raise XHSError("标题和正文不能为空。")

    if dry_run:
        result = {"status": "dry_run_ok", "type": "note", "title": title,
                  "image_count": len(images), "tags": tags or []}
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return result

    pw = _ensure_playwright()
    profile_dir = _profile_path("default")

    full_body = body.strip()
    if tags:
        tag_line = " ".join(f"#{t.lstrip('#')}" for t in tags if t.strip())
        full_body += "\n\n" + tag_line

    async with pw() as playwright:
        context = await playwright.chromium.launch_persistent_context(
            str(profile_dir),
            headless=True,
            viewport={"width": 1440, "height": 960},
            args=["--disable-blink-features=AutomationControlled", "--no-sandbox"],
        )
        try:
            page = context.pages[0] if context.pages else await context.new_page()
            await page.goto(PUBLISH_URL, wait_until="domcontentloaded")
            await page.wait_for_timeout(3000)

            if not await _check_logged_in(page):
                raise XHSError("未检测到登录态，请先运行 `publisher.py login` 扫码登录。")

            # Step 1: 切换到上传图文 tab（JS 方式，避免 viewport 问题）
            await _switch_to_image_tab(page)

            # Step 2: 上传图片（逐个上传多张）
            for i, img_path in enumerate(images):
                print(f"  上传图片 [{i+1}/{len(images)}]", flush=True)
                await _upload_image(page, img_path)

            # Step 3: 填写标题
            filled = await _fill_title(page, title)
            if not filled:
                print("⚠️ 标题输入框未找到")

            # Step 4: 填写正文 + 标签
            filled = await _fill_body(page, full_body)
            if not filled:
                print("⚠️ 正文编辑区未找到")

            # Step 5: 点击发布
            await _click_publish(page)

        finally:
            await context.close()

    result = {"status": "published", "type": "note", "title": title,
              "image_count": len(images),
              "message": "✅ 发布请求已提交，请确认最终状态。"}
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return result


# ====================================================================
# CLI
# ====================================================================

def main():
    parser = argparse.ArgumentParser(description="小红书发布器")
    sub = parser.add_subparsers(dest="command")

    p_login = sub.add_parser("login", help="登录（首次扫码）")
    p_login.add_argument("--timeout", type=int, default=300)

    p_note = sub.add_parser("note", help="发布图文笔记")
    p_note.add_argument("--images", nargs="+", required=True)
    p_note.add_argument("--title", required=True)
    p_note.add_argument("--body", required=True)
    p_note.add_argument("--tags", nargs="*", default=[])
    p_note.add_argument("--dry-run", action="store_true")

    p_video = sub.add_parser("video", help="发布视频")
    p_video.add_argument("--video", required=True)
    p_video.add_argument("--title", required=True)
    p_video.add_argument("--body", required=True)
    p_video.add_argument("--tags", nargs="*", default=[])
    p_video.add_argument("--dry-run", action="store_true")

    p_draft = sub.add_parser("draft", help="草稿管理")
    p_draft_sub = p_draft.add_subparsers(dest="draft_cmd")
    p_dc = p_draft_sub.add_parser("create")
    p_dc.add_argument("--images", nargs="+", required=True)
    p_dc.add_argument("--title", required=True)
    p_dc.add_argument("--body", required=True)
    p_dc.add_argument("--tags", nargs="*", default=[])
    p_draft_sub.add_parser("list")
    p_dp = p_draft_sub.add_parser("publish")
    p_dp.add_argument("--draft-id", required=True)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)

    try:
        import asyncio
        if args.command == "login":
            asyncio.run(cmd_login(timeout_seconds=args.timeout))
        elif args.command == "note":
            asyncio.run(_cmd_note_async(args.images, args.title, args.body,
                                        args.tags, dry_run=args.dry_run))
        elif args.command == "video":
            print("⚠️ video 命令待实现")
        elif args.command == "draft":
            print("⚠️ draft 命令待实现")
        else:
            parser.print_help()
    except XHSError as e:
        print(f"❌ {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
