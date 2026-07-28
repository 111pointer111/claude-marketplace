# 麦克斯韦 (James Clerk Maxwell) — Persona 使用说明

> 本目录包含历史人物 persona 蒸馏的全部产物。SKILL.md 是主要调用文件，其余文件提供元数据、引用清单、事件、声音特征等支撑信息。

## 文件清单

| 文件 | 用途 |
|------|------|
| `SKILL.md` | 主调用文件——包含 persona 核心、阶段切片、触发条件 |
| `README.md` | 本文件——使用说明 + 人物简介 |
| `METADATA.json` | 元数据（朝代、寿命、来源数、置信度等） |
| `CITATIONS.md` | 所有原文引用清单（含出处与年份） |
| `EVENTS.md` | 生平大事年表 |
| `VOICE.md` | 声音特征（口音、语气、节奏） |
| `raw_stats.json` | 蒸馏元数据（词数、来源数、切片数等） |

## 人物简介

**James Clerk Maxwell (1831-1879)** 是苏格兰物理学家和数学家，19 世纪最伟大的理论物理学家之一，被誉为"在牛顿和爱因斯坦之间的桥梁"。

### 主要贡献

1. **麦克斯韦方程组（Maxwell's Equations）**：1861-1865 年发展，1865 年发表"A Dynamical Theory of the Electromagnetic Field"，用 20 个方程（20 个未知数）统一了电、磁、光。后来 Oliver Heaviside 简化为现代形式的四个方程。预言电磁波以光速传播——这是物理学史上最大的统一性成就之一。

2. **麦克斯韦-玻尔兹曼分布（Maxwell-Boltzmann Distribution）**：气体动理论的核心成果，描述气体分子速度的统计分布。

3. **麦克斯韦妖（Maxwell's Demon）**：1867 年提出的思想实验，预示了信息论、控制论、混沌理论的发展。

4. **首张耐久彩色照片**：1861 年在 Royal Institution 演讲中演示（tartan ribbon）。

5. **色彩视觉理论**：1855-1865 年发展色彩三角（color triangle），是色视觉定量化的先驱。

6. **控制工程理论基础**：1868 年"On governors"论文，奠定了反馈控制理论。

7. **土星环稳定性研究**：1859 年以"On the Stability of the Motion of Saturn's Rings"赢得 Adams Prize。

### 学术生涯

- **Marischal College Aberdeen** (1856-1860) — 自然哲学讲座教授
- **King's College London** (1860-1865) — 自然哲学讲座教授
- **Glenlair** (1865-1871) — 退隐写作
- **Cavendish Laboratory Cambridge** (1871-1879) — 首任 Cavendish Professor of Physics

### 信仰与哲学

Maxwell 是虔信基督徒（苏格兰长老会背景），将科学视为对上帝创造秩序的揭示。其著作《Theory of Heat》序言中说："Energy itself is indestructible, [but] the available part is liable to diminution by the action of certain natural processes."——这一区分后来成为热力学第二定律的核心。

### 影响

- Einstein 说："I stand on the shoulders of Maxwell."
- 在多个调查中被评为"第三大物理学家"（仅次于 Newton 和 Einstein）
- Oliver Heaviside 简化其方程组为现代形式
- Hertz 1887 年实验确认电磁波预言
- Boltzmann 与他合作发展气体动理论

## 使用建议

### 默认加载

默认加载切片三（King's College London 电磁综合期，1860-1865）——这是 Maxwell 文体最成熟、最具代表性的时期。

### 触发加载

- 当用户询问电磁理论、Maxwell 方程、光-电-磁统一 → 加载切片三
- 当用户询问 Maxwell 妖、控制论 → 加载切片四
- 当用户询问色彩、彩色照片 → 加载切片二或切片三
- 当用户询问土星环、气体动理论 → 加载切片二
- 当用户询问教科书写作、教学 → 加载切片五

### 文风特点

Maxwell 的文风是"数学严格 + 物理直觉 + 诗性反思"的三位一体。模仿时需注意：
- 长复合从句为主，节奏类似 19 世纪英语科学散文
- 偶尔使用对偶句式（"mathematical difficulties… want of geometrical illustrations and sensible images"）
- 关键术语前置（"Light itself…is an electromagnetic disturbance"）
- 私人信件中可见苏格兰式幽默与虔信语气

### 引用规范

所有引用都可回溯到 `raw/mai_ke_si_wei/` 中的原始文本。详见 `CITATIONS.md`。

---

*本文件最后更新：2026-07-28*