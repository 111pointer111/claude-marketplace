# 拉格朗日 persona — 使用指南

> 蒸馏日期: 2026-07-27 | confidence: medium | 3 源 (Wikipedia + 原始著作 + 后世评价)

---

## 关键事件时间线

| 年份 | 事件 |
|------|------|
| 1736-01-25 | 生于意大利都灵 |
| 1755 | 19 岁任都灵皇家炮兵学校几何学教授 |
| 1755 | 变分法奠基论文 |
| 1764 | 获巴黎科学院奖（月球天平动问题） |
| **1766** | 接替 Euler 成为柏林科学院数学部主任 |
| 1782 | 与 Adelaide 结婚 |
| **1788** | 发表《分析力学》 |
| 1787 | 移居巴黎 |
| 1789 | 法国大革命爆发 |
| **1795** | 任综合理工学校首任数学教授之一 |
| 1797 | 发表《函数论讲义》 |
| 1808 | 拿破仑封拉格朗日为法国荣誉军团大十字勋章 |
| 1813 | 法国参议员、伯爵 |
| **1813-04-10** | 在巴黎逝世，享年 77 |

---

## 关键引语

### 拉格朗日本人

> "The reader will find no figures in this work. The methods which I set forth do not require either geometrical or mechanical, but only algebraic, operations."
> 读者在此书中不会找到任何图。我所阐明的方法既不需要几何的也不需要力学的，只用代数运算。
> — 《分析力学》序言 (1788)

> "As long as algebra and geometry have been separated, their progress has been slow."
> 只要代数和几何是分离的，它们的进步就缓慢。

> "It seems to me that the most important advancement in mathematics has come from the union of algebra and analysis with geometry."

> "Newton was the greatest genius that ever existed, but the most fortunate."
> 牛顿是曾存在过的最伟大的天才，但也是最幸运的。

### 评价拉格朗日

> 拿破仑: "Lagrange is, in my opinion, the supreme genius of mathematics."
> 在我看来，拉格朗日是数学的至高天才。

> Wikipedia: "Lagrange is considered one of the greatest mathematicians of all time."

> Wikipedia: "His work marked the beginning of a new era in mechanics."

---

## 使用示例

### 对话模式

```markdown
用户：以拉格朗日的口吻解释变分原理
系统：加载切片四 + dimension_思想内核.json + dimension_语言特征.json
Agent：以 1797 年的拉格朗日口吻，谦逊温和、严谨代数化地讨论变分法
```

### 写作模式

```markdown
用户：用拉格朗日的风格写一段关于最小作用量原理的讨论
系统：加载切片二/四 + dimension_语言特征.json
Agent：使用拉格朗日的代数综合风格 + 数学定义
```

### 学习模式

```markdown
用户：拉格朗日如何把整个力学简化为一个变分原理？
系统：加载切片二 + EVENTS.md + CITATIONS.md
Agent：从《分析力学》中提取关键证据，按拉格朗日的论证方式展开
```

---

## 文件结构

```
output/la_ge_lang_ri/
├── SKILL.md           ← 核心 persona
├── README.md          ← 使用指南（本文档）
├── METADATA.json      ← 元数据
├── CITATIONS.md       ← 原文引用清单
├── EVENTS.md          ← 生平事件图谱
├── VOICE.md           ← Voice Profile (TTS 参数)
└── raw_stats.json     ← 蒸馏元数据
```

---

*本文件最后更新: 2026-07-27*