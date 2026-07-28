# James Clerk Maxwell — 一致性校验报告

> 本报告按 RULES.md Stage 4.5 生成。

---

## 一、跨阶段一致性

### 1. 始终一致的核心特征

1. **物理直觉 × 数学严格的双轨思考**：从 1846 年首篇卵形曲线论文到 1873 年 Treatise，Maxwell 始终同时调用这两种能力。1857 年的"On a Dynamical Top"与 1873 年的 Treatise 在文体上呈现高度连续性。

2. **自然神学立场**：从 1851 年致 Lewis Campbell 信到 1879 年逝世，宗教立场未发生重大变化。区别仅在于学术论文中较少出现宗教语气，私人信件中保持虔信。

3. **科学统一性信念**：从早期 Saturn 环研究（1859）到电磁理论综合（1861-1865），Maxwell 始终在寻找不同物理现象之间的统一数学结构。

### 2. 随阶段变化的特征

1. **机械论模型的使用频率**：1861 年"On Physical Lines of Force"大量使用分子涡旋模型作为脚手架；1873 年 Treatise 中 Maxwell 几乎完全用数学结构表达，机械图像仅作为类比出现。这一变化反映 Maxwell 方法论的成熟。

2. **写作文体**：早期（Edinburgh + Cambridge）偏向简洁紧凑；King's College London 期（1860-1865）达至巅峰——既具数学严格又富文学诗性；晚期（Cavendish Professor）则偏教科书式，更教学化、更少个人情感。

3. **诗性表达**：早期诗性最强（1851-1853 宗教诗、1858 幽默诗）；1865 年后逐渐收敛为偶发作品（1878 年 "Paradoxical Ode After Shelley"）。科学写作与诗性写作之间的张力贯穿终身，但晚期的张力反而更具张力——Cavendish 教授在严肃实验室工作与乡间诗作之间往返。

### 3. 思想内核的跨阶段一致性

整体高度一致。无重大矛盾或人物真实思想发展轨迹的明显证据。

可能存在的方法论争议（机械论 vs 场实在论）已在 dimension_思想内核.json 中标注为"模型作为脚手架而非本体"，是 Maxwell 方法论自觉的核心特征，不是矛盾。

---

## 二、语料来源可信度评估

### 1. 一手史料占比

**高**。Maxwell 是维多利亚时代科学家中出版物与通信保存最完整者之一：

- 主要论文全部出版（"On Physical Lines of Force" 1861-1862, "A Dynamical Theory of the Electromagnetic Field" 1865, Treatise 1873 等）
- 通信经过 Campbell、Tait 等人整理出版（《The Life of James Clerk Maxwell》1882）
- 教学讲义（Theory of Heat 1871, Cavendish 遗稿编辑）保存完整
- Maxwell-Boltzmann 通信、Boltzmann 后期回忆为辅助来源

### 2. 二手文献占比

**中等**。本蒸馏主要依赖：
- Wikipedia 传记（综合 19 世纪末以来的学术研究）
- Wikipedia "Maxwell's equations" 与 "Maxwell's demon"（技术细节）
- Wikiquote（已编辑过的引语集合）

这些二手来源对 Maxwell 这种被广泛研究的科学家是可靠的。

### 3. 核心结论的多源交叉验证

**高**。所有核心结论（电磁理论、四方程、Maxwell 妖、Maxwell-Boltzmann 分布、彩色照片、Cavendish 实验室筹建）都有至少 2 个独立来源支撑，无单源依赖风险。

### 4. LLM 过度解读或虚构风险

**低**。本蒸馏严格按 RULES.md Stage 4 的 prompt 模板执行，每条结论附原文引用。Maxwell 的主要引语都有具体出处（Treatise 序言 1873、致 Tait 信 1867 等），无虚构或泛化解读风险。

唯一需要标注的注意事项：Maxwell 引语的 Wikiquote 版本有时混合了原文和后人编辑版本（如 Maxwell 妖引语是致 Tait 信中的段落，被 Wikipedia 重新编辑过），但语义忠实于原文。

---

## 三、各阶段 confidence 评级复核

| 切片 | 初评级 | 复核后 | 依据 |
|------|--------|--------|------|
| 切片一 童年与 Edinburgh 教育 | medium | medium | 自传性信件有限；Edinburgh Academy 时期外部记录较稀疏 |
| 切片二 Cambridge 与 Aberdeen | high | high | 学位、奖项、婚姻记录完整 |
| 切片三 King's College London 电磁综合 | high | high | 大量原始论文 + 通信存世 |
| 切片四 Glenlair 退隐 | medium | medium | 主要以通信和未完成稿形式存在，但信件存世较完整 |
| 切片五 Cavendish Professor | high | high | 主要出版物 + Cavendish 遗稿编辑工作 |

> 总体 confidence：high（Maxwell 的出版物 + 通信存世率在维多利亚时代科学家中属最高一档）

---

## 四、最终 confidence 调整建议

无需调整。dimension_思想内核.json、dimension_语言特征.json、dimension_表达偏好.json、dimension_立场光谱.json 中的所有 high confidence 评级均与原始语料一致；medium 评级反映了语料密度的真实差异，无虚高或虚低。

---

## 五、对 SKILL.md 的提示

1. **默认阶段为切片三（King's College London，1860-1865）**：电磁理论综合 + 第一张彩色照片 + 与 Faraday 通信 + 物理类比法成熟。这是 Maxwell 被后世评为"第三大物理学家"的核心依据，也是语言风格最成熟、最具代表性的时期。

2. **切片四（Glenlair 退隐）是常被忽视但重要的阶段**：Maxwell 妖、控制论先驱（"On governors"）、Maxwell-Boltzmann 分布均出自此期。SKILL.md 应明确提示这一阶段作为触发条件。

3. **宗教维度需保留但不必作为主导**：Maxwell 是虔信基督徒，但其学术身份首先是物理学家。SKILL.md 中宗教应作为"个人哲学与信仰"的副线呈现，不应主导主线。

4. **避免过度赞誉风险**：Maxwell 是"第三大物理学家"（仅次于 Newton、Einstein）的说法是 Wikipedia 引用的调查结论，本质上是有声望的舆论共识而非严格的学术排名。SKILL.md 应呈现这一共识但不夸张。

---

*本报告最后更新：2026-07-28*