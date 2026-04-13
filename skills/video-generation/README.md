# video-generation — 视频生成 Skill

封装了 Runway、Pika、Kling 等主流视频生成 API 的完整调用方法。

## 安装

Skill 文件在 `skills/video-generation/SKILL.md`，Claude Code 加载后直接可用。

## 快速开始

### 1. 配置 API Key

```bash
# 复制模板
cp skills/.env.example skills/.env

# 编辑 skills/.env，设置 VIDEO_PROVIDER 和对应 API Key
# 例如：
# VIDEO_PROVIDER=runway
# RUNWAY_API_KEY=sk-xxx
```

支持同时配置多个 provider 的 key，切换时只需修改 `VIDEO_PROVIDER` 即可。

### 2. 开始生成

配置好 key 后，直接描述你想生成的视频：

```bash
/video 一个人在海边跑步，日落背景
/video 赛博朋克风格的城市夜景，未来感
```

## 支持的 Provider

| Provider | 模型 | 特点 | 费用 |
|----------|------|------|------|
| Runway | gen3a_turbo | 质量高，效果逼真 | 付费 |
| Pika | pika-v1 | 动画风格，速度快 | 付费 |
| Kling | kling-v1 | 国产首选，性价比高 | 付费 |

## 常用场景

### 文生视频
直接用文字描述场景和动作，API 会生成对应的视频片段。

### 图生视频
将一张静态图片作为首帧，让它"动起来"。调用时在 prompt 中注明"基于图片"并附上图片路径。

## 项目结构

```
video-generation/
├── SKILL.md      # 核心指令文件（API 调用逻辑）
└── README.md     # 本文件
```
