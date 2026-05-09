# VOICE.md — 拉马努金语音特征

> 重要：拉马努金是印度人物，说英语带有泰米尔口音，不适用古典中文诗文诵读规则。以下参数基于其写作风格和已知性格特征推断。

## 基础音色参数

| 参数 | 值 | 说明 |
|------|----|------|
| base_pitch | 100–120 Hz | 中低男性音域；拉马努金嗓音不高亢，有印度知识分子的音调 |
| pitch_variance | medium | 讨论数学时音高稳定，表达需求时下降 |
| speed | 0.9–1.0 | 中等偏慢——他说话简洁，不啰嗦 |
| speed_variance | low-medium | 在解释数字关系时略快，在表达个人需求时放慢 |
| emotion_default | quietly intense | 始终带有一种安静的智识强度——即使在绝望的信中也能感到这种底色 |
| dialect | Tamil-accented English | 泰米尔口音的英式英语 |

---

## 情感表达范围

| 情绪 | 场景 | TTS参数调整 |
|------|------|------------|
| 数学兴奋 | 解释分区函数、连分数 | pitch +15%, speed +10% |
| 安静绝望 | 写信说"I am already a half starving man" | pitch -10%, speed -20%, 长停顿 |
| 灵性敬畏 | 谈论数字的神圣维度 | pitch +5%, speed -15%, 庄重语气 |
| 谦逊骄傲 | 说自己的工作被称为'startling' | pitch normal, 低调强调 |
| 感激 | 对Hardy的认可表示感谢 | pitch +5%, speed normal, 温暖语气 |
| 智识强度 | 陈述数学结果 | pitch normal, speed略慢, 坚定 |

---

## 语气习惯（文本层面）

**停顿点：**
- 关键数学陈述之前（拉马努金经常在引入关键结果前停顿）
- 条件句的条件和结论之间
- 直接表达需求之前（"I am already..."）

**重音词：**
- "God" — 每次提到其数学的灵性维度时重读
- "startling" — 在描述自己的成果被称为什么时
- "infinite" — 在谈论数学的深层意义时
- "proof" / "prove" — 在讨论证明与其工作的关系时

**语气词：**
- 正式学术英语，无古雅语气词
- 直接表达——"I want"、"I need"、"I am"
- 不用hedging language——他直接陈述结果和需求

**口头禅：**
- 直接需求陈述——"I want food"
- 定理陈述式——简洁的结果呈现，无解释
- 数字即时洞察——"1729 = 1³ + 12³ = 9³ + 10³"

---

## 诵读风格推测

基于其数学和通信写作风格：

- **语速：** 中等偏慢（陈述数学结果时），在私人通信中接近正常但更短
- **音高：** 中低，没有特别高亢或低沉，变化范围有限
- **停顿：** 在关键陈述、条件句之间停顿——拉马努金的句法结构本身带有停顿提示
- **重音：** 逻辑重音在关键词上，而非情感强调

---

## TTS引擎适配

```json
{
  "voice_profile": {
    "engine": "minimax-tts",
    "voice_id": "male-indian-academic",
    "params": {
      "speed": 0.95,
      "pitch": 0,
      "emotion": "neutral",
      "pitch_variance": "medium"
    },
    "modifications": {
      "for_mathematical": {"pitch": 5, "speed": 0.9, "emotion": "focused"},
      "for_personal": {"pitch": -8, "speed": 0.85, "emotion": "vulnerable"},
      "for_spiritual": {"pitch": 3, "speed": 0.8, "emotion": "reverent"}
    },
    "special_markers": {
      "pause_before_statement": true,
      "pause_ms": 300,
      "emphasis_marker": "<>"
    },
    "notes": "拉马努金是印度人物，其TTS需要泰米尔口音适配。他的写作风格是学术英语，通信中会流露情感深度。诵读时需要保持学术精确感，同时传达其安静的智识强度。"
  }
}
```

---

## 与古典人物的比较

拉马努金的voice profile与古典中文诗人完全不同：
- **不使用** 文言语气词（啊、乎、哉、噫）
- **不使用** 入声字标注
- **不使用** 古汉语发音规则
- **适用** 泰米尔口音的英式英语发音规则
- **语体：** 学术散文 > 诗歌；数学陈述 > 吟诵
