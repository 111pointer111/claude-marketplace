# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个 **Claude Code 插件市场**，全部内容均为 Markdown — 无构建工具、无测试、无包管理器、无运行时代码。

**权威文档分工：**
- `AGENTS.md` — 内容约定、添加新插件/Skill 的标准流程、特殊格式说明
- `README.md` — 完整的插件和 Skill 清单 + 版本日志
- `marketplace.json` — 插件市场的根索引（添加新插件时同步更新）

## 架构

仓库根目录两个平行内容区：

- **Plugins（插件）** — 直接放在仓库根（例如 `socratic-teach/`）。**不要**创建 `plugins/` 顶层目录。每个插件独立目录，包含：
  - `.claude-plugin/plugin.json` — 插件元信息
  - `skills/<name>/SKILL.md` — 核心技能逻辑
  - `skills/<name>/*.md` — 人格/风格文件，仅影响语气措辞

- **Skills（技能包）** — 放在 `skills/` 下。每个 Skill 独立目录，包含：
  - `SKILL.md` — frontmatter 元数据 + 环境检查 + 核心逻辑
  - `README.md` — 使用文档

完整 Skill/插件清单见 `README.md`。

### Skill 的两种格式（并存）

- **标准格式（推荐）**：`skills/*/SKILL.md`，YAML frontmatter + 环境检查前置 + Markdown 逻辑。**新 Skill 统一用此格式。**
- **清单格式**（仅 `skills/flutter-ios-code-review/`）：`manifest.json` + 小写 `skill.md`，无 frontmatter。这是历史遗留，新内容不要再用此格式。

### SKILL.md frontmatter 规范

```markdown
---
name: <skill-name>
description: <描述>
type: skill
user-invocable: true
argument-hint: '[<参数提示>]'
---
```

**所有 SKILL.md 必须以环境检查开头**，从 `skills/.env` 读取所需 API Key，并在缺失时引导用户配置。

### 环境变量
所有 API Key 集中在 `skills/.env` 管理（已 gitignore）。从 `skills/.env.example` 复制。每个 SKILL.md 自行处理缺失 key 的引导流程。

### 学生画像（仅 socratic-teach）
teach skill 读写学生画像到硬编码路径：
- `~/.claude/projects/-Users-huang-Documents-use-claude-study/memory/student-profile.md`
- `~/.claude/projects/-Users-huang-Documents-use-claude-study/memory/teaching-persona.md`

## 关键非显然规则

- **historical-persona-distiller 输出**：`skills/historical-persona-distiller/output/` 包含 ~90+ 自动生成的 persona SKILL.md。这些是 pipeline 输出，**不要手工编辑**；如需修正请改 distiller skill 自身（`skills/historical-persona-distiller/`）。
- **mmx CLI 例外**：`minimax_model_skill` 通过全局 `mmx` CLI 调用（`npm install -g mmx-cli`），不走 MCP。
- **本仓库无 lint / typecheck / test**——纯内容仓库。改动靠 PR review 与 Markdown 语法正确性保障质量。

## MCP 权限

`.claude/settings.local.json` 已允许 `mcp__MiniMax__web_search` 和 `mcp__MiniMax__understand_image`，并禁用 `supabase` 和 `playwright`。

## 添加新插件

1. 在仓库根创建 `<name>/.claude-plugin/plugin.json`
2. 创建 `<name>/skills/<skill-name>/SKILL.md`
3. 在 `marketplace.json` 的 `plugins` 数组中添加条目

## 添加新 Skill

1. 创建 `skills/<name>/SKILL.md`（含 frontmatter + 环境检查）
2. 创建 `skills/<name>/README.md`
3. 如需 API Key，在 `skills/.env.example` 中添加对应变量
