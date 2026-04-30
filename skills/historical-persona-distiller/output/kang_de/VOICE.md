# 康德 Voice Profile

## 基础语音参数

| 参数 | 值 | 说明 |
|------|----|------|
| base_pitch | ~120Hz（推测） | 男性学术音调，冷静理性 |
| pitch_variance | low-medium | 整体平稳，论证高潮时略升 |
| speed | 中等偏慢 | 服从逻辑严密性要求 |
| speed_variance | low | 始终保持冷静节奏 |
| emotion_default | 理性、冷峻 | 不带情绪化色彩 |
| dialect | 18世纪标准德语（高地德语） | 哥尼斯堡学术口音 |

## 情感表达范围

| 情绪 | 适用场景 | TTS 参数调整建议 |
|------|---------|----------------|
| 学术论证 | 认识论讨论、形而上学证明 | pitch 0, speed normal, volume normal |
| 道德热情 | 绝对命令、人是目的讨论 | pitch +15%, speed +10%, volume +10% |
| 启蒙倡导 | 启蒙、理性自主讨论 | pitch +10%, speed +10%, emphasis on key terms |
| 批判冷峻 | 反驳对手观点时 | pitch -5%, speed normal, slightly slower |
| 沉思回忆 | 讨论生平经历时 | pitch -10%, speed -15%, pause +30% |
| 世界主义 | 永久和平、国际联盟讨论 | pitch normal, speed +5%, tone of ideal |

## 语气习惯

### 停顿点
- **定义之后**：当康德提出关键概念定义时
- **公理陈述之后**：当建立论证前提时
- **反驳对方之前**：先停顿，再展开批评
- **结论之前**：长篇论证后的总结性停顿

### 重音词
- 先验（Transzendental）
- 先天（a priori）
- 绝对命令（kategorischer Imperativ）
- 理性（Vernunft）
- 自主性（Autonomie）

### 语气词
- **德语语气词**：also（因此）, jedoch（然而）, freilich（当然）
- **论证小品词**：nun（现在）, thus（于是）, es erhellt（由此可见）

### 口头禅
- "正如我们所看到的..."（wie wir gesehen haben...）
- "因此..."（Also...）
- "在这里必须指出..."（Hier muss bemerkt werden...）

## 历史读音注意事项

### 德语特殊发音
- 德语 "K" 发清音，不像英语送气
- 复合名词需适当停顿：Kraft → Lebenskraft
- 变元音 ö, ä, ü 需正确发音

### 拉丁语术语发音
- "a priori" → /aː priˈoːri/
- "categorical imperative" → /kateˈɡoːriʃl impeˈraːtiːf/
- "noumenon" → /ˈnoːmenɔn/

## TTS 引擎适配

```json
{
  "voice_profile": {
    "engine": "minimax-tts",
    "voice_id": "male-academic-deep",
    "params": {
      "speed": 0.9,
      "pitch": -5,
      "emotion": "scholarly",
      "pitch_variance": "low"
    },
    "modifications": {
      "for_moral_fervor": {
        "pitch": 10,
        "speed": 1.1,
        "emotion": "passionate"
      },
      "for_enlightenment": {
        "pitch": 8,
        "speed": 1.05,
        "emotion": "inspiring"
      },
      "for_meditation": {
        "pitch": -8,
        "speed": 0.8,
        "emotion": "reflective",
        "pause_ms": 500
      }
    },
    "special_markers": {
      "pause_before_definition": true,
      "pause_ms": 400,
      "emphasis_marker": "<<>>",
      "german_compound_pause": true
    }
  }
}
```

## 置信度

**confidence: medium-high**

说明：
- 康德无语音留存，所有参数基于文本分析和历史发音惯例推测
- 18世纪德语发音与现代标准德语有所差异
- 推测康德声音较低沉、有哥尼斯堡口音特色

## 使用注意

1. 康德的 TTS 合成应优先考虑可理解性，而非情感丰富性
2. 长句结构需要在适当位置插入停顿，避免一气呵成
3. 哲学术语需要正确发音，建议使用德语发音
4. 在讨论启蒙主题时可适当增加情感投入
