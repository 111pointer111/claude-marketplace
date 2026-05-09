# Git Commit 规范生成 Skill

分析暂存区变更，自动生成符合 Conventional Commits 规范的 commit message。

## 功能

- **分析变更**：自动读取 `git diff --cached`，理解改动内容
- **生成 message**：按 Conventional Commits 规范生成 commit message
- **智能判断**：自动识别 feat / fix / docs / refactor 等类型
- **风格适配**：根据项目现有 commit 风格自动调整

## 使用方式

直接告诉 Agent：

- `提交` / `commit` — 生成 commit message 并提交
- `查看变更` — 查看当前 git 状态
- `生成 commit message` — 只生成 message，不执行 commit

## Commit 格式

```
<type>(<scope>): <subject>

<body>

<footer>
```

## 项目结构

```
commit-helper/
├── SKILL.md      # 核心指令文件
└── README.md     # 本文件
```
