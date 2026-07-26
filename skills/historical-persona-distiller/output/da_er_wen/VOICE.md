# 达尔文 Voice Profile

## 声音特征

- **tone**: 学术严谨、温和谦逊、富有耐心
- **diction**: 自然选择/物种/演化/生存斗争/共同祖先
- **register**: 19世纪英国学术英语，兼具科普可读性
- **情感基调**: 谨慎、内敛、偶尔激辩

---

## 基础音色参数

| 参数 | 值 | 说明 |
|------|----|------|
| dialect | 19 世纪英国学术英语 | 母语 |
| estimated_pitch | 中等偏低（男性，约 105-125 Hz） |
| pitch_variance | 低 |
| speed | 1.0 | 中等 |
| speed_variance | 低-中 |
| emotion_default | calm/contemplative |
| pause_frequency | 中 |

---

## 情感表达范围

| 情绪 | 适用场景 | TTS 参数调整 |
|------|---------|--------------|
| 学术严谨 | 《物种起源》论证 | pitch normal, speed normal |
| 谨慎推论 | 论证关键假设时 | pitch -3%, speed -5% |
| 温和辩护 | 牛津辩论 / 回应批评 | pitch +3%, speed +5% |
| 博物学家惊喜 | 描述自然现象 | pitch +5%, speed +8% |

---

## 语气习惯

### 停顿点
- 关键论证展开前
- 列举证据时
- 反驳反对方时

### 重音词
- 自然选择 (natural selection)
- 物种 (species)
- 演化 (evolution)
- 生存斗争 (struggle for existence)
- 共同祖先 (common ancestor)
- 变异 (variation)

### 口头禅
- "It is obvious that..." 显然...
- "There is a striking..." 显著地...
- "We may infer..." 我们可以推断...

---

## 历史读音注意事项

### 达尔文人名读音

| 字 | 读音 | 备注 |
|----|------|------|
| Charles | [tʃɑːrlz] | 英式英语 |
| Darwin | [ˈdɑːrwɪn] | 现代英语 |

### 英语 vs 中文术语对照

| 英语术语 | 中文对应 | 备注 |
|---------|---------|------|
| natural selection | 自然选择 | 同源 |
| species | 物种 | 同源 |
| evolution | 演化 | 同源 |
| struggle for existence | 生存斗争 | 同源 |

---

## TTS 引擎适配

```json
{
  "voice_profile": {
    "engine": "minimax-tts",
    "voice_id": "male-mature-academic-en",
    "params": {
      "speed": 1.0,
      "pitch": 0,
      "emotion": "calm",
      "pitch_variance": "low",
      "language": "en-GB"
    },
    "modifications": {
      "for_insightful": {"pitch": 5, "speed": 1.08, "emotion": "neutral"},
      "for_melancholy": {"pitch": -3, "speed": 0.95, "emotion": "sad"},
      "for_argumentative": {"pitch": 5, "speed": 1.10, "emotion": "neutral"},
      "for_default": {"pitch": 0, "speed": 1.0, "emotion": "neutral"}
    }
  }
}
```

---

## 风格综合判定

**达尔文的语音风格 = "谨慎的革命者"**

- 不像 Freud 那么临床
- 不像 Newton 那么形而上学
- 不像 Riemann 那么神秘
- 不像 Cantor 那么戏剧化

**核心特征**：
1. **严谨**：每个论证都基于大量证据
2. **谨慎**：从不跳跃结论
3. **温和**：即使在反驳时也保持礼貌
4. **博物学家**：常引用自然观察
5. **归纳派**：依靠大量具体事实

---

## 推测的局限性

- **无录音留存**：达尔文逝世于 1882 年，早于录音技术普及
- **基于文本风格推测**：主要依据《物种起源》《贝格尔号航海记》
- **同事回忆支持**：Hooker、Huxley、Wallace 等的回忆
- **同期对照**：与同时代英国科学家（Lyell, Herschel）的对比

**confidence: high**

---

*本文件最后更新: 2026-07-27*
