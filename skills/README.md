# Skills — 可迁移的 AI 能力包

> 封装了大模型 API 的调用方法，让 AI Agent 零成本继承调用能力。

## 定位

`skills/` 目录存放的是**可迁移的 AI 能力包**。每个 Skill 记录了调用某个大模型 API 的完整方法——包括调用格式、参数说明、错误处理、最佳实践。

与插件不同，Skill 更偏向"知识沉淀"而非"功能扩展"。它的核心价值是：**你踩过的坑、调通过的 API，写成 Skill 后，下次换一个 Agent 也能直接用**。

## 目录结构

```
skills/
├── .env                       # API Key 存储文件（不提交到 Git）
├── .env.example               # 环境变量模板
├── README.md                  # 本文件
├── minimax/                   # MiniMax CodingPlan 全模态 Skill
│   ├── SKILL.md
│   └── README.md
├── video-generation/          # 视频生成 Skill
│   ├── SKILL.md
│   └── README.md
└── voice-synthesis/           # 配音合成 Skill
    ├── SKILL.md
    └── README.md
```

## 环境变量配置

所有 Skill 的 API Key 集中管理在 `skills/.env` 文件中。

### 首次配置

1. 复制 `.env.example` 为 `.env`：
   ```bash
   cp skills/.env.example skills/.env
   ```
2. 打开 `skills/.env`，填入你拥有的 API Key
3. 不确定用哪个 provider？直接填多个也无所谓，Skill 会根据你选择的 provider 自动读取对应 key

**注意：`.env` 文件在 `.gitignore` 中，不会提交到 Git。**

### 配置流程

当 Skill 检测到缺少必要的 API Key 时，会自动引导你完成配置：

1. 提示你前往对应平台申请 API Key
2. 引导你编辑 `skills/.env` 填入 key
3. 读取验证配置成功后执行任务

## Skill 列表

### minimax — MiniMax CodingPlan

MiniMax 全模态 AI 能力包，涵盖文本、语音、视频、图像、音乐五大模态。

👉 [查看详细文档](./minimax/README.md)

### video-generation — 视频生成

支持 Runway、Pika、Kling 等主流视频生成模型。

👉 [查看详细文档](./video-generation/README.md)

### voice-synthesis — 配音合成

支持 MiniMax、通义千问等 TTS 模型。

👉 [查看详细文档](./voice-synthesis/README.md)

## 开发新 Skill

参考以下模板创建新 Skill：

```
skills/<your-skill>/
├── SKILL.md      # frontmatter + 环境检查 + 核心逻辑
└── README.md     # 使用文档
```

SKILL.md 开头 frontmatter 参考：

```markdown
---
name: your-skill
description: 描述
type: skill
user-invocable: true
argument-hint: '[参数提示]'
---

# 技能名称

## 环境检查

1. 读取 `skills/.env` 中的环境变量
2. 缺少 key 时引导用户配置
3. 配置完成后继续执行
```
