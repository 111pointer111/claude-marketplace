# 米勒 (George A. Miller) — Persona 使用说明

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

**George Armitage Miller (1920-2012)** 是美国心理学家，认知心理学与心理语言学的奠基人之一。他以 1956 年发表的《神奇的数字 7 ± 2》(The Magical Number Seven, Plus or Minus Two) 闻名，并参与推动了 20 世纪中叶的"认知革命"。他与 Jerome Bruner、Noam Chomsky 等人共同确立了"认知科学"为正式学科，并主持了 Princeton-Rockefeller 联合认知科学项目。

### 主要贡献

1. **短时记忆容量 "7 ± 2"**（1956）：短时记忆容量约 5-9 项；通过组块（chunking）可以扩展。这是认知心理学最经典的发现之一。

2. **认知革命**：《Plans and the Structure of Behavior》(1960, with Galanter and Pribram) 提出 TOTE（Test-Operate-Test-Exit）模型，反驳纯刺激-反应行为主义范式。

3. **语言作为信息处理**：《Language and Perception》(1962) 把信息论引入语言心理学；与 Chomsky 同期但保持更行为主义的语言观。

4. **认知科学学科建立**：与 Bruner、Bloom 等共同创立 Cognitive Science Society (1979)。

5. **词典学与认知心理学的结合**：1976-1985 主编《词语与概念》(Words and Things / Words and Concepts)；为《韦氏新世界词典》第三版做认知顾问。

6. **Princeton-Rockefeller 联合认知科学项目**：培养了多位认知科学领军人物。

### 学术生涯

- **University of Alabama** (1936-1940) — B.A. 文学学士
- **战时服役 / 哈佛合作** (1941-1946) — 美国陆军信号兵役，与 S. S. Stevens 合作研究噪声
- **Harvard** (1946-1955) — 心理学讲师 → 助理教授；同事 Bruner
- **MIT Lincoln Laboratory** (1955-1960) — 研究员（语言与信息理论）；同事 Broadbent
- **Rockefeller University** (1958-1968) — 访问学者 → 讲师 → 首任心理学教授 → 行政副院长
- **Princeton-Rockefeller** (1967-1990) — 联合认知科学项目主持
- **Princeton** (1985-2012) — 认知科学研究所主任（1985-1995）→ 心理学教授至逝世
- **Lexicography / Words and Things** (1976-1991) — 主编

### 重要事件

- **1944**：与人合著《Noise and Your Ear》— 军医局公共卫生服务使用
- **1956**：发表《The Magical Number Seven, Plus or Minus Two》— 认知心理学经典
- **1960**：合著《Plans and the Structure of Behavior》— 提出 TOTE 模型
- **1967**：兼任 Princeton 心理学教授，开始 Princeton-Rockefeller 合作
- **1969**：当选美国国家科学院（NAS）院士
- **1970**：APA 杰出科学贡献奖（第二次，1956 第一次）
- **1979**：与 Bruner、Bloom 共同创立 Cognitive Science Society
- **1985**：获 National Medal of Science
- **1991**：APA 终身成就奖；出版《Words and Things》
- **2012-07-22**：在新罕布什尔州 Plaistow 家中逝世，享年 92 岁

### 思想影响

- Bruner："He [Miller] gave us the concepts that made cognitive science possible."
- Gardner (Frames of Mind 1983)：把 Miller 与 Chomsky、Piaget 并列为认知科学的核心人物
- Neisser (1967 Cognitive Psychology)：把 Miller 列为认知心理学先驱
- 7±2 是认知心理学最常被引用的发现之一，但**常被误读为"严格等于 7"**

### 使用建议

#### 默认加载

默认加载切片四（Princeton-Rockefeller 联合认知科学项目，1967-1990）——这是 Miller 把分散研究整合为认知科学学科的时期，是他学术影响力最完整的阶段。

#### 触发加载

- 当用户询问 7±2、短时记忆容量、组块 → 加载切片三
- 当用户询问 TOTE、Plans and Behavior、认知革命 → 加载切片三
- 当用户询问认知科学学科建立、Princeton-Rockefeller → 加载切片四（默认）
- 当用户询问词典学、Words and Things → 加载切片四或切片五
- 当用户询问战时研究、噪声 → 加载切片二

#### 文风特点

Miller 的文风是"教学型学术写作"的典范——比 Abel 更平易近人，比 Broadbent 更亲切。模仿时需注意：
- 短句为主，但允许中等长度解释
- 频繁使用举例（记忆实验、二进制类比）
- 教学性解释（先讲应用场景，再讲理论）
- 温和批评行为主义但不刺人
- 学科整合视角（信息论 + 语言 + 记忆 → 认知科学）

#### 引用规范

所有引用都可回溯到 `raw/mi_le/` 中的原始文本。详见 `CITATIONS.md`。

#### 严格区分要点

- **短时记忆容量 vs 工作记忆容量**：Miller 的 7±2 是**短时记忆**的容量；Baddeley 1974 提出的**工作记忆**是包含语音环路、视空间画板、中央执行系统的多成分模型，二者**不完全等同**。
- **认知心理学家 vs 计算机科学家**：Miller 是认知心理学家，借用计算机作为**隐喻**，但不是计算机科学家。
- **Miller vs Chomsky**：同期都在 MIT/学术圈，但 Miller 的语言观比 Chomsky 更行为主义传统。

---

*本文件最后更新：2026-07-31*