# 历史人物 Persona 蒸馏流水线

## 项目目标

自动蒸馏中国历史人物的 persona，生成标准化 SKILL.md 文件，构建可被 AI 加载的历史人物人格库。

## 流水线架构

```
OpenClaw 定时触发（每日 06:00）
        ↓
读取 DONE.md「下一待处理」
        ↓
Stage 1: 资料采集       → raw/{人物名}/
Stage 2: 阶段切分       → processed/{人物名}/stages.md
Stage 3: 多维蒸馏        → processed/{人物名}/dimension_*.json
Stage 4: 卡片生成       → output/{人物名}/
        ↓
Git push → done/{人物名}.done → DONE.md 更新
```

## 目录结构

```
historical-persona-distiller/
├── RULES.md              ← OpenClaw 执行规则
├── README.md             ← 说明文档
├── DONE.md               ← 唯一状态入口（已完成记录 + 下一待处理）
├── backlog.md            ← 25 人完整队列（优先级 + 状态）
└── output/               ← 已生成 persona（自动创建）
    └── {人物名}/
        ├── SKILL.md           ← 核心 persona 文件
        ├── README.md           ← 使用说明
        ├── METADATA.json       ← 元数据
        ├── CITATIONS.md        ← 原文引用清单
        └── raw_stats.json      ← 原始数据统计

raw/                      ← 原始语料（自动创建）
processed/                 ← 中间处理结果（自动创建）
done/                      ← 完成标记（自动创建）
```

## 核心状态管理

**DONE.md 是唯一入口。** OpenClaw 每次读取 DONE.md 中的「下一待处理」确定当前人物，完成后更新 DONE.md 中的完成记录和统计。

## 调度配置

- **执行频率：** 每日北京时间 06:00
- **触发条件：** DONE.md 中「下一待处理」有有效条目
- **并发：** 单个人物串行

## 输出格式

所有人物统一输出 SKILL.md，详见 RULES.md Stage 5 模板。

## 质量控制

详见 RULES.md Section 七。核心规则：引用必须回溯原文、置信度强制标注、成语典故搜索验证。
