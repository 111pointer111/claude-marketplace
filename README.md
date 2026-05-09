# Claude Code 插件市场 (Claude Marketplace)

> 为 Claude Code 提供一系列精选插件和可迁移的 AI 能力包，让 AI 助手更懂你。

## 项目概述

本仓库是一个 **Claude Code 插件和 Skill 集合**，包含两个平行部分：

- **Plugins（插件）** — 通过 Claude Code 插件机制集成的功能扩展
- **Skills（技能包）** — 封装了大模型 API 的调用方法，可迁移、可复用，让新 Agent 零成本继承调用能力

## 目录结构

```
claude-marketplace/
├── marketplace.json              # 插件市场索引文件
├── LICENSE                       # MIT 开源协议
├── README.md                     # 本文件
├── socratic-teach/               # 苏格拉底教学插件
│   ├── README.md
│   └── skills/
│       └── teach/                # 教学 Skill
│           ├── SKILL.md
│           └── *.md               # 风格文件
└── skills/                      # 技能包目录（AI 能力封装）
    ├── .env                      # API Key 存储（不提交 Git）
    ├── .env.example              # 环境变量模板
    ├── README.md                 # Skills 使用指南
    ├── minimax_model_skill/      # MiniMax CodingPlan 全模态 Skill
    ├── video-generation/          # 视频生成 Skill
    ├── voice-synthesis/          # 配音合成 Skill
    ├── chinese-literary-enhancement/  # 中文文学素养增强
    ├── historical-persona-agent/  # 历史人物对话控制器
    ├── historical-persona-distiller/ # 历史人物蒸馏 Pipeline
    ├── problem-summarizer/      # 问题总结记录
    └── commit-helper/           # Git Commit 规范生成
```

## 插件列表

### socratic-teach

苏格拉底式教学插件 — 6 种风格人格，个性化适配，基于费曼技巧、ZPD 等教学理论。

👉 [查看详细文档](./socratic-teach/README.md)

## Skill 列表

👉 [查看 Skills 总览](./skills/README.md)

### minimax_model_skill — MiniMax CodingPlan（mmx CLI）

MiniMax 全模态 AI 能力包，通过 `mmx` CLI 统一调用语音合成、音色克隆、音乐生成、视频生成、图片生成等能力。

👉 [查看详细文档](./skills/minimax_model_skill/README.md)

### video-generation — 视频生成

封装 Runway / Pika / Kling 等主流视频生成 API 的调用方法。

👉 [查看详细文档](./skills/video-generation/README.md)

### voice-synthesis — 配音合成

封装 MiniMax / 通义千问 TTS 等语音合成 API 的调用方法。

👉 [查看详细文档](./skills/voice-synthesis/README.md)

### chinese-literary-enhancement — 中文文学素养增强

让 AI 输出引经据典、妙语连珠，擅用成语、古诗词、名言、歇后语，使文风厚重而有韵。

👉 [查看详细文档](./skills/chinese-literary-enhancement/SKILL.md)

### historical-persona-distiller — 历史人物蒸馏 Pipeline

自动蒸馏中国历史人物的 persona，生成标准化 SKILL.md 文件，构建可被 AI 加载的历史人物人格库。每日北京时间 06:00 自动执行。

**已完成人物（7/25）：** 苏轼、杜甫、李白、辛弃疾、陶渊明、王维、白居易（均 high confidence）

**当前处理：** 李清照

👉 [查看详细文档](./skills/historical-persona-distiller/README.md)

### historical-persona-agent — 历史人物对话控制器

历史人物智能体系统的总入口。控制 persona 的加载、切换、关闭，以及对话历史的维护。支持 slash 命令：

- `/persona-on <人物>` — 开启对话
- `/persona-off` — 关闭对话
- `/persona-switch <人物>` — 切换人物
- `/persona-stage <时期>` — 切换时期切片
- `/persona-status` — 查看当前状态
- `/persona-list` — 查看可用人物列表

👉 [查看详细文档](./skills/historical-persona-agent/SKILL.md)

### problem-summarizer — 问题总结记录

将开发过程中遇到的问题和解决方案自动记录到固定文档，构建可检索的项目知识库。

👉 [查看详细文档](./skills/problem-summarizer/README.md)

### commit-helper — Git Commit 规范生成

分析暂存区变更，自动生成符合 Conventional Commits 规范的 commit message。

👉 [查看详细文档](./skills/commit-helper/README.md)

## 安装插件市场

```bash
/plugin marketplace add https://github.com/111pointer111/claude-marketplace
```

更新所有插件：

```bash
/plugin marketplace update
```

## 开发指南

### 开发新插件

参考上方 `socratic-teach/` 目录结构，创建插件目录并编写 `plugin.json` 和 `SKILL.md`，然后更新 `marketplace.json`。

### 开发新 Skill

参考上方 `skills/` 目录结构，创建 Skill 目录并编写 `SKILL.md`（核心指令）和 `README.md`（使用文档）。每个 Skill 的 `SKILL.md` 开头需要包含环境检查逻辑，自动引导用户配置 API Key。

## 参与贡献

欢迎提交新插件、Skill 或改进现有内容！

- **提交新插件**：创建 `<name>/` 目录，参考 `socratic-teach/` 的结构
- **提交新 Skill**：创建 `skills/<name>/` 目录，参考 `chinese-literary-enhancement/` 的结构
- **反馈问题**：提交 GitHub Issue

## 开源协议

本项目基于 [MIT License](LICENSE) 开源。

## 更新日志

### v1.4.0

- 重构 `minimax_model_skill`，从 MCP 改为 mmx CLI 调用
- 新增 `problem-summarizer`，问题总结记录 Skill
- 新增 `commit-helper`，Git Commit 规范生成 Skill

### v1.3.0

- 新增 `chinese-literary-enhancement`，中文文学素养增强 Skill
- 新增 `historical-persona-distiller`，历史人物蒸馏 Pipeline（已完成 7 位人物）
- 新增 `historical-persona-agent`，历史人物对话控制器，支持 6 种 slash 命令

### v1.2.0
- 新增 `minimax_model_skill`，覆盖 MiniMax CodingPlan 全模态模型（文本/TTS/视频/图像/音乐）
- 更新 `.env.example`，新增 MiniMax 相关环境变量

### v1.1.0
- 新增 `skills/` 目录及 Skills 框架
- 上线 `video-generation` 视频生成 Skill（支持 Runway / Pika / Kling）
- 上线 `voice-synthesis` 配音合成 Skill（支持 MiniMax / 通义千问）
- 所有 Skill 统一使用 `skills/.env` 管理 API Key

### v1.0.0
- 发布初始版本
- 上线 `socratic-teach` 苏格拉底教学插件
- 支持 6 种教学风格（御姐、暴躁、学姐、教师、闺蜜、直男）
