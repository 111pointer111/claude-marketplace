# Historical Agent — 历史人物对话控制器

## 简介

历史人物智能体系统的总入口 Skill。通过 slash 命令加载、切换、关闭历史人物 persona，实现角色扮演式对话。

## 核心能力

- **风格对话**：以该人物的说话风格与人交流
- **生平感知**：引用真实人生事件，不虚构
- **时期切换**：同一个人物在不同时期可切换
- **记忆管理**：长期对话中保持身份一致性
- **语音提示**：提供 TTS 参数，心里有数

## 指令

| 指令 | 作用 |
|------|------|
| `/persona-on 苏轼` | 加载苏轼（默认中年巅峰期） |
| `/persona-on 苏轼 --stage 黄州` | 加载苏轼黄州时期 |
| `/persona-off` | 关闭对话 |
| `/persona-switch 李白` | 切换到李白 |
| `/persona-stage 黄州` | 切换到当前人物的黄州时期 |
| `/persona-status` | 查看当前状态 |
| `/persona-list` | 列出所有可用人物 |

## 依赖

- 依赖 Pipeline 蒸馏的人物 persona（`output/{persona_id}/SKILL.md`）
- 依赖 `persona_state.json`（状态文件）
- 依赖 `memory/`（对话记忆）

## 文件结构

```
skills/
└── historical-persona-agent/     ← 本 Skill
    ├── SKILL.md
    └── README.md

skills/historical-persona-distiller/
    ├── RULES.md                  # Pipeline 执行规则
    ├── EXECUTION_LOGIC.md        # Pipeline 执行逻辑
    ├── ARCHITECTURE.md           # 整体架构
    ├── DONE.md                   # Pipeline 完成记录
    ├── backlog.md                # 待处理人物队列
    ├── persona_state.json       # 当前状态
    ├── memory/                   # 对话记忆
    └── output/                   # Pipeline 输出（人物数据）
        └── {persona_id}/
            ├── SKILL.md          # 核心 persona
            ├── EVENTS.md         # 生平事件
            └── VOICE.md          # TTS 参数
```

## 交互流程

```
用户：/persona-on 苏轼
        ↓
读 persona_state.json（active=false）
        ↓
确认苏轼已完成蒸馏
        ↓
加载 su_shi/SKILL.md + EVENTS.md + VOICE.md
        ↓
生成 session_id，初始化 memory 文件
        ↓
确认开启，以苏轼身份开场
        ↓
用户与苏轼对话中……
        ↓
用户：/persona-switch 李白
        ↓
保存苏轼对话记忆 → Summary Compress
        ↓
加载李白 persona，新开 memory
        ↓
继续对话
        ↓
用户：/persona-off
        ↓
压缩保存对话，关闭状态
```

## 设计原则

- **状态驱动**：所有状态存于 `persona_state.json`，无魔法变量
- **记忆压缩**：每 5 轮自动压缩，AI 自行摘要，无长度限制
- **无侵入**：Pipeline 和 Agent 分离，Pipeline 只管蒸馏，Agent 只管对话
