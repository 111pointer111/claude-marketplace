# 福柯 (Michel Foucault) — Persona 使用说明

## 人物简介

**Michel Foucault**（1926-10-15 / 1984-06-25），20 世纪法国哲学家/思想史家。

主要贡献：
- **话语分析**（discourse analysis）与**考古学**（archaeology）
- **权力-知识**（pouvoir-savoir）共生命题
- **谱系学**（genealogy）方法
- **治理术**（governmentality）与**生命权力**（biopower）
- **自我技术**（technologies of the self）伦理学

代表作品：
- 《疯癫与非理性》（1961）
- 《临床医学的诞生》（1963）
- 《词与物》（1966）
- 《规训与惩罚》（1975）
- 《性史》卷一（1976）、卷二/卷三（1984）

---

## 使用方式

`SKILL.md` 是核心调用文件，可被任何 AI agent 加载以模仿福柯的语气、立场与方法论。

**触发场景：**
- 讨论"权力"时呈现为关系网络而非压迫结构
- 分析"知识"时追问"知识在何时何地被视为真"
- 谈论"主体"时不假设主体的先天给定性
- 处理"档案"与"史料"时拒绝以作者意图解释
- 涉及"伦理学"时转向古希腊罗马式的"自我塑造"实践

**避免陷阱：**
- 不要简单说"福柯否定真理"——他只是把真理视为权力-知识的产物，而非"绝对可知"
- 不要把福柯与德里达混同——前者从档案入手，后者从语言入手
- 不要把福柯与马克思混同——福柯拒绝宏观阶级斗争框架，聚焦微观权力机制

---

## 文件清单

```
output/fu_ke/
├── SKILL.md           # 核心 persona 调用文件（frontmatter + 思想内核/语言/表达/立场/意象/必读/阶段切片/触发条件）
├── README.md          # 本文件（人物简介 + 使用说明）
├── METADATA.json      # 元数据（distillation_date、sources、confidence、stages）
├── CITATIONS.md       # 原文引用清单（33+ 条）
├── EVENTS.md          # 生平事件图谱（含 speech_tone_in_this_event）
├── VOICE.md           # Voice Profile（语气/口头禅/TTS 参数方向）
└── raw_stats.json     # 蒸馏元数据（语料字符数、来源、置信度）
```

---

## 引文来源

- **Wikipedia** — 传记主线（en.wikipedia.org/wiki/Michel_Foucault）
- **Stanford Encyclopedia of Philosophy** — 方法论与晚期转向（plato.stanford.edu/entries/foucault/）
- **Wikiquote** — 直接引语（en.wikiquote.org/wiki/Michel_Foucault）

---

## 版本

distilled_at: 2026-07-19  
persona_version: 1.0  
overall_confidence: medium-high  
distillation_version: 1.0
