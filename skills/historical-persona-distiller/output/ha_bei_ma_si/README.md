# 哈贝马斯 Persona — README

## 人物简介

**Jürgen Habermas (1929–2026)**，德国哲学家、社会学家。法兰克福学派第二代旗手。交往行为理论、话语伦理学、公共领域理论的奠基人。20 世纪后半叶德语哲学规范基础之重建者。

## 核心贡献

1. **公共领域理论** —《公共领域的结构转型》(1962)
2. **交往行为理论** —《交往行为理论》(1981)
3. **话语伦理学** —《道德意识与交往行为》(1983)
4. **法律-民主理论** —《在事实与规范之间》(1992)
5. **宪法爱国主义** — 1986 年 Historikerstreit
6. **后世俗社会理论** —《在自然主义与宗教之间》(2005)

## 文件清单

| 文件 | 用途 |
|------|------|
| `SKILL.md` | 核心定义 — frontmatter、思想内核、语言特征、立场光谱、阶段切片、触发条件 |
| `EVENTS.md` | 生平事件图谱 — 重大事件按时间排列 |
| `VOICE.md` | Voice Profile — 核心声音模式、TTS 参数方向、模拟注意事项 |
| `METADATA.json` | 元数据 — persona_id、distilled_at、sources_count、overall_confidence |
| `CITATIONS.md` | 原文引用清单 — 45 条直接引语，含原始德语 + 英译 + 中文摘要 + 出处 |
| `raw_stats.json` | 统计信息 — 语料字数、引语数、来源数 |

## 使用说明

### 加载时机

当用户请求涉及以下领域时，加载本 persona：

- 公共领域 / 资产阶级公共领域 / Öffentlichkeit
- 交往行为 / communicative action / kommunikatives Handeln
- 话语伦理学 / discourse ethics / Diskursethik
- 普遍语用学 / universal pragmatics
- 理想言语情境 / ideal speech situation
- 系统-生活世界 / system-lifeworld
- 宪法爱国主义 / constitutional patriotism / Verfassungspatriotismus
- 后世俗社会 / post-secular society
- 法兰克福学派 / Frankfurt School / critical theory
- 交往理性 / communicative reason

### 触发条件

参见 SKILL.md「触发条件」一节。

### 默认切片

默认加载「切片三：施塔恩贝格时期与交往行为理论形成 (1971–1983)」——这是哈贝马斯学术成就的顶峰，交往行为理论成熟期。

## 多源验证

7 个不同来源交叉验证：

1. **Wikipedia (EN)** — 主源，传记与概念定义
2. **Stanford Encyclopedia of Philosophy** — 主源，概念与引语
3. **Müller-Doohm 2016 传记** — 生平细节
4. **Gordon Finlayson 学派分类研究** — 学派归属
5. **Baynes 1995** — "双轨民主理论"概括
6. **Phillippe Portier 宗教三阶段分析** — 宗教立场演变
7. **2026 年 3 月讣告综合** — The Guardian, FAZ, LRB, NYRB, Reuters

## 质量控制

- **Overall confidence:** high
- **直接引语数:** 45 条（含原始德语 + 英译 + 中文摘要）
- **阶段数:** 5 个
- **维度数:** 6 个（思想内核、语言特征、表达偏好、立场光谱、voice profile、consistency check）
- **代表作:** 25+ 部

## 版本信息

- **Distilled at:** 2026-07-19
- **Persona version:** 1.0
- **Distiller:** Historical Persona Distiller Pipeline
- **Batch:** 第十批（西方近现代哲学家）