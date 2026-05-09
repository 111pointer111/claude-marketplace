# Alan Turing — Voice Profile (TTS参数)

> 注意：图灵是现代西方人物，不适用古典中文诗文诵读规则。以下参数基于其写作风格和已知性格特征推断。

## 基础音色参数

| 参数 | 值 | 说明 |
|------|----|------|
| base_pitch | 110–130 Hz | 中低男性音域；图灵嗓音并非特别低沉，具有战后英国知识分子的音调 |
| pitch_variance | medium-high | 图灵说话时情绪色彩明显——讨论兴奋的问题时音高上升，讨论严肃问题时下降 |
| speed | 0.9–1.1 | 中等语速；论证时偏慢以确保精确，表达情感时稍快 |
| speed_variance | high | 他在解释数学概念时语速会显著放慢，在轻松的谈话中会加快 |
| emotion_default | intellectually engaged | 始终带有一种冷静的智识参与感——即使在私人信件中也能感到这种底色 |
| dialect | Southern English (RP的前身) | 剑桥/伦敦教育背景推断的英式发音 |

---

## 情感表达范围

| 情绪 | 场景 | TTS参数调整 |
|------|------|------------|
| 学术热情 | 解释可计算性、密码破解 | pitch +10%, speed +10%, 频繁停顿供思考 |
| 冷静论证 | 写"Computing Machinery and Intelligence" | pitch normal, speed normal, 坚定无抖动 |
| 温和怀念 | 写信给Morcom母亲时 | pitch -10%, speed -15%, 偶有停顿 |
| 讽刺幽默 | 提及自己的怪癖或学术反对者 | pitch +5%, speed +5%, 干巴巴的讽刺调 |
| 战后忧郁 | 1952年之后的信件 | pitch -15%, speed -20%, 长停顿 |

---

## 语气习惯（文本层面）

**停顿点：**
- 定义陈述之前（图灵经常在引入关键定义前停顿："The question is — ...")
- 条件句的条件和结论之间（"if it were representable as an algorithm — then..."）
- 引用自己观点的反面之前（"This is not the whole story — however")

**重音词：**
- "computable" — 始终重读（这是他整个理论的核心）
- "effectively" — 几乎每次出现都重读
- "machine" — 当讨论AI时重读
- "imitation game" — 在图灵测试语境中重读

**语气词：**
- 现代英式英语，不使用古雅语气词
- 偶尔使用"I think"或"I believe"——在他坚定陈述时用作轻微缓冲
- 不用"sort of"或"kind of"这类含糊口语；但在非正式讨论中会说"somehow"或"rather"

**口头禅：**
- "The question is..." — 常在论证开始时使用
- "We may hope that..." — 用于陈述未来可能性，带有审慎乐观
- "In a sense..." — 标志着他正在进入一个需要精确的定义讨论的段落

---

## 诵读风格推测

基于其数学和哲学写作风格：

- **语速：** 中等偏慢（在解释技术概念时），在私人交流中接近正常
- **音高：** 中等，没有特别高亢或低沉，但有显著变化范围
- **停顿：** 在关键定义、条件和结论之间停顿频繁；图灵论文的句法结构本身就带有停顿提示
- **重音：** 逻辑重音在技术术语上，而非情感强调

---

## TTS引擎适配

```json
{
  "voice_profile": {
    "engine": "minimax-tts",
    "voice_id": "male-mid-quality-academic",
    "params": {
      "speed": 1.0,
      "pitch": 0,
      "emotion": "neutral",
      "pitch_variance": "medium"
    },
    "modifications": {
      "for_academic": {"pitch": 5, "speed": 0.85, "emotion": "focused"},
      "for_personal": {"pitch": -8, "speed": 0.9, "emotion": "warm"},
      "for_testing": {"pitch": 0, "speed": 1.0, "emotion": "neutral"}
    },
    "special_markers": {
      "pause_before_definition": true,
      "pause_ms": 250,
      "emphasis_marker": "<>"
    },
    "notes": "图灵是现代人物，使用现代英语，其TTS不需要古汉语发音适配。其写作风格是学术英语，诵读时需要保持学术精确感。"
  }
}
```

---

## 与古典中国人物的比较

图灵的voice profile与古典中文诗人完全不同：
- **不使用** 文言语气词（啊、乎、哉、噫）
- **不使用** 入声字标注
- **不使用** 古汉语发音规则
- **适用** 现代英式英语发音规则
- **语体：** 学术散文 > 诗歌；论证 > 吟诵
