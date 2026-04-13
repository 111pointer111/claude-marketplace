# voice-synthesis — 配音合成 Skill

封装了 MiniMax、通义千问 TTS 等语音合成 API 的完整调用方法。

## 安装

Skill 文件在 `skills/voice-synthesis/SKILL.md`，Claude Code 加载后直接可用。

## 快速开始

### 1. 配置 API Key

```bash
# 复制模板
cp skills/.env.example skills/.env

# 编辑 skills/.env，设置 VOICE_PROVIDER 和对应认证信息
# 例如（MiniMax）：
# VOICE_PROVIDER=minimax
# MINIMAX_API_KEY=xxx
# MINIMAX_APP_ID=xxx
# MINIMAX_API_SECRET=xxx
```

支持同时配置多个 provider 的认证信息，切换时只需修改 `VOICE_PROVIDER` 即可。

### 2. 开始合成

配置好认证信息后，直接告诉我你想合成什么：

```bash
/voice 你好，欢迎使用 Claude Code 插件市场
/tts 今天的天气晴朗，适合外出游玩
```

## 支持的 Provider

| Provider | 认证方式 | 特点 | 费用 |
|----------|---------|------|------|
| MiniMax | API_KEY + APP_ID + API_SECRET | 多音色，情绪控制，语音自然 | 付费 |
| 通义千问 TTS | DashScope API Key | 阿里云，稳定可靠 | 付费（有免费额度） |

## 常用场景

### 旁白配音
将文案转为自然语音，用于视频配音、播客、有声书等。

### 多语言配音
支持中英文混合配音，部分 provider 支持多语言切换。

### 情感语音
选择带有情绪标签的音色（如 happy、sad），让语音更有表现力。

## 项目结构

```
voice-synthesis/
├── SKILL.md      # 核心指令文件（API 调用逻辑）
└── README.md     # 本文件
```
