# Claude Code 插件市场 (Claude Marketplace)

> 为 Claude Code 提供一系列精选插件，涵盖教学、开发效率等多个场景，让 AI 助手更懂你。

## 项目概述

本仓库是一个 **Claude Code 插件集合**，旨在为 Claude Code 用户提供开箱即用的高质量插件。

随着 Claude Code 的生态发展，越来越多的场景可以通过插件来增强 AI 的能力。本项目将持续收录各类实用插件，你可以在此找到适合自己工作流的工具，并轻松一键安装。

### 核心特性

- **插件化架构**：每个插件独立目录，通过 Claude Code 的插件机制无缝集成
- **即装即用**：一行命令完成安装，无需复杂配置
- **持续更新**：插件库将不断扩充，覆盖更多使用场景
- **社区共建**：欢迎提交 PR，一起完善插件生态

## 目录结构

```
claude-marketplace/
├── marketplace.json          # 插件市场索引文件（声明所有插件）
├── LICENSE                   # MIT 开源协议
├── README.md                 # 本文件
└── <plugin-name>/            # 插件目录（每个插件独立）
    ├── README.md             # 该插件的使用文档
    ├── .claude-plugin/
    │   └── plugin.json       # 插件元信息
    └── skills/               # 插件包含的技能
        └── <skill-name>/
            ├── SKILL.md      # 技能定义文件
            └── *.md          # 风格/配置相关文件
```

## 插件列表

### socratic-teach

苏格拉底式教学插件 — 6 种风格人格，个性化适配，基于费曼技巧、ZPD 等教学理论。

👉 [查看详细文档](./socratic-teach/README.md)

## 安装插件市场

将整个插件市场添加到你的 Claude Code 中：

```bash
/plugin marketplace add https://github.com/111pointer111/claude-marketplace
```

更新所有插件：

```bash
/plugin marketplace update
```

## 插件开发指南

如果你想为 Claude Code 开发新插件，可以参考以下流程：

### 1. 创建插件目录

在仓库根目录下创建新的插件文件夹：

```
/your-plugin/
    ├── README.md              # 必选，插件使用文档
    ├── .claude-plugin/
    │   └── plugin.json        # 必选，插件元信息
    └── skills/
        └── <your-skill>/
            └── SKILL.md      # 必选，技能定义
```

### 2. 编写 plugin.json

```json
{
  "name": "your-plugin-name",
  "description": "插件描述",
  "version": "1.0.0",
  "license": "MIT",
  "keywords": ["keyword1", "keyword2"],
  "skills": ["./skills/"]
}
```

### 3. 编写插件 README.md

在插件目录下创建 `README.md`，详细介绍该插件的功能、安装方式、使用方法等。README 的内容以这个文件为主页入口，具体文档放在对应插件目录下。

### 4. 更新 marketplace.json

在 `plugins` 数组中添加新插件的条目：

```json
{
  "name": "your-plugin-name",
  "description": "插件描述",
  "source": "./your-plugin",
  "category": "education",
  "homepage": "https://github.com/111pointer111/claude-marketplace"
}
```

### 5. 提交并推送

```bash
git add .
git commit -m "feat: add your-plugin-name plugin"
git push
```

## 参与贡献

欢迎为仓库提交插件或改进现有功能！

- **提交新插件**：按照上方"插件开发指南"创建新插件，提交 PR
- **改进现有插件**：直接在对应目录下修改，提交 PR
- **反馈问题**：提交 GitHub Issue

## 开源协议

本项目基于 [MIT License](LICENSE) 开源。

## 更新日志

### v1.0.0
- 发布初始版本
- 上线 `socratic-teach` 苏格拉底教学插件
- 支持 6 种教学风格（御姐、暴躁、学姐、教师、闺蜜、直男）
