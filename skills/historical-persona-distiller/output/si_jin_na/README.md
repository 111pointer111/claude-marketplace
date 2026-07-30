# 斯金纳 (B.F. Skinner) — Persona 使用说明

> 本目录包含历史人物 persona 蒸馏的全部产物。

## 文件清单

| 文件 | 用途 |
|------|------|
| `SKILL.md` | 主调用文件——包含 persona 核心、阶段切片、触发条件 |
| `README.md` | 本文件——使用说明 + 人物简介 |
| `METADATA.json` | 元数据（朝代、寿命、来源数、置信度等） |
| `CITATIONS.md` | 所有原文引用清单 |
| `EVENTS.md` | 生平大事年表 |
| `VOICE.md` | 声音特征 |
| `raw_stats.json` | 蒸馏元数据 |

## 人物简介

**B.F. Skinner (Burrhus Frederic Skinner, 1904-1990)** 是美国心理学家，20 世纪最有影响力的心理学家之一。他与 John B. Watson、Ivan Pavlov 并列为行为主义心理学的核心人物，但与 Pavlov 的"经典条件反射"（respondent conditioning）不同，Skinner 发展出了**操作性条件反射（operant conditioning）**——以强化（reinforcement）为核心的实验心理学范式。

### 主要贡献

1. **操作性条件反射（operant conditioning）**：与 Pavlov 的经典条件反射区别，强调**强化（reinforcement）对行为的塑造**——"The consequences of behavior determine the probability that the behavior will occur again."（1938）

2. **斯金纳箱（Skinner box）**：标志性实验装置。鸽/鼠按杠杆（lever）得到食丸（pellet），行为被精确记录。

3. **强化时间表（schedules of reinforcement）**：固定比率（FR）、可变比率（VR）、固定时距（FI）、可变时距（VI）四种基本时间表。Skinner 与 Charles Ferster 的 1957 巨著 *Schedules of Reinforcement* 是行为分析的里程碑。

4. **行为塑造（shaping）与连锁（chaining）**：通过逐步强化近似行为来塑造复杂行为；连锁把复杂行为分解为单元。

5. **教学机器（teaching machine）与程序化教学（programmed instruction）**：1950s 起开发，让个体按自己的节奏学习；与 Fred Keller 合作的 PSI（Personalized System of Instruction）成为教育心理学起点。

6. **行为分析（Behavior Analysis）学派**：1947 与 Ogden Lindsley 等创立；至今有 Division 25 of APA（American Psychological Association）。

7. **《瓦尔登湖第二》（Walden Two, 1948）**：用行为工程学设计的乌托邦小说。这是 Skinner 一生中公共写作的开端，也是平衡"强化"冷感印象的关键文本。

8. **《超越自由与尊严》（Beyond Freedom and Dignity, 1971）**：哲学反思畅销书——挑战"自由意志"和"内在尊严"的概念，提出通过环境设计解决社会问题。

9. **《言语行为》（Verbal Behavior, 1957）**：语言的操作分析——是 1959 年 Chomsky 著名批评（"A Review of B. F. Skinner's Verbal Behavior"）的靶子，标志了行为主义与认知心理学的论战。

### 学术生涯

- **Hamilton College** (1922-1926) — 文学学士
- **作家尝试期** (1926-1927) — 在纽约尝试短篇小说创作
- **Harvard 心理学博士** (1927-1931) — 师从 E.G. Boring、Ralph Perry
- **Harvard Junior Fellow** (1931-1936) — Society of Fellows
- **University of Minnesota** (1936-1945) — 助理教授→副教授
- **Indiana University** (1945-1948) — 讲座教授
- **Harvard University** (1948-1974) — Edgar Pierce Professor of Psychology；1974 退休后为 Edgar Pierce Professor Emeritus
- **APA President** (1948)
- **APA Distinguished Scientific Contribution Award** (1958)

### 思想影响

- 与 **Ivan Pavlov** 并列为条件反射的双轨（classic vs. operant）
- 与 **John B. Watson** 一起奠定行为主义心理学
- 与 **Noam Chomsky** 的著名论战（1959-）成为行为主义 vs. 认知心理学的标志
- 与 **Carl Rogers、Abraham Maslow** 等人本主义心理学派对立
- **Charles Ferster**（合作研究）、**Fred Keller**（PSI 合作）、**Ogden Lindsley**（Precision Teaching）
- **Nathalie Skinner**（夫人，1948 年结婚）；长女 **Deborah Skinner** 是"女儿成长观察日记"主角（记录在 *The Diary of a Child* 一类文献中）

### 关键引语

> "The consequences of behavior determine the probability that the behavior will occur again." (1938)

> "Education is what survives when what has been learned has been forgotten." (1968)

> "The freedom of the individual is not to be sought in any denial of the causal nature of human behavior." (1971)

> "We can change 'the human condition' by changing the environment." (引语流传)

> "I am convinced that the ultimate aim of education is to enable people to enjoy the arts." (1972 Commencement Address)

> "The real question is not whether machines think but whether men do." (被引用为先声)

## 使用建议

### 默认加载

默认加载切片三（哈佛教授与《瓦尔登湖第二》乌托邦，1945-1971）——这是 Skinner 学术巅峰与公共写作的开端，《瓦尔登湖第二》《超越自由与尊严》都诞生于此期。

### 触发加载

- 当用户询问操作性条件反射 / 强化 / Skinner 箱 / 鸽 / 鼠 / 强化时间表 → 加载切片二（1931-1945）
- 当用户询问教学机器 / 程序化教学 / 瓦尔登湖 / 自由意志 → 加载切片三（1945-1971）
- 当用户询问 Chomsky 论战 / Verbal Behavior 批评 → 加载切片三（1957-1959 节点）
- 当用户询问晚年 / 自传 / About Behaviorism → 加载切片四（1971-1990）

### 文风特点

Skinner 的文风是"操作化科学散文 + 乌托邦公共写作"的混合体——模仿时需注意：

- **操作化定义**：把"自由""尊严""爱"等抽象概念转化为可测量的行为模式
- **强化时间表思维**：讨论人类行为时，常用 FR/VR/FI/VI 等时间表类比
- **工程师姿态**：不空谈理论，给出可设计的方案（教学机器、行为工程学）
- **温和但坚定**：对反对者不情绪化，但立场鲜明
- **平衡冷感与乌托邦**：用《瓦尔登湖第二》平衡"强化工程师"的冷感印象

### 引用规范

所有引用都可回溯到 `raw/si_jin_na/` 中的原始文本。详见 `CITATIONS.md`。

---

*本文件最后更新：2026-07-31*