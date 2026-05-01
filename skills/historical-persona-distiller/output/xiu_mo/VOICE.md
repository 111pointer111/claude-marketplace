# 休谟 David Hume Voice Profile

> 本文件为 TTS 合成休谟声音提供参数建议。休谟是18世纪苏格兰哲学家，其声音特点基于其书面哲学散文风格和生平记录推断。

---

## 基础音色参数

| 参数 | 建议值 | 说明 |
|------|--------|------|
| **语言** | 英语（18世纪苏格兰英语） | 休谟用标准英语写作，但带有苏格兰背景 |
| **音色类型** | male-mature-educated | 受过高等教育的成年男性，带有启蒙时代学者的温雅 |
| **基础语速** | 中等偏慢（0.85–1.0x） | 哲学论证需要时间消化，不宜过快 |
| **音高** | 中低（偏低沉稳，非年轻男性的高亢） | 理性、沉稳、有思想深度 |
| **停顿频率** | 高 | 哲学论证需要停顿思考；句间停顿300–500ms |
| **语气** | 冷静、理性、带轻微讽刺幽默 | 非冷漠，而是优雅的知性 |

---

## 情感表达范围

### 平静论述（默认）
- **场景：** 一般哲学讨论
- **参数：** pitch 0, speed 1.0, pause_ms 400
- **语气：** 冷静、有条理、逻辑清晰

### 讽刺幽默
- **场景：** 讽刺形而上学、嘲讽神学辩论
- **参数：** pitch +5%, speed 1.1, slight smile emphasis
- **语气：** 优雅的讽刺，带有文化优越感的温和嘲讽
- **典型文字：** "Commit it then to the flames: For it can contain nothing but sophistry and illusion."

### 自传式叙述
- **场景：** 谈论个人经历、《人性论》的失败
- **参数：** pitch -5%, speed 0.9, longer pauses
- **语气：** 温和从容，带自嘲式幽默
- **典型文字：** "It fell dead-born from the press, without reaching such distinction, as even to excite a murmur among the zealots."

### 热烈论证
- **场景：** 为自己的哲学立场辩护、论述因果问题时
- **参数：** pitch +10%, speed 1.15, emphasis on key terms
- **语气：** 坚定、自信、论证严密
- **典型文字：** 论述因果习惯论时的热情论证段落

---

## 语气习惯（文本层面）

### 停顿点
- **观念界定后：** 首次提出重要术语（impression, idea, custom, belief）后需要简短停顿
- **条件从句后：** "if... then..." 条件句的 then 后需要停顿
- **因果论证后：** 重要结论前需要停顿
- **例子前：** "For example..." 或具体例证前需要停顿

### 重音
- **关键词重音：** impression, custom, habit, belief, sentiment, nature
- **否定重音：** 当否定一个常见观点时（形而上学可能性等）重音落在否定词
- **类比强调：** 当借用牛顿或科学类比时对关键比喻词加重音

### 语气词
- **书面语气词（罕见口语）：** therefore, hence, consequently, thus（用于逻辑推论）
- **反问语气：** 在论证结束时用反问句引导读者思考
- **讽刺性断言：** 当嘲讽形而上学时，用确定无疑的语气表达极端观点

---

## 历史读音注意事项

### 18世纪苏格兰英语特征
- **'r' 音：** 比现代标准英音更卷曲（Scottish 'r'）
- **元音：** 部分元音与今音略有不同
- **语调：** 苏格兰背景可能导致整体语调略有上升趋势

### 关键哲学术语发音
- **impression /ɪmˈprɛʃən/** — 重音在第二个音节
- **causality /kɔːˈzælɪti/** — 重音在第二个音节
- **sentiment /ˈsɛntɪmənt/** — 重音在第一个音节
- **empiricism /ɛmˈpɪrɪsɪzəm/** — 重音在第二个音节

---

## TTS 引擎适配

```json
{
  "voice_profile": {
    "engine": "minimax-tts",
    "voice_id": "male-mature-calm",
    "params": {
      "speed": 0.9,
      "pitch": -5,
      "emotion": "calm",
      "pause_ms": 400
    },
    "modifications": {
      "for_sarcasm": {
        "pitch": 5,
        "speed": 1.1,
        "emotion": "sarcastic"
      },
      "for_autobiographical": {
        "pitch": -8,
        "speed": 0.85,
        "emotion": "warm"
      },
      "for_passionate": {
        "pitch": 10,
        "speed": 1.15,
        "emotion": "passionate"
      }
    },
    "special_markers": {
      "pause_before_key_term": true,
      "pause_ms": 300,
      "emphasis_marker": "<>"
    }
  }
}
```

---

## 置信度与局限性

**Confidence: MEDIUM**

- 休谟没有语音留存，所有参数均为推断
- 主要基于其书面散文风格和历史记录
- 18世纪苏格兰英语的确切音色已不可考
- 建议通过试读其散文（如Enquiry Section 12）来人工调整TTS参数

---

## 推荐试读文本

> "When we run over libraries, persuaded of these principles, what havoc must we make? If we take in our hand any volume; of divinity or school metaphysics, for instance; let us ask, Does it contain any abstract reasoning concerning quantity or number? No. Does it contain any experimental reasoning concerning matter of fact and existence? No. Commit it then to the flames: For it can contain nothing but sophistry and illusion."

— Enquiry Concerning Human Understanding, Section 12

此段包含休谟最典型的语气特点：讽刺性夸张、冷静论证、优雅的学术嘲讽，适合作为TTS调参测试文本。
