---
name: minimax_model_skill
description: MiniMax 全模态 Skill — 语音合成、音色克隆、音色设计、音乐生成、视频生成、图像生成，统一通过 MiniMax MCP 调用
type: skill
user-invocable: true
argument-hint: '[<任务描述>]'
---

# MiniMax 全模态 Skill

MiniMax 全模态 AI 能力包，通过 MiniMax MCP 提供语音合成、音色克隆、音色设计、音乐生成、视频生成、图像生成等全部多模态能力。

**用户只需配置一个 API Key，所有工具统一通过 MCP 调用。**

---

## 优先原则

1. **优先使用 MCP 工具**：能用 MCP 完成的操作，优先用 MCP（工具会自动保存文件到本地）
2. **MCP 不可用时使用 REST API**：如 MCP 未安装或特定场景下，用 REST API 手动调用
3. **文本对话**：Claude Code 默认使用 Claude 模型，无需走 MiniMax 文本 API

---

## 第一步：安装 MCP（Agent 自动执行）

**无需用户手动操作，Agent 检测到未安装时自动执行。**

### 1.1 检查 MCP 是否已安装

Agent 每次加载此 Skill 时，先检查 Claude Code MCP 配置中是否存在 `MiniMax` 服务器。若已安装，跳过安装步骤。

### 1.2 安装 uvx（如未安装）

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 1.3 配置环境变量

先读取 `skills/.env` 中的 `MINIMAX_API_KEY`。若不存在，引导用户配置。

### 1.4 安装 MCP

从 `skills/.env` 读取以下变量：
- `MINIMAX_API_KEY`（必需）
- `MINIMAX_MCP_BASE_PATH`（本地输出目录，如 `~/Desktop/MiniMax-Output`，默认 `~/Desktop/MiniMax-Output`）
- `MINIMAX_API_HOST`（默认 `https://api.minimaxi.com`）

然后运行：

```bash
claude mcp add -s user MiniMax \
  --env MINIMAX_API_KEY=<MINIMAX_API_KEY> \
  --env MINIMAX_API_HOST=<MINIMAX_API_HOST> \
  --env MINIMAX_MCP_BASE_PATH=<MINIMAX_MCP_BASE_PATH> \
  -- uvx minimax-mcp -y
```

### 1.5 验证 MCP

调用 MCP 工具 `list_voices`（查询音色列表），若返回结果说明 MCP 安装成功。

### 1.6 安装后重启 Claude Code

告知用户需重启 Claude Code，MCP 工具才能生效。

---

## 第二步：配置 API Key（用户执行一次）

### 引导用户配置

Agent 读取 `skills/.env`，若缺少 `MINIMAX_API_KEY`，自动引导：

1. 告知用户前往 MiniMax 开放平台获取 API Key：
   - 平台地址：https://platform.minimaxi.com/user-center/basic-information/interface-key
   - 点击"Create new secret key"创建新的 API Key
2. 引导用户编辑 `skills/.env`，填入 `MINIMAX_API_KEY`
3. 引导用户设置 `MINIMAX_MCP_BASE_PATH`（本地输出目录，生成的文件会保存到这里）
4. 验证配置：调用 `list_voices` 测试 key 是否有效

### .env 示例配置

```env
MINIMAX_API_KEY=你的API_KEY
MINIMAX_MCP_BASE_PATH=~/Desktop/MiniMax-Output
MINIMAX_API_HOST=https://api.minimaxi.com
```

---

## MCP 工具详解

### 工具一览

| 工具 | 功能 | 关键参数 |
|------|------|---------|
| `text_to_audio` | 文本转语音 | `text`, `voice_id`, `model`, `emotion`, `speed`, `output_directory` |
| `list_voices` | 查询可用音色 | `voice_type`（system / voice_cloning / voice_generation / all） |
| `voice_clone` | 克隆音色 | `voice_id`, `file`, `text`, `output_directory` |
| `voice_design` | AI 生成音色 | `prompt`, `preview_text`, `voice_id`, `output_directory` |
| `play_audio` | 播放音频 | `input_file_path` |
| `music_generation` | 生成音乐 | `prompt`, `lyrics`, `output_directory` |
| `generate_video` | 生成视频 | `prompt`, `model`, `first_frame_image`, `duration`, `resolution`, `output_directory` |
| `image_to_video` | 图片转视频 | `prompt`, `first_frame_image`, `output_directory`（仅 JS 版 MCP 支持） |
| `query_video_generation` | 查询视频任务状态 | `task_id` |
| `text_to_image` | 生成图片 | `prompt`, `model`, `aspect_ratio`, `n`, `output_directory` |

---

### text_to_audio — 语音合成

将文本合成为自然语音。

| 参数 | 必填 | 说明 | 默认值 |
|------|------|------|--------|
| `text` | 是 | 待合成的文本，< 10000 字符，段落用换行符分隔 | — |
| `output_directory` | 否 | 保存目录 | `MINIMAX_MCP_BASE_PATH` |
| `voice_id` | 否 | 音色编号 | `female-shaonv` |
| `model` | 否 | 模型：`speech-02-hd` / `speech-2.6-hd` / `speech-2.8-hd` | `speech-02-hd` |
| `speed` | 否 | 语速，范围 [0.5 - 2.0] | `1.0` |
| `vol` | 否 | 音量 | `1.0` |
| `pitch` | 否 | 音调，整数 [-12, 12] | `0` |
| `emotion` | 否 | 情绪：`happy` / `sad` / `angry` / `fearful` / `disgusted` / `surprised` / `calm` / `whisper` | `happy` |
| `sample_rate` | 否 | 采样率：`8000` / `16000` / `22050` / `24000` / `32000` / `44100` | `32000` |
| `bitrate` | 否 | 比特率：`32000` / `64000` / `128000` / `256000`（仅 mp3） | `128000` |
| `format` | 否 | 格式：`mp3` / `pcm` / `flac` / `wav` | `mp3` |
| `language_boost` | 否 | 语言增强，提升小语种/方言表现 | `null` |

**音色选择参考：**

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
- 情绪参数 `emotion` 仅对 speech-02-hd / speech-2.6-hd 等高清模型生效

---

### list_voices — 查询音色列表

| 参数 | 必填 | 说明 | 默认值 |
|------|------|------|--------|
| `voice_type` | 否 | `system`（系统音色）/ `voice_cloning`（克隆音色）/ `voice_generation`（AI生成音色）/ `all` | `all` |

---

### voice_clone — 音色克隆

根据音频文件克隆音色。

| 参数 | 必填 | 说明 |
|------|------|------|
| `voice_id` | 是 | 自定义音色 ID，首字符必须为英文字母，允许数字、`-`、`_`，末位不可为 `-`、`_`，不可与已有 ID 重复 |
| `file` | 是 | 音频文件路径，支持 `mp3` / `m4a` / `wav` |
| `text` | 否 | 克隆音色演示文本，< 2000 字符 |
| `output_directory` | 否 | 保存目录 |
| `is_url` | 否 | `file` 是否为 URL，默认 `false` |

---

### voice_design — AI 生成音色

根据文本描述生成全新音色。

| 参数 | 必填 | 说明 |
|------|------|------|
| `prompt` | 是 | 生成音色的描述，如："Mysterious narrator with deep magnetic voice" |
| `preview_text` | 是 | 试听文本 |
| `voice_id` | 否 | 自定义音色 ID，不填则自动生成唯一 ID |
| `output_directory` | 否 | 保存目录 |

---

### play_audio — 播放音频

| 参数 | 必填 | 说明 |
|------|------|------|
| `input_file_path` | 是 | 音频文件路径或 URL |
| `is_url` | 否 | 是否为 URL，默认 `false` |

---

### music_generation — 音乐生成

根据提示词和歌词生成音乐，最长 5 分钟。

| 参数 | 必填 | 说明 | 默认值 |
|------|------|------|--------|
| `prompt` | 是 | 音乐创作灵感，描述风格/情绪/场景，10-300 字符 | — |
| `lyrics` | 是 | 歌词，用换行符分隔每行，支持结构标签 `[Intro]` `[Verse]` `[Chorus]` `[Bridge]` `[Outro]` | — |
| `sample_rate` | 否 | 采样率 | `32000` |
| `bitrate` | 否 | 比特率 | `128000` |
| `format` | 否 | 格式：`mp3` / `wav` / `pcm` | `mp3` |
| `output_directory` | 否 | 保存目录 | `MINIMAX_MCP_BASE_PATH` |

**歌词结构标签示例：**
```
[Intro]
轻柔的钢琴声响起

[Verse]
月光洒在窗台上
星星点点闪烁

[Chorus]
这就是爱的旋律
永远不停止
```

---

### generate_video — 视频生成

根据文本或图片生成视频，`prompt` 和 `first_frame_image` 至少有其一。

| 参数 | 必填 | 说明 | 默认值 |
|------|------|------|--------|
| `prompt` | 否 | 视频描述，< 2000 字符 | — |
| `first_frame_image` | 否 | 首帧图片，`data:image/jpeg;base64,<data>` 格式或公网 URL | — |
| `model` | 否 | 模型见下方模型列表 | `T2V-01` |
| `duration` | 否 | 时长（秒），与模型相关 | `6` |
| `resolution` | 否 | 分辨率，与模型相关 | — |
| `output_directory` | 否 | 保存目录 | `MINIMAX_MCP_BASE_PATH` |
| `async_mode` | 否 | 异步模式，`true` 返回 task_id，`false` 等待完成 | `false` |

**模型选择：**

| 模型 | 类型 | 分辨率 | 时长 |
|------|------|--------|------|
| `MiniMax-Hailuo-02` | 文/图生视频 | 512P / 768P / 1080P | 6s / 10s |
| `T2V-01-Director` | 文生视频 | 不支持设置 | 6s |
| `I2V-01-Director` | 图生视频 | 不支持设置 | 6s |
| `S2V-01` | 主体驱动 | 不支持设置 | 6s |
| `I2V-01-live` | 图生视频 | 不支持设置 | 6s |
| `T2V-01` | 文生视频 | 不支持设置 | 6s |

**分辨率说明（Hailuo-02 专用）：**
- 6s 时长：默认 `768P`，可选 `512P` / `768P` / `1080P`
- 10s 时长：默认 `768P`，可选 `512P` / `768P`

**Prompt 技巧：** 视频 Prompt 需要描述动作和变化，不要只说主体，要描述具体的动作轨迹、场景变化、氛围。

**异步模式：** 视频生成耗时较长（1-3 分钟）。`async_mode=true` 时立即返回 task_id，通过 `query_video_generation` 查询状态。

---

### image_to_video — 图片转视频

使用首帧图片生成视频。**仅 JavaScript/TypeScript 版 MCP 支持。**

| 参数 | 必填 | 说明 | 默认值 |
|------|------|------|--------|
| `prompt` | 是 | 视频描述 | — |
| `first_frame_image` | 是 | 首帧图片，Base64 或 URL | — |
| `model` | 否 | 同 `generate_video` | `T2V-01` |
| `output_directory` | 否 | 保存目录 | `MINIMAX_MCP_BASE_PATH` |
| `async_mode` | 否 | 异步模式 | `false` |

---

### query_video_generation — 查询视频任务状态

| 参数 | 必填 | 说明 |
|------|------|------|
| `task_id` | 是 | 视频生成任务 ID |
| `output_directory` | 否 | 保存目录 |

---

### text_to_image — 图片生成

| 参数 | 必填 | 说明 | 默认值 |
|------|------|------|--------|
| `prompt` | 是 | 图像描述，< 1500 字符 | — |
| `model` | 否 | `image-01` / `image-01-live` | `image-01` |
| `aspect_ratio` | 否 | 宽高比：`1:1` / `16:9` / `4:3` / `3:2` / `2:3` / `3:4` / `9:16` / `21:9` | `1:1` |
| `n` | 否 | 单次生成数量 | `1` |
| `prompt_optimizer` | 否 | 自动优化提示词 | `true` |
| `output_directory` | 否 | 保存目录 | `MINIMAX_MCP_BASE_PATH` |

---

## REST API（备用：MCP 不可用时）

如需直接调用 REST API（不使用 MCP），参考以下端点和认证方式。

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

### 文本模型（OpenAI 兼容格式）

```bash
curl https://api.minimax.chat/v1/messages \
  -H "Authorization: Bearer $MINIMAX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "MiniMax-M2.7",
    "max_tokens": 4096,
    "messages": [{"role": "user", "content": "你好"}]
  }'
```

支持的模型：`MiniMax-M2.7` / `MiniMax-M2.5` / `M2.7-highspeed` / `M2.5-highspeed`

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

用户可以直接说需求，Agent 自动选择最合适的 MCP 工具：

| 需求 | 工具 |
|------|------|
| 生成语音 | `text_to_audio` |
| 找音色 | `list_voices` |
| 克隆音色 | `voice_clone` |
| AI 设计音色 | `voice_design` |
| 生成音乐 | `music_generation` |
| 文生视频 | `generate_video`（纯 prompt） |
| 图生视频 | `generate_video`（含 first_frame_image）或 `image_to_video` |
| 查询视频进度 | `query_video_generation` |
| 生成图片 | `text_to_image` |
