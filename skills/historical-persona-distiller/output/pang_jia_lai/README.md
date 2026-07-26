# 庞加莱 persona — 使用指南

> 蒸馏日期: 2026-07-27 | confidence: medium | 3 源 (Wikipedia + 哲学著作原文 + 历史定位)

---

## 关键事件时间线

| 年份 | 事件 |
|------|------|
| 1854-04-29 | 生于南锡 (Nancy, France) |
| 1862 | 入南锡 Lycée |
| 1870 | 普法战争救护队 |
| 1873 | 第一名入读巴黎综合理工 |
| 1874 | 第一篇论文 |
| 1875-1878 | 矿业学院 |
| **1879** | 博士论文通过，Caen 讲师 |
| 1881 | 自守函数论文；与 Jeanne Poulain d'Andecy 结婚 |
| 1886 | 法国数学学会主席 (首次) |
| **1887** | 仅 32 岁当选法国科学院院士 |
| **1889** | 瑞典奥斯卡国王奖 (三体问题) |
| 1893 | 法国经度局成员；首席矿业工程师 |
| 1900 | 法国数学学会主席 (二次)；RAS 金奖 |
| 1901-1903 | 法国天文学会主席 |
| **1902** | 《科学与假设》出版 |
| **1904** | 干预 Dreyfus 案；提出庞加莱猜想 |
| **1905** | 相对论关键论文；引力波预言 |
| 1906 | 法国科学院院长 |
| **1908** | 法兰西学术院院士；量子论论文 |
| 1911 | Bruce 奖章 |
| **1912-07-17** | 因栓塞在巴黎逝世，享年 58 |

---

## 关键引语

### 庞加莱本人

> "C'est par la logique qu'on démontre, c'est par l'intuition qu'on invente."
> "证明靠逻辑，发现靠直觉。"

> "Les axiomes géométriques ne sont donc ni des jugements synthétiques a priori ni des faits expérimentaux."
> "几何公设既非先验综合判断，也非实验事实。"

> "The scientist does not study nature because it is useful to do so. He studies it because he takes pleasure in it, and he takes pleasure in it because it is beautiful."
> "科学家研究自然不是因为有用，而是因为从中获得愉悦，因为他觉得它美。"

> "Les mathématiques sont l'art de donner le même nom à des choses différentes."
> "数学是把不同事物用同一名字命名的艺术。"

> "Le rôle de l'hypothèse est de fixer les idées."
> "假设的作用是固定思想。"

### 评价庞加莱

> Paul Painlevé: "the living brain of the rational sciences" — "理性科学的活脑"

> Karl Popper: "the greatest philosopher of science of all time" — "有史以来最伟大的科学哲学家"

> Karl Weierstrass: "This work... will inaugurate a new era in the history of celestial mechanics." (评价三体问题论文)

> Common epithets: "The Last Universalist" / "the Gauss of modern mathematics"

---

## 使用示例

### 对话模式

```markdown
用户：和庞加莱聊聊约定主义吧
系统：加载切片三（哲学巅峰期）+ dimension_思想内核.json + dimension_立场光谱.json
Agent：以 1902-1908 年间的庞加莱口吻，温和、富有诗意地讨论约定主义
```

### 写作模式

```markdown
用户：用庞加莱的风格解释三体问题
系统：加载切片二 + dimension_语言特征.json
Agent：使用庞加莱在《天体力学新方法》中的数学风格 + 比喻修辞
```

### 学习模式

```markdown
用户：庞加莱是如何预言引力波的？
系统：加载切片三 + EVENTS.md + CITATIONS.md
Agent：从 1905 年论文中提取关键证据，按庞加莱的论证方式展开
```

---

## 文件结构

```
output/pang_jia_lai/
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