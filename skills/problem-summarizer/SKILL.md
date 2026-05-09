---
name: problem-summarizer
description: 问题总结记录 — 将开发过程中遇到的问题和解决方案自动记录到固定文档，构建可检索的知识库
type: skill
user-invocable: true
argument-hint: '[记录|查看|搜索 <关键词>]'
---

# 问题总结记录 Skill

将开发过程中遇到的问题和解决方案自动记录到固定文档，形成可检索的项目知识库。

---

## 环境检查（每次加载必执行）

1. 检查记录文档目录是否存在：`~/.claude/projects/<project-path>/memory/`
2. 若不存在，自动创建
3. 检查记录文档是否存在：`~/.claude/projects/<project-path>/memory/problem-log.md`
4. 若不存在，自动创建并写入初始结构

---

## 核心功能

### 1. 记录问题（默认触发）

当用户说"记录问题"、"总结问题"、"这个问题怎么解决的"时，执行：

1. 回顾当前对话中遇到的问题
2. 提取关键信息：问题描述、根因、解决方案、相关文件
3. 追加到 `problem-log.md`

**记录格式：**

```markdown
## [日期] 问题标题

**问题描述：** 一句话描述问题现象

**根因分析：** 问题的根本原因

**解决方案：** 具体的解决步骤

**相关文件：**
- `path/to/file.ts:123` — 相关代码位置

**标签：** #标签1 #标签2
```

### 2. 查看记录

当用户说"查看问题记录"、"问题列表"时：
- 读取 `problem-log.md`
- 按时间倒序展示所有记录

### 3. 搜索问题

当用户说"搜索问题 <关键词>"时：
- 在 `problem-log.md` 中搜索关键词
- 返回匹配的记录

---

## 记录原则

1. **只记录有价值的问题**：跳过简单的拼写错误、明显的语法问题
2. **突出根因和方案**：问题描述和解决方案必须具体可操作
3. **保留代码位置**：记录相关的文件路径和行号
4. **添加标签**：便于后续检索，如 `#API` `#配置` `#依赖` `#权限`

---

## 触发条件

**自动记录：**
- 用户明确说"记录这个问题"、"总结一下"
- 解决了一个非平凡的问题后，主动询问是否记录

**手动触发：**
- `/problem-log` — 查看所有记录
- `/problem-search <关键词>` — 搜索记录

---

## 文件位置

记录文档固定路径：
```
~/.claude/projects/<project-path>/memory/problem-log.md
```

其中 `<project-path>` 是项目根目录的路径，斜杠替换为连字符。

例如：`/Users/huang/Documents/github_project/claude-marketplace` →
`~/.claude/projects/-Users-huang-Documents-github-project-claude-marketplace/memory/problem-log.md`

---

## 文档结构

```markdown
# 问题解决记录

> 自动生成的知识库，记录开发过程中遇到的问题和解决方案。

---

## [2026-05-09] MCP 连接失败

**问题描述：** MiniMax MCP 工具调用返回超时错误

**根因分析：** 网络代理配置问题，MCP 服务器无法访问 MiniMax API

**解决方案：**
1. 检查代理设置：`echo $HTTP_PROXY`
2. 在 MCP 配置中添加代理环境变量
3. 重启 Claude Code

**相关文件：**
- `~/.claude/settings.json` — MCP 配置

**标签：** #MCP #网络 #配置

---
```
