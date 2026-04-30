"""
知乎发布器 — 通过 OpenClaw 浏览器自动化发布

支持两种模式:
1. OpenClaw browser 工具 (browser tool) — 原生方式，适用于 Gateway 启用了 browser 插件的场景
2. Playwright CDP fallback — 适用于 browser 工具不可用的环境（如当前 session capabilities=none）
   通过连接 OpenClaw 的 Chrome CDP 端口 (默认 18801) 实现自动化

⚠️ 实测重要经验:
- md 文件导入在 Playwright CDP 模式下不工作（知乎对 setInputFiles 有检查）
  → 内容必须通过 keyboard.type() 注入编辑器
- 话题/来源按钮的 innerText 包含换行符 (\n)，不能用精确匹配
- 话题下拉选项必须直接点击元素，不能用 ArrowDown+Enter
- 来源选择需要两步：展开"选择具体的信息来源" → 选"官方网站" → 确认添加
- 发布按钮为 disabled 时，必须确保：话题已选 OR 来源已选（两者至少其一即可）
"""

import os
import time
import shutil
import subprocess
from pathlib import Path


# ============================================================
# 文件准备
# ============================================================

def prepare_files(article_path: str, cover_path: str | None, settings: dict) -> tuple:
    """将文章和封面复制到上传目录"""
    upload_dir = Path(settings.get("UPLOAD_DIR", "/tmp/openclaw/uploads"))
    upload_dir.mkdir(parents=True, exist_ok=True)

    timestamp = int(time.time())
    dest_article = upload_dir / f"article_{timestamp}.md"
    shutil.copy(article_path, dest_article)

    dest_cover = None
    if cover_path and Path(cover_path).exists():
        dest_cover = upload_dir / f"cover_{timestamp}.png"
        shutil.copy(cover_path, dest_cover)

    return str(dest_article), str(dest_cover) if dest_cover else None


# ============================================================
# Browser Tool 模式（原生 OpenClaw browser 工具）
# ============================================================

def find_element_by_text(snapshot: dict, text: str, partial: bool = True) -> str | None:
    """通过文本内容查找元素 ref"""
    text_lower = text.lower()
    def search(obj):
        if isinstance(obj, dict):
            if obj.get("text", "").lower() and text_lower in obj.get("text", "").lower():
                return obj.get("ref")
            for v in obj.values():
                if isinstance(v, (dict, list)):
                    r = search(v)
                    if r:
                        return r
        elif isinstance(obj, list):
            for item in obj:
                r = search(item)
                if r:
                    return r
        return None
    return search(snapshot)


def find_element_by_placeholder(snapshot: dict, placeholder: str) -> str | None:
    """通过 placeholder 查找元素 ref"""
    ph_lower = placeholder.lower()
    def search(obj):
        if isinstance(obj, dict):
            if ph_lower in obj.get("placeholder", "").lower():
                return obj.get("ref")
            for v in obj.values():
                if isinstance(v, (dict, list)):
                    r = search(v)
                    if r:
                        return r
        elif isinstance(obj, list):
            for item in obj:
                r = search(item)
                if r:
                    return r
        return None
    return search(snapshot)


def find_button(snapshot: dict, text: str) -> str | None:
    """通过按钮文本查找 ref"""
    text_lower = text.lower()
    def search(obj):
        if isinstance(obj, dict):
            role = obj.get("role", "")
            kind = obj.get("kind", "").lower()
            if ("button" in role or "button" in kind):
                if text_lower in obj.get("text", "").lower():
                    return obj.get("ref")
            for v in obj.values():
                if isinstance(v, (dict, list)):
                    r = search(v)
                    if r:
                        return r
        elif isinstance(obj, list):
            for item in obj:
                r = search(item)
                if r:
                    return r
        return None
    return search(snapshot)


def get_snapshot(browser, target_id: str) -> dict | None:
    """获取页面 snapshot"""
    try:
        resp = browser(action="snapshot", targetId=target_id)
        if resp.get("ok") and "data" in resp:
            return resp["data"]
    except Exception:
        pass
    return None


def auto_publish_browser_tool(article_path: str, cover_path: str | None, title: str, settings: dict) -> str | None:
    """使用 OpenClaw browser 工具发布（原生方式）"""
    from tools import browser

    dest_article, dest_cover = prepare_files(article_path, cover_path, settings)
    default_topic = settings.get("DEFAULT_TOPIC", "人工智能")
    default_source = settings.get("DEFAULT_SOURCE", "官方网站")

    print("=" * 50)
    print("📤 开始发布到知乎（browser 工具模式）...")
    print(f"   文章: {dest_article}")
    print("=" * 50)

    # Step 1: 打开写文章页面
    print("\n[Step 1/7] 打开知乎写文章页面...")
    browser(action="open", url=settings.get("ZHIHOU_WRITE_URL", "https://zhuanlan.zhihu.com/write"))
    time.sleep(3)

    target_id = None
    tabs_resp = browser(action="tabs")
    for tab in tabs_resp.get("tabs", []):
        if "zhihu.com/write" in tab.get("url", ""):
            target_id = tab.get("targetId")
            break
    if not target_id:
        target_id = "zhihu-publish"

    # Step 2: 导入 md 文件
    print("\n[Step 2/7] 导入 md 文件...")
    snapshot = get_snapshot(browser, target_id)
    if snapshot:
        ref = find_button(snapshot, "导入文档")
        if ref:
            browser(action="act", request={"kind": "click", "ref": ref}, targetId=target_id)
            time.sleep(2)
    try:
        browser(action="upload", paths=[dest_article], targetId=target_id)
        print("   ✅ md 文件上传成功")
    except Exception as e:
        print(f"   ⚠️ md 文件上传失败（内容将手动填入）: {e}")
    time.sleep(5)

    # Step 3: 上传封面图
    if dest_cover:
        print("\n[Step 3/7] 上传封面图...")
        browser(action="act", request={"kind": "evaluate", "fn": "window.scrollTo(0, 0)"}, targetId=target_id)
        time.sleep(1)
        snapshot = get_snapshot(browser, target_id)
        ref = find_button(snapshot, "添加封面")
        if ref:
            browser(action="act", request={"kind": "click", "ref": ref}, targetId=target_id)
            time.sleep(2)
            try:
                browser(action="upload", paths=[dest_cover], targetId=target_id)
                print("   ✅ 封面上传成功")
            except Exception as e:
                print(f"   ⚠️ 封面上传失败: {e}")
    else:
        print("\n[Step 3/7] 跳过封面上传")

    # Step 4: 输入标题
    print("\n[Step 4/7] 输入标题...")
    snapshot = get_snapshot(browser, target_id)
    if snapshot:
        ref = find_element_by_placeholder(snapshot, "请输入标题")
        if ref:
            browser(action="act", request={"kind": "click", "ref": ref}, targetId=target_id)
            time.sleep(0.5)
            browser(action="act", request={"kind": "type", "ref": ref, "text": title}, targetId=target_id)
            print(f"   ✅ 标题输入成功: {title}")
    time.sleep(2)

    # Step 5: 添加话题
    print("\n[Step 5/7] 添加话题...")
    browser(action="act", request={"kind": "evaluate", "fn": "window.scrollTo(0, document.body.scrollHeight)"}, targetId=target_id)
    time.sleep(1)
    snapshot = get_snapshot(browser, target_id)
    ref = find_button(snapshot, "添加话题")
    if ref:
        browser(action="act", request={"kind": "click", "ref": ref}, targetId=target_id)
        time.sleep(1)
        ref2 = find_element_by_placeholder(snapshot, "搜索话题")
        if ref2:
            browser(action="act", request={"kind": "type", "ref": ref2, "text": default_topic}, targetId=target_id)
            time.sleep(1)
            snapshot2 = get_snapshot(browser, target_id)
            ref3 = find_button(snapshot2, default_topic)
            if ref3:
                browser(action="act", request={"kind": "click", "ref": ref3}, targetId=target_id)
                print(f"   ✅ 话题添加成功: {default_topic}")
    time.sleep(1)

    # Step 6: 添加内容来源
    print("\n[Step 6/7] 添加内容来源...")
    snapshot = get_snapshot(browser, target_id)
    ref = find_button(snapshot, "添加来源")
    if ref:
        browser(action="act", request={"kind": "click", "ref": ref}, targetId=target_id)
        time.sleep(1)
        snapshot2 = get_snapshot(browser, target_id)
        ref2 = find_button(snapshot2, default_source)
        if ref2:
            browser(action="act", request={"kind": "click", "ref": ref2}, targetId=target_id)
            time.sleep(0.5)
            snapshot3 = get_snapshot(browser, target_id)
            ref3 = find_button(snapshot3, "确认添加")
            if ref3:
                browser(action="act", request={"kind": "click", "ref": ref3}, targetId=target_id)
                print(f"   ✅ 内容来源添加成功: {default_source}")
    time.sleep(1)

    # Step 7: 检查发布按钮
    print("\n[Step 7/7] 检查发布状态...")
    snapshot = get_snapshot(browser, target_id)
    ref = find_button(snapshot, "发布")
    if ref:
        print("   ✅ 发布按钮已就绪")
    else:
        print("   ⚠️ 发布按钮未找到")

    tabs_resp = browser(action="tabs")
    for tab in tabs_resp.get("tabs", []):
        if tab.get("targetId") == target_id:
            return tab.get("url", "https://zhihu.com/draft")
    return "https://zhihu.com/draft"


# ============================================================
# Playwright CDP Fallback 模式
# （当 browser 工具不可用时，通过 CDP 连接 OpenClaw 的 Chrome）
# ============================================================

CDP_PORT = 18801  # OpenClaw browser 的 CDP 调试端口


def auto_publish_playwright(article_path: str, cover_path: str | None, title: str, settings: dict) -> str | None:
    """
    使用 Playwright CDP 连接 OpenClaw 浏览器发布。

    ⚠️ 前置条件：
    - OpenClaw browser 必须已启动且 remote-debugging-port=18801
    - 需要安装 Playwright: npm install -g playwright

    ⚠️ 实测关键点：
    - md 导入不工作 → 内容必须 keyboard.type() 注入
    - 按钮 innerText 有换行符 → 用部分匹配 jsClick(text) 而非精确匹配
    - 话题下拉选项必须直接点击元素，不能用键盘
    - 来源选择需要两步展开
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("❌ Playwright 未安装，请运行: npm install -g playwright")
        return None

    dest_article, dest_cover = prepare_files(article_path, cover_path, settings)
    default_topic = settings.get("DEFAULT_TOPIC", "人工智能")
    default_source = settings.get("DEFAULT_SOURCE", "官方网站")

    # 读取文章内容
    with open(dest_article, "r", encoding="utf-8") as f:
        md_content = f.read()

    print("=" * 50)
    print("📤 开始发布到知乎（Playwright CDP 模式）...")
    print(f"   文章: {dest_article}")
    print(f"   封面: {dest_cover}")
    print(f"   标题: {title}")
    print("=" * 50)

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(f"http://127.0.0.1:{CDP_PORT}")
        context = browser.contexts()[0] if browser.contexts() else browser.new_context()
        pages = context.pages
        page = pages[0] if pages else context.new_page()

        try:
            # Step 1: 打开写文章页面
            print("\n[Step 1/7] 打开知乎写文章页面...")
            page.goto("https://zhuanlan.zhihu.com/write", wait_until="domcontentloaded", timeout=30000)
            page.wait_for_timeout(3000)

            # Step 2: 填入内容（md 导入不可用，用 keyboard.type）
            print("\n[Step 2/7] 填入文章内容...")
            page.keyboard.press("Escape")
            page.wait_for_timeout(300)
            editor = page.query_selector(".public-DraftEditor-content")
            if editor:
                editor.click()
                page.keyboard.type(md_content, delay=2)
                print(f"   ✅ 内容已填入 ({len(md_content)} 字符)")
            else:
                print("   ⚠️ 未找到编辑器元素")

            # Step 3: 输入标题（React-compatible）
            print("\n[Step 3/7] 输入标题...")
            page.evaluate(f"""
                () => {{
                    const ta = document.querySelector('textarea');
                    if (ta) {{
                        const setter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, 'value').set;
                        setter.call(ta, {repr(title)});
                        ta.dispatchEvent(new Event('input', {{ bubbles: true }}));
                    }}
                }}
            """)
            page.wait_for_timeout(500)
            print(f"   ✅ 标题已填入: {title}")

            # 滚动到页面底部，让话题/来源按钮可见
            page.evaluate("() => window.scrollTo(0, 3000)")
            page.wait_for_timeout(500)

            # Step 4: 添加话题
            print("\n[Step 4/7] 添加话题...")
            _js_click_partial(page, "添加话题")
            page.wait_for_timeout(2000)

            # 在搜索框输入话题
            page.evaluate(f"""
                () => {{
                    const inputs = document.querySelectorAll('input');
                    for (const inp of inputs) {{
                        if (inp.placeholder && inp.placeholder.includes('搜索') && inp.offsetWidth > 0) {{
                            inp.value = {repr(default_topic)};
                            inp.dispatchEvent(new Event('input', {{ bubbles: true }}));
                            return;
                        }}
                    }}
                }}
            """)
            page.wait_for_timeout(2000)

            # 直接点击话题选项（不能用键盘选择）
            topic_found = page.evaluate(f"""
                () => {{
                    const all = document.querySelectorAll('[role="option"], [role="listitem"], li, div');
                    for (const el of all) {{
                        if ((el.innerText || '').trim() === {repr(default_topic)} && el.offsetWidth > 0) {{
                            el.click();
                            return true;
                        }}
                    }}
                    return false;
                }}
            """)
            if topic_found:
                print(f"   ✅ 话题已选择: {default_topic}")
            else:
                print(f"   ⚠️ 话题选项未找到（继续尝试）")
            page.wait_for_timeout(1500)

            # Step 5: 添加内容来源
            print("\n[Step 5/7] 添加内容来源...")
            _js_click_partial(page, "添加来源")
            page.wait_for_timeout(2000)

            # 展开"选择具体的信息来源"
            _js_click_partial(page, "选择具体的信息来源")
            page.wait_for_timeout(1500)

            # 选择"官方网站"
            source_clicked = page.evaluate(f"""
                () => {{
                    const all = document.querySelectorAll('button');
                    for (const b of all) {{
                        if ((b.innerText || '').trim() === {repr(default_source)}) {{
                            b.click();
                            return true;
                        }}
                    }}
                    return false;
                }}
            """)
            if source_clicked:
                print(f"   ✅ 内容来源已选择: {default_source}")
            page.wait_for_timeout(500)

            # 确认添加
            _js_click_partial(page, "确认添加")
            page.wait_for_timeout(1500)

            # Step 6: 检查发布按钮
            print("\n[Step 6/7] 检查发布状态...")
            pub_state = page.evaluate("""
                () => {
                    const btns = Array.from(document.querySelectorAll('button'));
                    const pub = btns.find(b => b.innerText.trim() === '发布');
                    return pub ? { disabled: pub.disabled } : null;
                }
            """)
            print(f"   发布按钮状态: {pub_state}")

            if pub_state and not pub_state.get("disabled"):
                print("\n[Step 7/7] 点击发布...")
                _js_click_partial(page, "发布")
                page.wait_for_timeout(5000)
                final_url = page.url
                print(f"\n🎉 发布成功: {final_url}")
            else:
                print("\n⚠️ 发布按钮仍为 disabled，内容已填入，请手动检查并发布")
                final_url = page.url

            page.wait_for_timeout(1000)
            return final_url

        finally:
            page.wait_for_timeout(60000)  # 留出人工检查时间
            browser.close()


def _js_click_partial(page, text: str):
    """用部分匹配方式点击按钮（处理 innerText 含换行符的情况）"""
    page.evaluate(f"""
        () => {{
            const all = document.querySelectorAll('button, [role="button"]');
            for (const el of all) {{
                if ((el.innerText || '').replace(/\\s+/g, ' ').trim().includes({repr(text)})) {{
                    el.click();
                    return true;
                }}
            }}
        }}
    """)


# ============================================================
# 主入口
# ============================================================

def auto_publish(article_path: str, cover_path: str | None, title: str, settings: dict) -> str | None:
    """
    自动发布到知乎。

    优先使用 OpenClaw browser 工具，
    不可用时自动降级为 Playwright CDP 模式。
    """
    try:
        # 尝试 browser 工具模式
        from tools import browser
        return auto_publish_browser_tool(article_path, cover_path, title, settings)
    except Exception as e:
        print(f"⚠️ browser 工具不可用 ({e})，尝试 Playwright CDP 模式...")
        return auto_publish_playwright(article_path, cover_path, title, settings)
