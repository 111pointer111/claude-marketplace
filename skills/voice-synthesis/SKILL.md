---
name: voice-synthesis
description: 配音合成 — 封装 MiniMax / 通义千问 TTS 等语音合成 API 的调用方法
type: skill
user-invocable: true
argument-hint: '[<要合成的文本>]'
---

# 配音合成

根据文本生成自然语音。

## 环境检查

1. 读取 `skills/.env` 中的 `VOICE_PROVIDER` 和对应 provider 的 API Key
2. 检查必填字段：
   - `VOICE_PROVIDER`：当前选用的 provider（`minimax` / `qwen`）
   - 对应 provider 的认证信息
3. 缺少任何必填项时，执行配置流程（见下方"配置流程"章节）
4. 配置完成后继续执行配音任务

## 配置流程

### 缺少 VOICE_PROVIDER 或认证信息

**Step 1 — 选择 Provider 并申请 Key**

| Provider | 特点 | 申请地址 | 费用 |
|----------|------|---------|------|
| MiniMax | 语音自然，支持多语言多音色 | https://www.minimax.io |
| 通义千问 TTS | 阿里云出品，稳定性高 | https://dash.console.aliyun.com |

**MiniMax 认证方式**：需要 `API_KEY` + `APP_ID` + `API_SECRET`

**通义千问认证方式**：需要 `API_KEY`（阿里云 DashScope API Key）

**Step 2 — 配置 .env 文件**

打开 `skills/.env`，设置：

```env
VOICE_PROVIDER=minimax
MINIMAX_API_KEY=
MINIMAX_APP_ID=
MINIMAX_API_SECRET=
```

或者：

```env
VOICE_PROVIDER=qwen
DASHSCOPE_API_KEY=
```

**Step 3 — 验证配置**

配置完成后，告诉我"配置好了"，Skill 会读取 `.env` 验证认证信息是否有效。

## 配音合成

配置完成后，直接告诉我你想合成什么内容：

- `/tts 你好，欢迎来到 Claude Code 插件市场`
- `/voice 今天的天气晴朗，适合外出游玩`

Skill 会根据你选择的 provider 调用对应 API，完成语音合成。

## Provider 调用方法

### MiniMax

**认证方式**：三方认证（API_KEY + APP_ID + API_SECRET）

**签名生成**（Python 示例）：
```python
import time, hashlib, base64, hmac

def generate_signature(api_secret: str, app_id: str) -> str:
    t = str(int(time.time()))
    sign_str = f"{app_id}{t}"
    signature = base64.b64encode(
        hmac.new(api_secret.encode(), sign_str.encode(), hashlib.sha1)
    ).decode()
    return t, signature

t, signature = generate_signature("你的API_SECRET", "你的APP_ID")
```

**API 端点**：`POST https://api.minimax.io/v1/t2a_v2`

**请求体**：
```json
{
  "model": "speech-02-hd",
  "text": "<要合成的文本>",
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

**Headers**：
```
Authorization: Bearer $MINIMAX_API_KEY
Content-Type: application/json
X-APP-ID: $MINIMAX_APP_ID
X-Timestamp: $签名时间戳
X-Signature: $生成的签名
```

**响应处理**：从响应中提取 `data` 字段的 Base64 音频数据，解码保存为 `.mp3` 文件。

---

### 通义千问 TTS（DashScope）

**API 端点**：`POST https://dashscope.aliyuncs.com/api/v1/services/aigc/text2audio/audio`

**请求体**：
```json
{
  "model": "cosyvoice-v1",
  "input": {
    "text": "<要合成的文本>"
  },
  "parameters": {
    "voice": "aixia",
    "response_format": "mp3",
    "sample_rate": 32000,
    "speed_ratio": 1.0,
    "pitch_ratio": 1.0,
    "volume_ratio": 1.0
  }
}
```

**Headers**：
```
Authorization: Bearer $DASHSCOPE_API_KEY
Content-Type: application/json
```

**响应处理**：响应为二进制音频流，直接保存为 `.mp3` 文件。

---

## 音色选择参考

### MiniMax 可用音色

| voice_id | 名称 | 适用场景 |
|----------|------|---------|
| male-qn-qingse | 青年男声-清冷 | 正式解说、旁白 |
| female-shaonv | 少女音 | 可爱、活泼风格 |
| male-tianmei | 甜妹音 | 温柔内容 |
| female-yunyang | 云扬男声 | 新闻、播报 |
| female-xiaowei | 晓伟男声 | 磁性低沉 |

### 通义千问可用音色

| voice | 名称 | 适用场景 |
|-------|------|---------|
| aixia | 阿霞 | 女声，温柔亲切 |
| zhishu | 知榆 | 女声，知性稳重 |
| male-qn-qingse | 青衫苦读 | 男声，书生感 |
| aiXiaoMo | 阿星 | 男声，沉稳有力 |

## 通用最佳实践

- **文本预处理**：TTS 对英文缩写（如 `AI`）和数字读法有时不稳定，建议预先转为自然文字（如 `"AI"` → `"人工智能"`，`"2024年"` → `"二零二四年"`）
- **分段合成**：单次合成文本建议控制在 500 字以内，过长文本建议分段合成后拼接
- **音频格式**：统一输出为 `.mp3`（兼容性最好），采样率 `32000Hz`
- **输出命名**：`voice_<timestamp>.mp3`
- **情绪标签**：部分 API 支持情绪参数（happy/sad/angry），可根据内容类型调整
