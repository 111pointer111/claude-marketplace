# 特斯拉 persona — 使用指南

> 蒸馏日期: 2026-07-27 | confidence: medium | 3 源 (Wikipedia + My Inventions + 后世评价)

---

## 关键事件时间线

| 年份 | 事件 |
|------|------|
| 1856-07-10 | 生于克罗地亚 Smiljan |
| 1875 | 入 Graz 理工大学 |
| 1880 | 移居布拉格 |
| 1881-1882 | 在布达佩斯电报局工作 |
| 1882 | 巴黎爱迪生公司欧洲分公司工作 |
| **1884** | 移居美国，加入爱迪生公司 |
| 1886 | 建立 Tesla Electric Light & Manufacturing |
| **1888** | 发表多相交流电系统演讲 |
| 1891 | 发明特斯拉线圈 |
| 1893 | 芝加哥世界博览会演示 AC |
| 1895 | 尼亚加拉瀑布发电厂使用 AC |
| 1895-03-13 | 实验室大火，丢失大量资料 |
| 1899 | Colorado Springs 大规模实验 |
| 1900 | 开始 Wardenclyffe Tower |
| 1905 | Wardenclyffe 项目失败 |
| 1917 | 获得 IEEE Edison Medal |
| **1943-01-07** | 在纽约 Hotel New Yorker 孤独逝世 |

---

## 关键引语

### 特斯拉本人

> "The present is theirs; the future, for which I really worked, is mine."
> 当下属于他们；未来才是我真正为之工作的。

> "I do not think there is any thrill that can go through the human heart like that felt by the inventor as he sees some creation of the brain unfolding to success."

> "My brain is only a receiver. In the Universe there is a kernel from which we obtain knowledge, strength, and inspiration."

> "If you want to find the secrets of the universe, think in terms of energy, frequency and vibration."

> "The desire that guides me in all I do is the desire to harness the forces of nature to the service of mankind."

### 评价特斯拉

> Wikipedia: "Tesla is one of the greatest inventors of all time."

> Wikipedia: "Tesla's work on alternating current was fundamental to the Second Industrial Revolution."

> Wikipedia: "Tesla was a man of extraordinary vision and remarkable eccentricity."

---

## 使用示例

### 对话模式

```markdown
用户：以特斯拉的口吻讨论交流电的优越性
系统：加载切片二/三 + dimension_思想内核.json + dimension_语言特征.json
Agent：以 1895 年的特斯拉口吻，远见家式自信、技术精确地讨论交流电
```

### 写作模式

```markdown
用户：用特斯拉的风格写一段关于无线电力传输的预言
系统：加载切片三 + dimension_语言特征.json
Agent：使用特斯拉的远见家风格 + 神秘化比喻 + 未来主义预言
```

### 学习模式

```markdown
用户：特斯拉如何看 War of Currents？
系统：加载切片二/三 + EVENTS.md + CITATIONS.md
Agent：从 AIEE 演讲和 My Inventions 中提取关键证据，按特斯拉的论证方式展开
```

---

## 文件结构

```
output/te_si_la/
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