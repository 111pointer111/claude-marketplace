# 历史人物 Persona 蒸馏流水线

## 项目目标

自动蒸馏中国历史人物的 persona，生成标准化 SKILL.md 文件，构建可被 AI 加载的历史人物人格库。

## 流水线架构

```
queue/daily.md          ← 每日任务队列
       ↓
Stage 1: 资料采集       → raw/{人物名}/
Stage 2: 阶段切分       → processed/{人物名}/stages.md
Stage 3: 多维蒸馏        → processed/{人物名}/dimension_*.json
Stage 4: 卡片生成       → output/{人物名}/
       ↓
GitHub push            → skills/{人物名}/SKILL.md
```

## 目录结构

```
skills/historical-persona-distiller/
├── RULES.md            ← OpenClaw 执行规则（本文件）
├── README.md           ← 说明文档
├── queue/              ← 任务队列
│   ├── daily.md         ← 今日任务（每日更新）
│   └── backlog.md       ← 待处理人物列表
└── output/             ← 已生成 persona（自动创建）
    └── {人物名}/
        ├── SKILL.md
        ├── README.md
        ├── METADATA.json
        ├── CITATIONS.md
        └── raw_stats.json

raw/                    ← 原始语料（自动创建）
processed/               ← 中间处理结果（自动创建）
done/                    ← 已完成标记（自动创建）
```

## 调度配置

- **执行频率：** 每日北京时间 06:00
- **触发条件：** queue/daily.md 存在且人物未在 done/ 中
- **并发：** 单个人物串行执行

## 输出格式

所有人物统一输出 SKILL.md，格式见 RULES.md Stage 5 模板。

## 人物队列

详见 RULES.md Section 六。执行顺序按 priority 从高到低。

## 质量控制

详见 RULES.md Section 三。执行前强制检查引用回溯、confidence 评级、成语典故准确性。
