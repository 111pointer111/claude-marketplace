---
name: video-generation
description: 视频生成 — 封装 Runway / Pika / Kling 等主流视频生成 API 的调用方法
type: skill
user-invocable: true
argument-hint: '[<prompt描述>]'
---

# 视频生成

根据文本描述生成视频。

## 环境检查

1. 读取 `skills/.env` 中的 `VIDEO_PROVIDER` 和对应 provider 的 API Key
2. 检查必填字段：
   - `VIDEO_PROVIDER`：当前选用的 provider（`runway` / `pika` / `kling`）
   - 对应 provider 的 API Key
3. 缺少任何必填项时，执行配置流程（见下方"配置流程"章节）
4. 配置完成后继续执行视频生成任务

## 配置流程

### 缺少 VIDEO_PROVIDER 或 API Key

**Step 1 — 选择 Provider 并申请 Key**

| Provider | 特点 | 申请地址 | 费用 |
|----------|------|---------|------|
| Runway | 质量高，支持文生视频/图生视频 | https://runwayml.com/api |
| Pika | 适合动画风格，生成速度快 | https://pika.art/api |
| Kling | 快手出品，国产首选，性价比高 | https://klingai.com |

选择好 provider 后，前往对应平台申请 API Key。

**Step 2 — 配置 .env 文件**

1. 打开 `skills/.env`
2. 设置 `VIDEO_PROVIDER` 为你选定的 provider（如 `runway`）
3. 填入对应的 API Key（如 `RUNWAY_API_KEY=sk-xxx`）
4. 其他 provider 的 key 可以留空，不影响

**Step 3 — 验证配置**

配置完成后，告诉我"配置好了"，Skill 会读取 `.env` 验证 key 是否有效。

## 视频生成

配置完成后，直接告诉我你想生成什么样的视频，例如：

- `/video 一个人在海边跑步，日落背景`
- `/video 一只猫在弹钢琴，写实风格`

Skill 会根据你选择的 provider 调用对应 API，完成视频生成。

## Provider 调用方法

### Runway

**API 端点**：`POST https://api.runwayml.com/v1/video/text_to_video`

**请求体**：
```json
{
  "prompt": "<你的描述>",
  "model": "gen3a_turbo",
  "duration": 5,
  "aspect_ratio": "16:9"
}
```

**Headers**：
```
Authorization: Bearer $RUNWAY_API_KEY
Content-Type: application/json
```

**响应处理**：从响应中提取 `video_url`，下载并保存为本地文件。

---

### Pika

**API 端点**：`POST https://api.pika.art/v1/video/generate`

**请求体**：
```json
{
  "prompt": "<你的描述>",
  "aspect_ratio": "16:9",
  "fps": 24,
  "frames": 240
}
```

**Headers**：
```
Authorization: Bearer $PIKA_API_KEY
Content-Type: application/json
```

**响应处理**：轮询 job 状态，任务完成后下载视频文件。

---

### Kling

**API 端点**：`POST https://api.klingai.com/v1/videos/text2video`

**请求体**：
```json
{
  "prompt": "<你的描述>",
  "aspect_ratio": "16:9",
  "duration": "5s",
  "model": "kling-v1"
}
```

**Headers**：
```
Authorization: Bearer $KLING_API_KEY
Content-Type: application/json
```

**响应处理**：从响应中获取 `task_id`，通过 `GET /v1/videos/{task_id}` 查询任务状态，完成后下载视频。

---

## 通用最佳实践

- **Prompt 优化**：视频生成的 prompt 与图片不同，需要描述**动作、场景变化、时间感**。例如"一个人从左走到右"比"一个人在走路"效果更好
- **时长选择**：大多数 API 支持 5-10 秒，生成更长视频需要多段生成后拼接
- **宽高比**：统一使用 `16:9`（横版）或 `9:16`（竖版），避免中途切换
- **生成速度**：Runway 约 1-2 分钟，Pika 约 30 秒，Kling 约 1-3 分钟
- **输出格式**：统一保存为 `.mp4` 文件，命名格式 `video_<timestamp>.mp4`
