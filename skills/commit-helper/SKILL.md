---
name: commit-helper
description: Git Commit 规范生成 — 分析暂存区变更，自动生成符合 Conventional Commits 规范的 commit message
type: skill
user-invocable: true
argument-hint: '[提交|生成 commit message|查看变更]'
---

# Git Commit 规范生成 Skill

分析暂存区变更，自动生成符合 Conventional Commits 规范的 commit message。

---

## 核心流程

当用户说"提交"、"commit"、"生成 commit message"时，执行以下步骤：

### 1. 检查变更状态

```bash
git status
git diff --cached --stat
git diff --cached
```

### 2. 分析变更内容

根据 diff 内容判断：
- **变更类型**：feat / fix / docs / style / refactor / perf / test / chore / build / ci
- **影响范围**：涉及的模块、组件、功能
- **变更摘要**：一句话描述核心改动

### 3. 生成 Commit Message

**格式（Conventional Commits）：**

```
<type>(<scope>): <subject>

<body>

<footer>
```

**type 类型：**

| type | 说明 | 示例 |
|------|------|------|
| `feat` | 新功能 | `feat(auth): 添加微信登录` |
| `fix` | 修复 bug | `fix(api): 修复用户列表分页错误` |
| `docs` | 文档更新 | `docs: 更新 README 安装说明` |
| `style` | 代码格式（不影响逻辑） | `style: 统一缩进为 2 空格` |
| `refactor` | 重构（非新功能非修复） | `refactor(utils): 提取日期格式化函数` |
| `perf` | 性能优化 | `perf: 优化图片懒加载` |
| `test` | 测试相关 | `test: 添加用户模块单元测试` |
| `chore` | 构建/工具/依赖 | `chore: 升级 webpack 到 v5` |
| `build` | 构建系统变更 | `build: 迁移到 Vite` |
| `ci` | CI 配置变更 | `ci: 添加 GitHub Actions` |

**scope 规则：**
- 可选，表示影响范围
- 通常对应模块名、组件名、目录名
- 小写，多个词用连字符

**subject 规则：**
- 使用中文或英文，保持项目一致性
- 不超过 50 个字符
- 不以句号结尾
- 使用祈使语气（"添加" 而非 "添加了"）

### 4. 确认并执行

向用户展示生成的 commit message，确认后执行：

```bash
git commit -m "<type>(<scope>): <subject>" -m "<body>" -m "<footer>"
```

---

## 快捷命令

| 命令 | 功能 |
|------|------|
| `提交` / `commit` | 生成 commit message 并提交 |
| `查看变更` / `git status` | 查看当前变更状态 |
| `生成 commit message` | 只生成 message，不执行 commit |

---

## 示例

### 示例 1：新功能

```bash
# 用户：提交
# Agent 分析 diff 后生成：
git commit -m "feat(auth): 添加 JWT 认证中间件" -m "- 实现 token 验证逻辑
- 添加 refresh token 机制
- 处理 token 过期场景"
```

### 示例 2：Bug 修复

```bash
# 用户：提交
# Agent 分析 diff 后生成：
git commit -m "fix(api): 修复用户列表空指针异常" -m "当 users 数组为空时，map 操作抛出异常。
添加空数组检查，返回空列表而非报错。"
```

### 示例 3：文档更新

```bash
# 用户：提交
# Agent 分析 diff 后生成：
git commit -m "docs: 更新 AGENTS.md 添加 minimax CLI 说明"
```

---

## 特殊情况处理

### 多个不相关的变更

如果暂存区包含多个不相关的变更，建议拆分为多次提交：

```
检测到多个不相关的变更，建议拆分提交：
1. feat(auth): 添加登录功能
2. docs: 更新 API 文档
3. fix: 修复配置文件读取错误

是否拆分提交？还是合并为一次提交？
```

### 无暂存文件

如果没有文件在暂存区，提示用户先 `git add`：

```
暂存区为空，请先添加要提交的文件：
git add <file>
或添加所有变更：
git add .
```

---

## 风格适配

- 如果项目已有 commit 历史，分析现有风格并保持一致
- 中文项目优先使用中文 commit message
- 英文项目使用英文 commit message
- 支持 emoji 前缀（如果项目已有此惯例）：`✨ feat: ...`、`🐛 fix: ...`
