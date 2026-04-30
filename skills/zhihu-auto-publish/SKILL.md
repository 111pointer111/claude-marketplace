---
name: zhihu-auto-publish
description: 知乎AI热点自动发布 — 从热点抓取、AI文章生成、封面图生成到知乎专栏发布，以及手动文章发布到知乎的完整流程。
user-invocable: true
---

# 知乎自动发布 Skill

支持两种核心场景：
1. **自动热点发布**：抓取 HN AI 热点 → AI 生成文章 → 生成封面 → 发布知乎
2. **手动文章发布**：将已有文章或 AI 生成的文章发布到知乎专栏

## 配置

读取 `{skillDir}/settings.yaml` 获取配置：
- `MINIMAX_API_KEY`：MiniMax API Key（用于文章生成和封面图，**必须从环境变量 `MINIMAX_API_KEY` 读取，禁止硬编码**）
- `MINIMAX_REGION`：区域，可选 `cn` / `global`（从环境变量 `MINIMAX_REGION` 读取）
- `MINIMAX_TEXT_MODEL`：文本模型（默认 `MiniMax-M2.7`）
- `MINIMAX_MAX_TOKENS`：最大 token 数（默认 8192）
- `MINIMAX_TEMPERATURE`：温度（默认 0.7）
- `ZHIHOU_COOKIE`：知乎登录 Cookie（浏览器发布用，可选）
- `TOPIC_COOLDOWN_DAYS`：主题冷却天数（默认 1）
- `ARTICLE_MIN_WORDS` / `ARTICLE_MAX_WORDS`：文章字数范围
- `TOPIC_ANGLES`：文章角度池（轮换避免重复）
- `UPLOAD_DIR`：上传临时目录（必须为 `/tmp/openclaw/uploads`）

## 完整自动流程（Step by Step）

当用户说"发知乎"、"发布到知乎"、"知乎热点发布"时，执行：

### Step 1 — 读取配置
```python
import yaml
import os
MINIMAX_API_KEY = os.environ.get("MINIMAX_API_KEY")  # 优先从环境变量读取
settings = yaml.safe_load(open("{skillDir}/settings.yaml"))
settings["MINIMAX_API_KEY"] = MINIMAX_API_KEY
```

### Step 2 — 抓取热点
调用 `{skillDir}/tools/topic_manager.py` 的 `TopicManager` 检查冷却状态。
调用 `{skillDir}/tools/article_generator.py` 的 `fetch_hn_ai_topics(limit=10)` 抓取 HN AI 热点。

### Step 3 — 选择主题（防重复）
用 `TopicManager.can_use_topic()` 过滤冷却期内主题。
用 `TopicManager.get_next_angle()` 获取本次角度（技术解析/产业分析/实战案例/未来预测 等）。

### Step 4 — 生成文章
```python
from tools.article_generator import generate_article
article_path = generate_article(topic, angle, settings)
```
调用 `mmx text chat`（MiniMax 模型），生成 2500-3500 字知乎文章。

**Prompt 内容约束（详见 article_generator.py）：**

#### 主题与调性
- **硬核科技** — 聚焦 AI 前沿、模型动态、产业落地，不写泛泛的"AI 改变生活"
- **国内视角** — 涉及国内外对比时重点分析差距、追赶路径、自主创新
- **时效性强** — 引用最新发布/论文/事件，不用模糊时间描述

#### 内容与结构
- 每篇至少包含一个：具体技术细节 / 真实案例 / 可操作的洞察
- 选 2-3 个核心点深入，不罗列
- 排版可读：自然段，重要数据可单独强调

#### 语言风格
- **有观点，不中立** — 可以站边，但用数据说话
- **用具体替代抽象** — ❌ "效果显著提升" → ✅ "延迟从 3s 到 800ms"
- **克制情绪，事实驱动**

#### 去 AI 味
- 禁止句式："X 是一种强大的工具"、"首先…其次…最后…"、"综上所述"
- 口语化，可以抛梗但不要强行搞笑
- 自检：匿名发知乎会被认成 AI 写吗？

### Step 5 — 生成封面图
```python
from tools.cover_generator import generate_cover
cover_path = generate_cover(topic['title'], title, settings)
```
调用 `mmx image generate`，赛博朋克/未来科技风格封面，下载保存到 `UPLOAD_DIR`。

### Step 6 — 发布到知乎（浏览器自动化）
```python
from tools.publisher import auto_publish
url = auto_publish(article_path, cover_path, title)
```

**关键流程（实测经验）：**
1. 打开 `https://zhuanlan.zhihu.com/write`
2. md 导入在 Playwright CDP 模式下不工作，必须通过 `keyboard.type()` 直接注入内容到编辑器
3. **上传封面图**（如有）
4. **在顶部标题框输入标题**（md 导入只导入正文，标题框是空的！）
5. 滚动到页面底部，添加话题：人工智能
6. 添加内容来源：官方网站（必填）
7. 点击"发布"

**文件上传路径：** 必须为 `/tmp/openclaw/uploads/`（OpenClaw browser upload 限制）

### Step 7 — 记录状态
```python
from tools.topic_manager import TopicManager
tm = TopicManager(settings)
tm.record_topic(topic['title'], angle, title)
```
更新 `/tmp/zhihu_topic_state.json`，避免 1 天内重复使用同一主题。

### Step 8 — 输出报告
```
✅ 知乎发布成功

主题：{topic_title}
角度：{angle}
文章字数：{word_count}
封面：{cover_path}
链接：{url}
冷却期：1 天
```

## 手动发布流程

当用户说"把这篇文章发到知乎"或"发布 [文章内容]"时：

1. 读取用户提供的文章内容或文件路径
2. 将文章保存到 `{UPLOAD_DIR}/article_{timestamp}.md`
3. 封面图：如有提供则上传；如无则跳过
4. 执行 Step 6（发布流程）中的浏览器自动化步骤
5. 输出发布链接

## 手动内容生成

当用户说"帮我写一篇知乎文章"、"生成一篇 AI 热点文章"时：

1. 抓取 HN AI 热点（Step 2）
2. 选择主题和角度（Step 3）
3. 生成文章（Step 4，去 AI 味）
4. 生成封面图（Step 5）
5. **不自动发布**，仅输出文章内容和封面路径，等待用户确认后发布

## Browser 工具使用规范

所有页面操作使用 OpenClaw 的 `browser` 工具：

| 操作 | 命令 |
|------|------|
| 打开页面 | `browser action=open url="https://zhuanlan.zhihu.com/write"` |
| 获取内容 | `browser action=snapshot` → 解析 ref |
| 点击元素 | `browser action=act request={kind:"click", ref:"<ref>"}` |
| 输入文本 | `browser action=act request={kind:"type", ref:"<ref>", text:"..."}` |
| 上传文件 | `browser action=upload paths=["/tmp/openclaw/uploads/file.md"]` |
| 等待 | `browser action=act request={kind:"wait", timeMs:3000}` |
| 关闭 | `browser action=stop` |

**重要规则：**
- 文件必须先 `cp` 到 `/tmp/openclaw/uploads/`，才能 browser upload
- 每次发布使用**全新的 write 页面**（导入是追加不是替换）
- md 导入在 Playwright CDP 模式下失败，内容需通过 `keyboard.type()` 注入
- 发布前确认"内容来源"已填（必填项）

## 实测坑点

### 1. md 文件导入不工作
**现象**：`setInputFiles()` 成功返回，但编辑器内容为空（char count = 1）
**原因**：知乎的文件上传 handler 检测到非原生文件选择，有检查逻辑
**解决**：不用导入，直接 `keyboard.type()` 注入内容到 `.public-DraftEditor-content`

### 2. 话题/来源按钮 innerText 含换行符
**现象**：用精确文本匹配找不到按钮
**原因**：`innerText = "\n添加话题"` 而不是 `"添加话题"`
**解决**：用 `.replace(/\s+/g, ' ').trim()` 去除空白后部分匹配

### 3. 话题下拉选项用键盘无法选中
**现象（旧）**：`ArrowDown + Enter` 无效
**原因**：如果用 `evaluate` 模拟.click() 打开弹窗，React 事件没触发，弹窗实际未打开
**修复**：必须用 Playwright 原生 `locator().filter({ hasText: '添加话题' }).click()` 打开弹窗
  → 弹窗正确打开后，`searchInput.fill() + ArrowDown + Enter` 即可选中

### 4. 来源选择需要两步
**现象**：点"添加来源"后，选项不直接出现
**解决**：先点"选择具体的信息来源"展开 → 选"官方网站" → "确认添加"

### 5. 发布按钮 enabled 条件
**现象**：内容+标题+话题+来源全填了，发布按钮仍然 disabled
**实际要求**：话题和来源**二选一**即可（两者都未选时 disabled）

## 注意事项

- API Key 必须从环境变量 `MINIMAX_API_KEY` 读取，**禁止硬编码**
- 同一主题至少间隔 1 天（冷却期）
- 同一主题使用不同角度轮换
- 每次生成全新结构和论述，不重复已有内容
- 发布后保留草稿链接，供用户确认
- API 调用失败时，打印错误信息并询问用户是否手动发布
- 浏览器操作超时（>60s 无响应）时，输出当前状态和可用的手动操作说明
