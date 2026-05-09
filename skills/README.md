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
├── minimax_model_skill/       # MiniMax CodingPlan 全模态 Skill
│   ├── SKILL.md
│   └── README.md
├── video-generation/          # 视频生成 Skill
│   ├── SKILL.md
│   └── README.md
├── voice-synthesis/           # 配音合成 Skill
│   ├── SKILL.md
│   └── README.md
├── chinese-literary-enhancement/  # 中文文学素养增强
│   └── SKILL.md
├── historical-persona-agent/  # 历史人物对话控制器
│   └── SKILL.md
├── historical-persona-distiller/ # 历史人物蒸馏 Pipeline
│   ├── SKILL.md
│   └── README.md
├── problem-summarizer/      # 问题总结记录
│   ├── SKILL.md
│   └── README.md
└── commit-helper/           # Git Commit 规范生成
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

### minimax_model_skill — MiniMax CodingPlan（mmx CLI）

MiniMax 全模态 AI 能力包，通过 `mmx` CLI 统一调用语音合成、音色克隆、音乐生成、视频生成、图片生成等能力，只需一个 API Key。

👉 [查看详细文档](./minimax_model_skill/README.md)

### video-generation — 视频生成

支持 Runway、Pika、Kling 等主流视频生成模型。

👉 [查看详细文档](./video-generation/README.md)

### voice-synthesis — 配音合成

支持 MiniMax、通义千问等 TTS 模型。

👉 [查看详细文档](./voice-synthesis/README.md)

### chinese-literary-enhancement — 中文文学素养增强

让 AI 输出引经据典、妙语连珠，擅用成语、古诗词、名言、歇后语，使文风厚重而有韵。先联网搜索最贴切的素材，内置资源库作兜底。

👉 [查看详细文档](./chinese-literary-enhancement/SKILL.md)

### historical-persona-distiller — 历史人物蒸馏 Pipeline

自动蒸馏中国历史人物 persona 的 Pipeline，每日北京时间 06:00 自动执行。已完成 7 位人物（苏轼、杜甫、李白、辛弃疾、陶渊明、王维、白居易），共 25 人队列。

👉 [查看详细文档](./historical-persona-distiller/README.md)

### historical-persona-agent — 历史人物对话控制器

历史人物智能体系统的总入口。通过 slash 命令控制 persona 的加载、切换、关闭，并维护对话记忆。

👉 [查看详细文档](./historical-persona-agent/SKILL.md)

### problem-summarizer — 问题总结记录

将开发过程中遇到的问题和解决方案自动记录到固定文档，构建可检索的项目知识库。

👉 [查看详细文档](./problem-summarizer/README.md)

### commit-helper — Git Commit 规范生成

分析暂存区变更，自动生成符合 Conventional Commits 规范的 commit message。

👉 [查看详细文档](./commit-helper/README.md)

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
