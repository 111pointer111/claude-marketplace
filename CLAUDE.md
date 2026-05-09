# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个 **Claude Code 插件市场**，包含两个并行部分：

- **Plugins（插件，`plugins/`）** — 通过 Claude Code 插件机制集成的功能扩展
- **Skills（技能包，`skills/`）** — 封装 LLM API 调用方法的知识沉淀

项目没有构建工具、没有测试、没有包管理器——全部基于 Markdown 文件。

## 架构

### 市场索引
`marketplace.json` — 整个插件市场的根索引。添加新插件需更新此文件。

### 插件（`plugins/`）
每个插件独立目录，包含：
- `.claude-plugin/plugin.json` — 插件元信息（名称、版本、skills 路径、关键词）
- `skills/<name>/SKILL.md` — 插件的核心技能逻辑
- `skills/<name>/*.md` — 人格/风格文件，仅影响语气措辞，不改变逻辑

**当前插件：** `socratic-teach/` — 苏格拉底式教学插件，6 种人格风格。SKILL.md 定义所有教学规则；风格文件只定义说话语气。

### 技能包（`skills/`）
每个 Skill 目录包含：
- `SKILL.md` — frontmatter 元数据 + 环境检查 + 核心逻辑。**所有 SKILL.md 必须以环境检查开头，从 `skills/.env` 读取 API Key**
- `README.md` — 使用文档

SKILL.md frontmatter 格式：
```markdown
---
name: <skill-name>
description: <描述>
type: skill
user-invocable: true
argument-hint: '[<参数提示>]'
---
```

**当前 Skills：**
- `minimax_model_skill/` — MiniMax 全模态，通过 mmx CLI 统一调用
- `video-generation/` — 视频生成，支持 Runway / Pika / Kling
- `voice-synthesis/` — 配音合成，支持 MiniMax / 通义千问
- `problem-summarizer/` — 问题总结记录，自动记录问题和解决方案
- `commit-helper/` — Git Commit 规范生成，自动生成 Conventional Commits 格式

### 环境变量
所有 API Key 集中在 `skills/.env` 管理（已 gitignore）。从 `skills/.env.example` 复制。每个 SKILL.md 自行处理缺失 key 的引导流程。

### 学生画像（仅 socratic-teach）
teach skill 读写学生画像到硬编码路径：
- `~/.claude/projects/-Users-huang-Documents-use-claude-study/memory/student-profile.md`
- `~/.claude/projects/-Users-huang-Documents-use-claude-study/memory/teaching-persona.md`

## 添加新插件

1. 创建 `plugins/<name>/.claude-plugin/plugin.json`
2. 创建 `plugins/<name>/skills/<skill-name>/SKILL.md`
3. 在 `marketplace.json` 中添加条目

## 添加新 Skill

1. 创建 `skills/<name>/SKILL.md`（含 frontmatter + 环境检查）
2. 创建 `skills/<name>/README.md`
3. 如需 API Key，在 `skills/.env.example` 中添加对应变量
