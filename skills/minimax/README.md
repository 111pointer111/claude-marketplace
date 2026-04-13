# MiniMax — CodingPlan 全模态能力包

封装了 MiniMax CodingPlan 支持的所有模型调用方法，覆盖文本、语音、视频、图像、音乐五大模态，以及 Token Plan MCP 服务。

## 模型一览

| 模态 | 模型 | 说明 |
|------|------|------|
| **文本** | MiniMax-M2.7 / M2.5 | 旗舰文本模型，支持超长上下文 |
| **文本(极速)** | M2.7-highspeed / M2.5-highspeed | 极速版专属，低延迟响应 |
| **语音合成** | speech-2.8-hd / 2.6-hd / 02-hd | 高清 TTS，多音色可选 |
| **视频生成** | Hailuo-2.3-Fast / Hailuo-2.3 | 文生视频，768P 6秒 |
| **图像生成** | image-01 | 高质量文生图 |
| **音乐生成** | Music-2.6 | 最长 5 分钟音乐 |
| **MCP** | web_search / understand_image | 网络搜索 + 图片理解 |

## 安装

Skill 文件在 `skills/minimax/SKILL.md`，Claude Code 加载后直接可用。

## 快速开始

### 1. 配置 API Key

```bash
# 复制模板
cp skills/.env.example skills/.env

# 编辑 skills/.env
# MINIMAX_API_KEY=你的API_KEY
# MINIMAX_APP_ID=你的APP_ID         # 仅 TTS 需要
# MINIMAX_API_SECRET=你的SECRET       # 仅 TTS 需要
```

### 2. 配置 MCP（可选，推荐）

MCP 提供网络搜索和图片理解工具，配置后在 Claude Code 中可直接调用：

```bash
claude mcp add -s user MiniMax \
  --env MINIMAX_API_KEY=你的API_KEY \
  --env MINIMAX_API_HOST=https://api.minimaxi.com \
  -- uvx minimax-coding-plan-mcp -y
```

### 3. 开始使用

```bash
/minimax 你好，请介绍一下 MiniMax 的文本模型
/video 一个人在海边跑步，日落背景
/tts 你好，欢迎使用 MiniMax
/image 一只可爱的橘猫在阳光下睡觉
/music 欢快的吉他弹唱，户外民谣风格
```

## Token Plan MCP

Token Plan 专属 MCP 提供两个工具：

| 工具 | 功能 |
|------|------|
| `web_search` | 网络搜索，返回搜索结果和建议 |
| `understand_image` | 图片理解，支持 URL 或本地文件（最大 20MB） |

配置后在 Claude Code 中输入 `/mcp` 验证是否连接成功。

## 快速任务

| 任务 | 命令示例 |
|------|---------|
| 文本对话 | `/minimax 帮我写一段 Python 代码` |
| 语音合成 | `/tts 今天天气真好` |
| 视频生成 | `/video 赛博朋克风格的城市夜景` |
| 图像生成 | `/image 未来感的机械臂在工厂作业` |
| 音乐生成 | `/music 平静的钢琴曲，适合冥想` |
| 网络搜索 | 直接说"帮我搜索 xxx"，MCP 自动调用 |
| 图片理解 | 直接发图片并提问，MCP 自动分析 |

## API 调用示例

### Python（文本模型）

```python
import anthropic

client = anthropic.Anthropic(
    api_key="你的MINIMAX_API_KEY",
    base_url="https://api.minimax.chat/v1"
)

message = client.messages.create(
    model="MiniMax-M2.7",
    max_tokens=4096,
    system="你是一个有帮助的AI助手。",
    messages=[{"role": "user", "content": "你好"}]
)
print(message.content[0].text)
```

### curl（视频生成）

```bash
curl -X POST https://api.minimax.chat/v1/video_generation \
  -H "Authorization: Bearer $MINIMAX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"Hailuo-2.3","prompt":"一个人在海边跑步","duration":6}'
```

## 项目结构

```
minimax/
├── SKILL.md      # 核心指令文件（所有模型 + MCP 调用方法）
└── README.md     # 本文件
```
