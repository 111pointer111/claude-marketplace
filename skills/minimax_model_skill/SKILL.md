---
name: minimax_model_skill
description: MiniMax 全模态 Skill — 语音合成、音色克隆、音色设计、音乐生成、视频生成、图像生成，统一通过 mmx CLI 调用
type: skill
user-invocable: true
argument-hint: '[<任务描述>]'
---

# MiniMax 全模态 Skill（mmx CLI）

MiniMax 全模态 AI 能力包，通过 `mmx` CLI 提供语音合成、音色克隆、音色设计、音乐生成、视频生成、图像生成等全部多模态能力。

**用户只需配置一个 API Key，所有工具统一通过 CLI 调用。**

---

## 环境检查（每次加载必执行）

1. 检查 `mmx` 是否已安装：`which mmx`
2. 若未安装，自动执行：`npm install -g mmx-cli`
3. 检查 `skills/.env` 中是否存在 `MINIMAX_API_KEY`
4. 若不存在，引导用户配置（见下方）
5. 检查认证状态：`mmx auth status`，若未登录执行 `mmx auth login --api-key <key>`

---

## 优先原则

1. **优先使用 mmx CLI**：能用 `mmx` 完成的操作，优先用 CLI
2. **CLI 不可用时使用 REST API**：如 `mmx` 安装失败或特定场景下，用 REST API 手动调用
3. **文本对话**：Claude Code 默认使用 Claude 模型，无需走 MiniMax 文本 API

---

## 第一步：安装 mmx CLI

```bash
npm install -g mmx-cli
```

---

## 第二步：配置 API Key

### 引导用户配置

Agent 读取 `skills/.env`，若缺少 `MINIMAX_API_KEY`，自动引导：

1. 告知用户前往 MiniMax 开放平台获取 API Key：
   - 平台地址：https://platform.minimaxi.com/user-center/basic-information/interface-key
   - 点击"Create new secret key"创建新的 API Key
2. 引导用户编辑 `skills/.env`，填入 `MINIMAX_API_KEY`
3. 执行认证：`mmx auth login --api-key <MINIMAX_API_KEY>`

### .env 示例配置

```env
MINIMAX_API_KEY=你的API_KEY
```

---

## Agent Flags

在非交互式（agent/CI）环境中，**必须**使用以下 flags：

| Flag | 用途 |
|------|------|
| `--non-interactive` | 缺少参数时快速失败，而非交互式提示 |
| `--quiet` | 抑制进度条/旋转指示器，stdout 只输出纯数据 |
| `--output json` | 机器可读的 JSON 输出 |
| `--async` | 立即返回任务 ID（视频生成） |
| `--yes` | 跳过确认提示 |

---

## CLI 命令详解

### 语音合成 — speech synthesize

文本转语音。默认模型：`speech-2.8-hd`。最大 10k 字符。

```bash
mmx speech synthesize --text <text> [flags]
```

| Flag | 类型 | 说明 |
|------|------|------|
| `--text <text>` | string | 待合成文本 |
| `--text-file <path>` | string | 从文件读取文本，`-` 表示 stdin |
| `--model <model>` | string | `speech-2.8-hd`（默认）、`speech-2.6`、`speech-02` |
| `--voice <id>` | string | 音色 ID（默认 `English_expressive_narrator`） |
| `--speed <n>` | number | 语速倍数 |
| `--volume <n>` | number | 音量 |
| `--pitch <n>` | number | 音调调整 |
| `--format <fmt>` | string | 格式（默认 `mp3`） |
| `--language <code>` | string | 语言增强 |
| `--subtitles` | boolean | 包含字幕时间数据 |
| `--sound-effect <effect>` | string | 添加音效 |
| `--out <path>` | string | 保存音频到文件 |

**音色选择参考（中文常用）：**

| voice_id | 名称 | 风格 |
|----------|------|------|
| `female-shaonv` | 少女音 | 可爱活泼 |
| `male-qn-qingse` | 青年男声-清冷 | 正式旁白 |
| `male-tianmei` | 甜妹音 | 温柔 |
| `female-yunyang` | 云扬男声 | 新闻播报 |
| `female-xiaowei` | 晓伟男声 | 磁性低沉 |

**最佳实践：**
- 英文缩写和数字建议预先转为自然文字（`"AI"` → `"人工智能"`，`"2024年"` → `"二零二四年"`）
- 单次合成建议 500 字以内，过长分段合成后拼接

```bash
mmx speech synthesize --text "你好世界" --voice female-shaonv --out hello.mp3 --quiet
echo "长文本" | mmx speech synthesize --text-file - --out long.mp3
```

---

### 音色克隆 — 不支持 CLI

`mmx` CLI 不支持音色克隆。如需克隆音色，使用 REST API：

```bash
curl -X POST "https://api.minimaxi.com/v1/voice_clone" \
  -H "Authorization: Bearer $MINIMAX_API_KEY" \
  -F "voice_id=<自定义ID>" \
  -F "file=@<音频文件>" \
  -F "text=<演示文本>"
```

---

### 音乐生成 — music generate

生成音乐。模型：`music-2.5`。

```bash
mmx music generate --prompt <text> [--lyrics <text>] [flags]
```

| Flag | 类型 | 说明 |
|------|------|------|
| `--prompt <text>` | string | 音乐风格描述 |
| `--lyrics <text>` | string | 歌词，支持结构标签 `[Intro]` `[Verse]` `[Chorus]` `[Bridge]` `[Outro]` |
| `--lyrics-file <path>` | string | 从文件读取歌词 |
| `--vocals <text>` | string | 人声风格，如 `"warm male baritone"` |
| `--genre <text>` | string | 流派，如 folk, pop, jazz |
| `--mood <text>` | string | 情绪，如 warm, melancholic |
| `--instruments <text>` | string | 乐器，如 `"acoustic guitar, piano"` |
| `--tempo <text>` | string | 节奏，如 fast, slow, moderate |
| `--bpm <number>` | number | BPM |
| `--structure <text>` | string | 曲式结构 |
| `--references <text>` | string | 参考曲目或艺术家 |
| `--avoid <text>` | string | 要避免的元素 |
| `--instrumental` | boolean | 纯音乐（无人声） |
| `--out <path>` | string | 保存路径 |

```bash
mmx music generate --prompt "中文民谣" --lyrics "[Verse]\n清晨的便利店..." --out song.mp3 --quiet
mmx music generate --prompt "Cinematic orchestral" --instrumental --out bgm.mp3 --quiet
```

---

### 视频生成 — video generate

生成视频。默认模型：`MiniMax-Hailuo-2.3`。异步任务，默认轮询直到完成。

```bash
mmx video generate --prompt <text> [flags]
```

| Flag | 类型 | 说明 |
|------|------|------|
| `--prompt <text>` | string | 视频描述 |
| `--model <model>` | string | `MiniMax-Hailuo-2.3`（默认）或 `MiniMax-Hailuo-2.3-Fast` |
| `--first-frame <path-or-url>` | string | 首帧图片 |
| `--download <path>` | string | 保存视频到指定路径 |
| `--async` | boolean | 立即返回任务 ID |
| `--poll-interval <seconds>` | number | 轮询间隔（默认 5） |

```bash
# 阻塞模式：等待完成并保存
mmx video generate --prompt "海边日落" --download sunset.mp4 --quiet

# 非阻塞模式：获取任务 ID
mmx video generate --prompt "机器人" --async --quiet
# 返回: {"taskId":"..."}
```

### 查询视频任务 — video task get

```bash
mmx video task get --task-id <id> [--output json]
```

### 下载视频 — video download

```bash
mmx video download --file-id <id> [--out <path>]
```

---

### 图片生成 — image generate

生成图片。模型：`image-01`。

```bash
mmx image generate --prompt <text> [flags]
```

| Flag | 类型 | 说明 |
|------|------|------|
| `--prompt <text>` | string | 图片描述 |
| `--aspect-ratio <ratio>` | string | 宽高比，如 `16:9`, `1:1` |
| `--n <count>` | number | 生成数量（默认 1） |
| `--subject-ref <params>` | string | 主体参考：`type=character,image=path-or-url` |
| `--out-dir <dir>` | string | 保存目录 |
| `--out-prefix <prefix>` | string | 文件名前缀 |

```bash
mmx image generate --prompt "可爱的橘猫" --out-dir ./gen/ --quiet
mmx image generate --prompt "Logo" --n 3 --aspect-ratio 1:1 --quiet
```

---

### 图片理解 — vision describe

图片分析。提供 `--image` 或 `--file-id` 之一。

```bash
mmx vision describe (--image <path-or-url> | --file-id <id>) [flags]
```

| Flag | 类型 | 说明 |
|------|------|------|
| `--image <path-or-url>` | string | 本地路径或 URL |
| `--file-id <id>` | string | 已上传的文件 ID |
| `--prompt <text>` | string | 关于图片的问题（默认 `"Describe the image."`） |

```bash
mmx vision describe --image photo.jpg --prompt "这是什么品种?" --output json
```

---

### 网页搜索 — search query

```bash
mmx search query --q <query> [--output json --quiet]
```

---

### 配额查询 — quota show

```bash
mmx quota show [--output json]
```

---

## Piping 模式

```bash
# stdout 始终是纯数据，可安全管道
mmx text chat --message "Hi" --output json | jq '.content'

# stderr 有进度信息，需要时丢弃
mmx video generate --prompt "Waves" 2>/dev/null

# 链式：生成图片 → 描述图片
URL=$(mmx image generate --prompt "A sunset" --quiet)
mmx vision describe --image "$URL" --quiet

# 异步视频工作流
TASK=$(mmx video generate --prompt "A robot" --async --quiet | jq -r '.taskId')
mmx video task get --task-id "$TASK" --output json
mmx video download --file-id "$TASK" --out robot.mp4
```

---

## 退出码

| 代码 | 含义 |
|------|------|
| 0 | 成功 |
| 1 | 通用错误 |
| 2 | 用法错误（错误的 flags、缺少参数） |
| 3 | 认证错误 |
| 4 | 配额超限 |
| 5 | 超时 |
| 10 | 内容过滤触发 |

---

## 配置优先级

CLI flags → 环境变量 → `~/.mmx/config.json` → 默认值

```bash
# 持久化配置
mmx config set --key region --value cn
mmx config show

# 环境变量
export MINIMAX_API_KEY=sk-xxxxx
export MINIMAX_REGION=cn
```

---

## REST API（备用：CLI 不可用时）

如需直接调用 REST API（不使用 CLI），参考以下端点和认证方式。

### 认证

所有 REST API 请求统一使用 `MINIMAX_API_KEY`：

```
Authorization: Bearer $MINIMAX_API_KEY
Content-Type: application/json
```

### 端点总览

| 能力 | 端点 | Base URL |
|------|------|-----------|
| 文本模型 | `POST /v1/messages` | `https://api.minimax.chat` |
| 语音合成 | `POST /v1/t2a_v2` | `https://api.minimax.io` |
| 视频生成 | `POST /v1/video_generation` | `https://api.minimax.chat` |
| 图片生成 | `POST /v1/image_generation` | `https://api.minimax.chat` |
| 音乐生成 | `POST /v1/music_generation` | `https://api.minimax.chat` |

---

## 配额说明

| 模型类型 | 配额机制 |
|---------|---------|
| 文本模型（M2.7/M2.5） | 5 小时滚动窗口 |
| TTS / 语音合成 | 独立每日配额 |
| Hailuo 视频 | 独立每日配额 |
| 图片生成 | 独立每日配额 |
| 音乐生成 | 独立每日配额 |

具体配额由 CodingPlan 套餐等级决定。

---

## 快速任务

| 需求 | 命令 |
|------|------|
| 生成语音 | `mmx speech synthesize --text "..." --out voice.mp3` |
| 生成音乐 | `mmx music generate --prompt "..." --lyrics "..." --out song.mp3` |
| 文生视频 | `mmx video generate --prompt "..." --download video.mp4` |
| 图生视频 | `mmx video generate --prompt "..." --first-frame img.jpg --download video.mp4` |
| 查询视频进度 | `mmx video task get --task-id <id>` |
| 生成图片 | `mmx image generate --prompt "..." --out-dir ./gen/` |
| 图片理解 | `mmx vision describe --image photo.jpg` |
| 网页搜索 | `mmx search query --q "..."` |
| 查看配额 | `mmx quota show` |
