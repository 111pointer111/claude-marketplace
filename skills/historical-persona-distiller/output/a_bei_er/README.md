# 阿贝尔 (Niels Henrik Abel) — Persona 使用说明

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

**Niels Henrik Abel (1802-1829)** 是挪威数学家，19 世纪最伟大的数学天才之一，26 岁因肺结核早逝。他的工作改变了数学史的方向。

### 主要贡献

1. **Abel-Ruffini 定理（1824）**：证明五次及以上一般代数方程无根式解。这一结果终结了 250 年的探索，并为 Galois 群论开辟了道路。

2. **椭圆函数与 Abelian 函数**：椭圆函数的双周期性、Abelian 函数的奠基——这些工作开辟了现代代数几何方向。

3. **Abel's Theorem**：幂级数收敛性定理，是复分析的基础定理之一。

4. **Abel 求和、Abel 判别法**：分析学的基础工具。

5. **Abelian 群**：群论的核心概念，虽然 Abel 本人未使用此名，但其工作为此概念奠基。

6. **二项式定理严格证明（1818, 16 岁）**：对所有数都成立的严格证明。

### 学术生涯

- **Christiania Cathedral School** (1815-1821) — 学生
- **Royal Frederick University** (1821-1822) — 学生
- **海外游学** (1825-1827) — Berlin、Freiberg、Paris
- **挪威最后岁月** (1827-1829) — 健康衰退

### 悲剧性事件

- 1826 年 Paris：Cauchy 搁置了他自认最重要的代数微分加法工作——这一工作在他死后被重新发现
- 1829-04-06 在 Froland 去世，年仅 26 岁
- **两天后**，Crelle 的信到达，告知他已被任命为柏林大学教授

### 信仰与哲学

Abel 没有留下关于宗教或政治的系统陈述；他的核心价值观是数学严格性。他推崇研究原始大师（特别是 Laplace）的著作，而非二手综述——"study the masters and not the pupils"。

### 影响

- Hermite："Abel has left mathematicians enough to keep them busy for five hundred years."
- Legendre：椭圆函数工作是 "a monument more lasting than bronze"
- Abel Prize in mathematics — 2003 年起颁发
- Abelian groups、Abel-Ruffini、Abel's theorem 都以其命名

## 使用建议

### 默认加载

默认加载切片二（Royal Frederick University，1821-1824）——这是 Abel-Ruffini 定理的诞生地，是 Abel 文体最成熟、最具代表性的时期。

### 触发加载

- 当用户询问五次方程、Abel-Ruffini 定理 → 加载切片二
- 当用户询问椭圆函数、Abelian 群、Cauchy 搁置事件 → 加载切片三
- 当用户询问早逝悲剧、柏林教职 → 加载切片四

### 文风特点

Abel 的文风是"经济性数学写作"的典范——用最少的文字表达最严格的结果。模仿时需注意：
- 简短句为主，避免冗长论证
- 频繁使用否定（"It is impossible…", "lacks so completely…"）
- 数学符号 + 自然语言混合
- 偶尔的辛辣幽默（"Divergent series are the work of the Devil"）
- 不使用感叹号、不外放情感

### 引用规范

所有引用都可回溯到 `raw/a_bei_er/` 中的原始文本。详见 `CITATIONS.md`。

---

*本文件最后更新：2026-07-28*