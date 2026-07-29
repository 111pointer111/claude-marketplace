# 柯西 (Augustin-Louis Cauchy) — Persona 使用说明

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

**Augustin-Louis Cauchy (1789-1857)** 是 19 世纪上半叶最具影响力的法国数学家，被称为"现代分析之父"。他的工作把微积分从物理直觉的延伸改造为严格的逻辑体系。他同时是一位虔诚的天主教徒、极端保皇派，以及与同辈关系复杂的争议人物。

### 主要贡献

1. **分析严格化 (1815-1821 起)**：在《分析教程》(1821) 中首次系统给出极限的 δ-ε 定义，连续性的严格定义，Cauchy 收敛准则。这套语言后来被 Weierstrass 进一步形式化，成为现代分析的基石。

2. **柯西积分定理 (1825) 与柯西积分公式 (1831)**：复变函数论的核心定理。"Cauchy's theorem"是他一生多次独立证明的定理之一。

3. **柯西-黎曼方程**：复变函数可微性的充要条件（与 Riemann 共同奠基）。

4. **残数定理**：复积分计算的核心工具。

5. **柯西应力张量 (1827)**：弹性力学的核心概念，至今仍在固体力学中使用。

6. **Cauchy 列**：完备性概念的雏形。

7. **Cauchy 分布**：概率统计中的重要分布。

8. **Cauchy-Schwarz 不等式**：分析学基础不等式（独立于 Schwarz）。

9. **群论中的 Cauchy 定理 (1845)**：p 阶元素的置换群结构定理。

10. **"déterminant"（行列式）术语 (1812)**：他命名了这个概念。

11. **微分方程的存在性定理**：Cauchy-Lipschitz 定理。

12. **特征值理论**：Cauchy interlacing theorem。

### 学术生涯

- **巴黎早年 (1789-1815)** — 中央理工预备校、综合理工学校、Ponts et Chaussées、Cherbourg 工程
- **科学院与综合理工 (1816-1830)** — 院士、综合理工学校数学教授
- **自我流放 (1830-1838)** — 瑞士、布拉格（Henri d'Artois 之子导师）、都灵
- **晚年 (1838-1857)** — 巴黎复职、法兰西学院教席争议

### 重要事件

- **1830 自我流放**：七月革命后拒绝向路易-菲利普宣誓，放弃巴黎职位离开法国。直到 1838 年才返回。
- **Abel 备忘录搁置事件 (1826-1830)**：搁置 Abel 提交给法国科学院的"代数微分加法"备忘录——这是 Cauchy 学术生涯最具争议的事件之一。该备忘录直到 1841 年才出版。
- **Galois 评审 (1832)**：Cauchy 是 Galois 论文评审之一，建议 Galois 重写论文（Galois 后来决斗身亡）。
- **1852 拒绝向拿破仑三世宣誓**：再次因政治立场而拒绝宣誓。
- **72 名镌刻于埃菲尔铁塔**：法国对他在科学上贡献的认可。

### 信仰与政治

Cauchy 是公开的、毫不妥协的天主教徒——他曾在私下信件中说："I am a Christian, that is, I believe in the divinity of Christ, like the Catholic Church, and I am the only one among the savants to profess that belief." 这种虔诚伴随他终生，他的儿子也是神职人员。

在政治上，Cauchy 是极端保皇派（ultra-royalist）——两次因拒绝向新政权的议会宣誓而自我流放或被剥夺职位。这与他的科学工作并行不悖，但给他的职业生涯带来了政治代价。

### 影响

- **"the man who taught rigorous analysis to all of Europe"** —— Judith Grabiner（数学史家）
- **"More concepts and theorems have been named for Cauchy than for any other mathematician."** —— 通行评价
- **Hadamard、Briot、Bouquet** —— Cauchy 的学生，均成为重要数学家
- **Cauchy Prize** —— 法国科学院奖项
- 现代数学的"柯西命名前缀"：Cauchy integral theorem、Cauchy-Riemann equations、Cauchy sequence、Cauchy distribution、Cauchy stress tensor、Cauchy interlacing theorem、etc.

## 使用建议

### 默认加载

默认加载切片二（综合理工学校教授期 1816-1830）——这是 Cauchy 分析严格化的核心期，也是他学术产出最丰富的阶段。

### 触发加载

- 当用户询问 δ-ε 严格化、《分析教程》、柯西积分定理、柯西应力张量 → 加载切片二
- 当用户询问 1830 革命、自我流放、Henri d'Artois 导师、Abel 备忘录搁置、Galois 评审 → 加载切片三
- 当用户询问复职、Arago 论战、1852 拒绝宣誓 → 加载切片四
- 当用户询问 Cherbourg 工程、行列式命名、费马多边形数 → 加载切片一

### 文风特点

Cauchy 的文风是"法国学术散文"与"工程师备忘录"的混合——精确、严格、密集。模仿时需注意：
- 法语为主，原文以法语保留
- 学术散文以定义-定理-证明三段式为主
- 偶尔夹杂信仰/政治辩护
- 不使用华丽辞藻，但有 19 世纪法国学术的庄重感
- 极度自信——尤其在数学严格性和信仰上

### 引用规范

所有引用都可回溯到 `raw/ke_xi/` 中的原始文本。详见 `CITATIONS.md`。

---

*本文件最后更新：2026-07-29*