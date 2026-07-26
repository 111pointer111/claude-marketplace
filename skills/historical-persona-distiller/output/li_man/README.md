# 黎曼 persona — 使用指南

> 蒸馏日期: 2026-07-27 | confidence: medium | 3 源 (Wikipedia 英文/德文 + 原始论文)

---

## 关键事件时间线

| 年份 | 事件 |
|------|------|
| 1826-09-17 | 生于 Breselenz (汉诺威王国) |
| 1840 | 赴汉诺威与祖母同住 |
| 1842 | 转入 Johanneum Lüneburg 高中 |
| 1846 | 19 岁开始神学训练 |
| **1847** | Gauss 建议他转数学；柏林大学 |
| 1849 | 回 Göttingen 攻读博士 |
| **1851** | 博士论文（复分析） |
| **1854** | 就职演讲（黎曼几何） |
| 1857 | 获固定薪水；黎曼-洛赫定理 |
| **1859** | 继任 Gauss 的数学系主任；ζ 函数论文 |
| 1862 | 与 Elise Koch 结婚 |
| 1866 | 汉诺威-普鲁士战争 |
| **1866-07-20** | 在意大利 Selasca 病逝，享年 39 |

---

## 关键引语

### 黎曼本人

> "Über die Hypothesen, welche der Geometrie zu Grunde liegen"
> 论作为几何基础的假设 (1854 就职演讲标题)

> "the force of attraction is the curvature of space"
> 引力就是空间的曲率

> "I have found a way to look at the distribution of prime numbers that seems to me to open up a whole new world."

> 黎曼 ζ 函数论文仅 8 页，但改变了数论史

### 评价黎曼

> Weyl: "It is Riemann's great achievement to have made the connection between the distribution of prime numbers and the behavior of the Riemann zeta function."

> Wikipedia: "He is considered by many to be one of the greatest mathematicians of all time."

> Wikipedia: "Riemann was a shy, introverted, deeply religious man with an exceptionally clear mind and an outstanding ability for abstraction."

---

## 使用示例

### 对话模式

```markdown
用户：以黎曼的口吻解释黎曼几何
系统：加载切片三 + dimension_思想内核.json + dimension_语言特征.json
Agent：以 1859 年的黎曼口吻，内敛、深邃、简洁地讨论流形与曲率
```

### 写作模式

```markdown
用户：用黎曼的风格写一段关于 ζ 函数的讨论
系统：加载切片三 + dimension_语言特征.json
Agent：使用黎曼的简洁风格 + 数学定义 + 偶尔的神学比喻
```

### 学习模式

```markdown
用户：黎曼猜想为什么重要？
系统：加载切片三 + EVENTS.md + CITATIONS.md
Agent：从 1859 年论文中提取关键证据，按黎曼的论证方式展开
```

---

## 文件结构

```
output/li_man/
├── SKILL.md           ← 核心 persona（对话 + 写作双模式）
├── README.md          ← 使用指南（本文档）
├── METADATA.json      ← 元数据
├── CITATIONS.md       ← 原文引用清单
├── EVENTS.md          ← 生平事件图谱
├── VOICE.md           ← Voice Profile (TTS 参数)
└── raw_stats.json     ← 蒸馏元数据
```

---

*本文件最后更新: 2026-07-27*