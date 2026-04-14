# Claude Code 插件市场 (Claude Marketplace)

> 为 Claude Code 提供一系列精选插件和可迁移的 AI 能力包，让 AI 助手更懂你。

## 项目概述

本仓库是一个 **Claude Code 插件和 Skill 集合**，包含两个平行部分：

- **Plugins（插件）** — 通过 Claude Code 插件机制集成的功能扩展
- **Skills（技能包）** — 封装了大模型 API 的调用方法，可迁移、可复用，让新 Agent 零成本继承调用能力

## 目录结构

```
claude-marketplace/
├── marketplace.json          # 插件市场索引文件
├── LICENSE                   # MIT 开源协议
├── README.md                 # 本文件
├── plugins/                  # 插件目录（功能扩展）
│   └── socratic-teach/      # 苏格拉底教学插件
│       ├── README.md
│       ├── .claude-plugin/
│       │   └── plugin.json
│       └── skills/
│           └── teach/
│               ├── SKILL.md
│               └── *.md       # 风格文件
└── skills/                   # 技能包目录（API 调用方法）
    ├── .env                  # API Key 存储（不提交 Git）
    ├── .env.example          # 环境变量模板
    ├── README.md             # Skills 使用指南
    ├── minimax_model_skill/  # MiniMax CodingPlan 全模态 Skill
    ├── video-generation/     # 视频生成 Skill
    └── voice-synthesis/      # 配音合成 Skill
```

## 插件列表

### socratic-teach

苏格拉底式教学插件 — 6 种风格人格，个性化适配，基于费曼技巧、ZPD 等教学理论。

👉 [查看详细文档](./socratic-teach/README.md)

## Skill 列表

👉 [查看 Skills 总览](./skills/README.md)

### minimax_model_skill — MiniMax CodingPlan

MiniMax 全模态 AI 能力包，覆盖文本、语音、视频、图像、音乐五大模态。

👉 [查看详细文档](./skills/minimax_model_skill/README.md)

### video-generation — 视频生成

封装 Runway / Pika / Kling 等主流视频生成 API 的调用方法。

👉 [查看详细文档](./skills/video-generation/README.md)

### voice-synthesis — 配音合成

封装 MiniMax / 通义千问 TTS 等语音合成 API 的调用方法。

👉 [查看详细文档](./skills/voice-synthesis/README.md)

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

参考上方 `plugins/` 目录结构，创建插件目录并编写 `plugin.json` 和 `SKILL.md`，然后更新 `marketplace.json`。

### 开发新 Skill

参考上方 `skills/` 目录结构，创建 Skill 目录并编写 `SKILL.md`（核心指令）和 `README.md`（使用文档）。每个 Skill 的 `SKILL.md` 开头需要包含环境检查逻辑，自动引导用户配置 API Key。

## 参与贡献

欢迎提交新插件、Skill 或改进现有内容！

- **提交新插件**：创建 `plugins/<name>/` 目录，参考现有插件结构
- **提交新 Skill**：创建 `skills/<name>/` 目录，参考 `video-generation` 的结构
- **反馈问题**：提交 GitHub Issue

## 开源协议

本项目基于 [MIT License](LICENSE) 开源。

## 更新日志

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
