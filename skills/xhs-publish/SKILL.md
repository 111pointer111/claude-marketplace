---
name: xhs-publish
description: 小红书内容发布 — 通过 Playwright 持久化 profile 实现图文/视频发布，支持本地图片和标签，自动复用登录态。
user-invocable: true
---

# 小红书发布 Skill

通过 Playwright + 持久化 profile 实现小红书内容发布。**首次扫码登录一次，后续自动复用登录态**，全程 headless 不弹窗。

## 前置条件
```bash
pip install playwright
playwright install chromium
```

## 目录结构
```
skills/xhs-publish/
├── SKILL.md               # 本文档
├── tools/
│   └── publisher.py       # 发布工具入口
├── xhs_profiles/default/   # 持久化登录态（自动生成，不要手动改）
└── xhs_drafts.json        # 本地草稿缓存
```

## 命令

### 首次登录（后续不需要）
```bash
python3 tools/publisher.py login --timeout 300
```
- 弹出 Chrome 窗口到小红书创作者中心
- 手动在窗口中扫码登录
- **登录态永久保存在 `xhs_profiles/default/` 中**
- 后续所有发布都在 headless 模式下自动进行

### 图文发布
```bash
python3 tools/publisher.py note \
  --images /path/img1.jpg [/path/img2 ...] \
  --title "标题" \
  --body "正文内容" \
  [--tags tag1 tag2] \
  [--dry-run]
```

### 视频发布（待实现）
```bash
python3 tools/publisher.py video ...   # 接口已预留，逻辑待适配
```

## 实现架构
```
用户输入 → publisher.py CLI
  → Playwright launch_persistent_context(xhs_profiles/default/)
  → 非 headless: 登录窗口
  → headless: 自动操作 DOM
    → 1. 切换到"上传图文" tab（JS 精确点击 position:relative 的 tab）
    → 2. 上传图片（set_input_files）
    → 3. 填写标题
    → 4. 填写正文 + 标签
    → 5. 点击底部"发布"按钮（不是顶部 tab 标题）
  → 输出发布结果
```

## 已知问题与边界
| 问题 | 解决方案 |
|------|---------|
| 小红书检测 headless | 加 `--disable-blink-features=AutomationControlled` 绕过 |
| 多层 tab 结构，默认在视频 tab | JS 精确选择 `div.creator-tab` + `position:relative` 的版本 |
| 页面顶部和底部都有"发布"文字 | 只能点底部 `<button>发布</button>`，不是顶部 tab 标题 |
| 图片上传后需等待处理 | `wait_for_timeout(3000)` + 检查缩略图可见 |
| profile 被 lock | 删除 `SingletonLock`/`SingletonSocket` 文件 |

## 发布测试记录
| 时间 | 标题 | 结果 | 原因 |
|------|------|------|------|
| 04-25 00:30 | 测试发布/测试发布 v2 | ❌ 未发布 | 默认在视频 tab 下发图文，或 tab 切换不对 |
| 04-25 00:48 | 测试发布 v3/v4 | ❌ 存草稿 | 点了顶部 tab 标题"发布笔记"而非底部"发布"按钮 |
| 04-25 00:55 | 测试发布 v6 | ✅ 成功 | 正确切 tab + 正确点击底部"发布"按钮 |

## 注意事项
- 首次使用一定要先 `login` 一次扫码
- 如果 Chrome profile 被 lock，删除 `xhs_profiles/default/Singleton*` 文件
- 发布默认 headless=True，调试可以临时改成 False
