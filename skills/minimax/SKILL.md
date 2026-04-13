---
name: minimax
description: MiniMax CodingPlan — 封装 MiniMax 全模态模型（文本/语音/视频/图像/音乐）+ Token Plan MCP（网络搜索/图片理解）
type: skill
user-invocable: true
argument-hint: '[<任务描述>]'
---

# MiniMax CodingPlan

MiniMax 全模态 AI 能力包，涵盖文本生成、语音合成、视频生成、图像生成和音乐生成五大模态。

## 环境检查

1. 读取 `skills/.env` 中的 `MINIMAX_API_KEY`
2. 如果使用 TTS 或其他需要三方认证的接口，还需读取 `MINIMAX_APP_ID` 和 `MINIMAX_API_SECRET`
3. 缺少必填项时，执行配置流程

### 配置流程

**Step 1 — 获取 API Key**

前往 MiniMax 开放平台注册并获取 API Key：

- MiniMax 开放平台：https://www.minimax.io
- CodingPlan 订阅页面：https://www.minimaxi.com/user-center/basic-information/interface-key

**Step 2 — 配置 .env**

打开 `skills/.env`，确认以下字段：

```env
MINIMAX_API_KEY=你的API_KEY
MINIMAX_APP_ID=你的APP_ID       # 仅 TTS 等部分接口需要
MINIMAX_API_SECRET=你的SECRET    # 仅 TTS 等部分接口需要
```

**Step 3 — 验证配置**

告诉我"配置好了"，Skill 会读取 `.env` 验证认证信息。

---

## Token Plan MCP

MiniMax Token Plan 提供专属 MCP 服务，包含**网络搜索**和**图片理解**两个工具。配置后可在 Claude Code 中直接调用，无需手动发 API 请求。

### MCP 工具一览

| 工具 | 功能 | 说明 |
|------|------|------|
| `web_search` | 网络搜索 | 根据查询词搜索网络，返回结果和相关建议 |
| `understand_image` | 图片理解 | 分析图片内容，支持 URL 或本地文件路径 |

### 前置准备

**Step 1 — 订阅 Token Plan**

前往 https://platform.minimaxi.com/subscribe/token-plan 订阅套餐，获取 API Key。

**Step 2 — 安装 uvx**

uvx 是运行 MCP 的必需工具：

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# 验证安装
which uvx
```

**Step 3 — 在 Claude Code 中配置 MCP（一键安装）**

在终端运行：

```bash
claude mcp add -s user MiniMax \
  --env MINIMAX_API_KEY=你的API_KEY \
  --env MINIMAX_API_HOST=https://api.minimaxi.com \
  -- uvx minimax-coding-plan-mcp -y
```

或手动编辑 `~/.claude.json`，添加：

```json
{
  "mcpServers": {
    "MiniMax": {
      "command": "uvx",
      "args": ["minimax-coding-plan-mcp", "-y"],
      "env": {
        "MINIMAX_API_KEY": "你的API_KEY",
        "MINIMAX_API_HOST": "https://api.minimaxi.com"
      }
    }
  }
}
```

**Step 4 — 验证配置**

进入 Claude Code 后输入 `/mcp`，能看到 `web_search` 和 `understand_image`，说明配置成功。

### understand_image 支持的格式

| 格式 | 说明 |
|------|------|
| 输入方式 | HTTP/HTTPS URL 或本地文件路径 |
| 支持格式 | JPEG、PNG、GIF、WebP |
| 文件大小 | 最大 20MB |

### Cursor / OpenCode 配置（参考）

如在其他 IDE 中使用，配置方式类似：

**Cursor** — `Cursor -> Preferences -> Tools & Integrations -> MCP -> Add Custom MCP`，添加 `mcp.json` 配置：

```json
{
  "mcpServers": {
    "MiniMax": {
      "command": "uvx",
      "args": ["minimax-coding-plan-mcp"],
      "env": {
        "MINIMAX_API_KEY": "填写你的API密钥",
        "MINIMAX_API_HOST": "https://api.minimaxi.com"
      }
    }
  }
}
```

**OpenCode** — 编辑 `~/.config/opencode/opencode.json`：

```json
{
  "mcp": {
    "MiniMax": {
      "type": "local",
      "command": ["uvx", "minimax-coding-plan-mcp", "-y"],
      "environment": {
        "MINIMAX_API_KEY": "你的API_KEY",
        "MINIMAX_API_HOST": "https://api.minimaxi.com"
      },
      "enabled": true
    }
  }
}
```

---

## 文本模型

### 支持的模型

| 模型 ID | 说明 | 适用场景 |
|---------|------|---------|
| MiniMax-M2.7 | 旗舰文本模型，支持超长上下文 | 复杂推理、长文档、代码 |
| MiniMax-M2.5 | 高性价比文本模型 | 日常对话、写作、翻译 |
| MiniMax-M2.7-highspeed | 极速版专属，高速响应 | 实时对话、低延迟场景 |
| MiniMax-M2.5-highspeed | 极速版专属，高速响应 | 日常快速响应 |

> 注意：文本模型共享请求额度（5 小时滚动窗口）。非文本模型各自拥有独立的每日配额。

### API 调用（OpenAI 兼容格式）

MiniMax API 与 OpenAI API 兼容，使用 Anthropic Python SDK 或直接调用 REST API：

**Python SDK 方式：**

```python
import anthropic

client = anthropic.Anthropic(
    api_key="你的MINIMAX_API_KEY",
    base_url="https://api.minimax.chat/v1"
)

message = client.messages.create(
    model="MiniMax-M2.7",    # 切换模型：M2.7 / M2.5 / M2.7-highspeed / M2.5-highspeed
    max_tokens=4096,
    system="你是一个有帮助的AI助手。",
    messages=[
        {
            "role": "user",
            "content": "你的问题"
        }
    ]
)

print(message.content[0].text)
```

**REST API 方式：**

```bash
curl https://api.minimax.chat/v1/messages \
  -H "Authorization: Bearer $MINIMAX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "MiniMax-M2.7",
    "max_tokens": 4096,
    "messages": [
      {"role": "user", "content": "你好"}
    ]
  }'
```

### 常用参数

| 参数 | 说明 |
|------|------|
| `model` | 模型 ID，支持 M2.7 / M2.5 / M2.7-highspeed / M2.5-highspeed |
| `max_tokens` | 最大输出 token 数，建议 4096 |
| `system` | 系统提示词 |
| `temperature` | 随机性，0-2，默认 1。推理任务建议 0.3-0.5 |
| `top_p` | 核采样，默认 1 |

---

## TTS HD 语音合成

支持高清语音合成，多音色可选。

### 支持的模型

| 模型 ID | 说明 |
|---------|------|
| speech-2.8-hd | 最新高清语音，质量最高 |
| speech-2.6-hd | 高清语音，高性价比 |
| speech-02-hd | 经典高清语音，稳定可靠 |

### API 调用

**API 端点**：`POST https://api.minimax.io/v1/t2a_v2`

**请求体：**

```json
{
  "model": "speech-02-hd",
  "text": "要合成的文本内容",
  "stream": false,
  "voice_setting": {
    "voice_id": "male-qn-qingse",
    "speed": 1.0,
    "volume": 1.0,
    "pitch": 0,
    "emotion": "happy"
  }
}
```

**认证方式**：三方认证（API_KEY + APP_ID + API_SECRET）

**签名生成（Python）：**

```python
import time, hashlib, base64, hmac

def generate_signature(api_secret: str, app_id: str) -> tuple:
    t = str(int(time.time()))
    sign_str = f"{app_id}{t}"
    signature = base64.b64encode(
        hmac.new(api_secret.encode(), sign_str.encode(), hashlib.sha1)
    ).decode()
    return t, signature

t, signature = generate_signature("你的API_SECRET", "你的APP_ID")
```

**Headers：**

```
Authorization: Bearer $MINIMAX_API_KEY
Content-Type: application/json
X-APP-ID: $MINIMAX_APP_ID
X-Timestamp: <时间戳>
X-Signature: <签名>
```

### 常用音色

| voice_id | 名称 | 适用场景 |
|----------|------|---------|
| male-qn-qingse | 青年男声-清冷 | 正式解说、旁白 |
| female-shaonv | 少女音 | 可爱、活泼风格 |
| male-tianmei | 甜妹音 | 温柔内容 |
| female-yunyang | 云扬男声 | 新闻、播报 |
| female-xiaowei | 晓伟男声 | 磁性低沉 |

### 情绪参数

支持 `emotion` 参数：`happy` / `sad` / `angry` / `neutral`

### 最佳实践

- **文本预处理**：英文缩写和数字建议转为自然文字（如 `"AI"` → `"人工智能"`，`"2024年"` → `"二零二四年"`）
- **长度控制**：单次合成建议 500 字以内，过长分段合成后拼接
- **输出格式**：统一 `.mp3`，采样率 32000Hz
- **命名**：`voice_<timestamp>.mp3`

---

## 视频生成（Hailuo）

支持文生视频，支持多种分辨率和时长。

### 支持的模型

| 模型 ID | 说明 | 分辨率 | 时长 |
|---------|------|--------|------|
| Hailuo-2.3-Fast | 快速生成版 | 768P | 6s |
| Hailuo-2.3 | 标准版 | 768P | 6s |

### API 调用

**API 端点**：`POST https://api.minimax.chat/v1/video_generation`

**请求体：**

```json
{
  "model": "Hailuo-2.3",
  "prompt": "你的视频描述，建议包含动作、场景和氛围",
  "duration": 6
}
```

**Headers：**

```
Authorization: Bearer $MINIMAX_API_KEY
Content-Type: application/json
```

**响应处理：**

```json
{
  "task_id": "xxx",
  "status": "pending"
}
```

通过 `task_id` 轮询任务状态：

```bash
curl "https://api.minimax.chat/v1/video_generation?task_id=xxx" \
  -H "Authorization: Bearer $MINIMAX_API_KEY"
```

### Prompt 技巧

视频生成 Prompt 与图片不同，需要描述**动作和变化**：

| 要素 | 示例 |
|------|------|
| 主体动作 | "一个人在海边从左走到右" |
| 场景变化 | "天空从蓝色渐变为金色日落" |
| 氛围描述 | "未来感的城市夜景，霓虹灯光闪烁" |
| 避免 | 不要只说"一个人在海边"，要描述具体的动作 |

### 最佳实践

- 每次生成 6 秒，过长视频多段生成后拼接
- 统一输出 `.mp4`，命名 `video_<timestamp>.mp4`
- 生成时间约 1-3 分钟，使用 task_id 轮询等待

---

## 图像生成（image-01）

根据文本描述生成高质量图像。

### API 调用

**API 端点**：`POST https://api.minimax.chat/v1/image_generation`

**请求体：**

```json
{
  "model": "image-01",
  "prompt": "你的图像描述",
  "image_size": "1024x1024",
  "n": 1
}
```

**Headers：**

```
Authorization: Bearer $MINIMAX_API_KEY
Content-Type: application/json
```

**响应处理：** 从 `data[0].url` 获取图片 URL，下载保存。

### 常用尺寸

| size | 说明 |
|------|------|
| 1024x1024 | 正方形 |
| 1024x1792 | 竖版（9:16） |
| 1792x1024 | 横版（16:9） |

### 最佳实践

- Prompt 越具体效果越好，包含主体、风格、光线、色调等细节
- 支持中文 Prompt
- 输出命名：`image_<timestamp>.png`

---

## 音乐生成（Music-2.6）

根据文本描述生成音乐，最长 5 分钟。

### API 调用

**API 端点**：`POST https://api.minimax.chat/v1/music_generation`

**请求体：**

```json
{
  "model": "Music-2.6",
  "prompt": "你的音乐描述，如：欢快的流行音乐，有吉他伴奏，节奏明快",
  "duration": 300
}
```

**Headers：**

```
Authorization: Bearer $MINIMAX_API_KEY
Content-Type: application/json
```

### Prompt 技巧

| 要素 | 示例 |
|------|------|
| 风格 | 流行、古典、爵士、电子、摇滚 |
| 情绪 | 欢快、悲伤、平静、激昂 |
| 乐器 | 吉他、钢琴、鼓、弦乐 |
| 节奏 | 快节奏、慢节奏、中速 |

---

## 快速任务模板

直接告诉我你想做什么，自动调用对应模型：

- **文本对话**：`/minimax 你好，请介绍一下你自己`
- **语音合成**：`/tts 你好，欢迎使用 MiniMax`
- **生成视频**：`/video 一个人在海边跑步，日落背景`
- **生成图片**：`/image 一只可爱的橘猫在阳光下睡觉`
- **生成音乐**：`/music 欢快的吉他弹唱，户外民谣风格`

---

## 配额说明

| 模型类型 | 配额机制 |
|---------|---------|
| 文本模型（M2.7/M2.5） | 共享请求额度（5 小时滚动窗口） |
| TTS HD | 独立每日配额 |
| Hailuo 视频 | 独立每日配额 |
| image-01 | 独立每日配额 |
| Music-2.6 | 独立每日配额 |

具体配额由 CodingPlan 套餐等级决定。
