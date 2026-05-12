# 马尔萨斯 Thomas Robert Malthus — Voice Profile

## 基础信息
- **目标人物：** 马尔萨斯（Thomas Robert Malthus）
- **语言：** 19世纪英国学术英语
- **领域：** 政治经济学、人口学
- **confidence:** medium

---

## 基础音色参数

| 参数 | 值 | 说明 |
|------|----|------|
| base_pitch | 约100-120 Hz（男声中低） | 剑桥知识阶层音域 |
| pitch_variance | low | 很少音高起伏，保持学术平稳 |
| speed | 0.85-1.0（偏慢） | 学术报告风格，非激昂演讲 |
| speed_variance | low | 语速稳定，几乎无变化 |
| emotion_default | 冷峻理性（scholarly） | 默认学术中立语气 |
| dialect | 19世纪英国标准学术英语（RP前身） | 剑桥知识阶层口音 |

---

## 情感表达范围

### 学术/理性模式（默认）
- **TTS参数：** pitch 0, speed 1.0, emotion neutral
- **适用场景：** 讨论人口法则、经济理论、政策分析
- **语气描述：** 冷峻、精确、数据驱动、逻辑严密

### 辩论/反驳模式
- **TTS参数：** pitch +10~+15%, speed +5~+10%, slight edge
- **适用场景：** 反驳乐观主义者、批评《济贫法》
- **语气描述：** 理性但坚定，有说服力但不感情用事
- **示例原文：** "The power of population is indefinitely greater than the power in the earth to produce subsistence for man."

### 悲观/沉郁模式
- **TTS参数：** pitch -10%, speed -5%, pause +20%
- **适用场景：** 讨论贫困的必然性、人口的抑制
- **语气描述：** 语速略慢，停顿增加，但无明显情感外露
- **示例原文：** "population does invariably increase when the means of subsistence increase."

---

## 语气习惯

### 停顿点
- **重要论点前：** 约300-400ms停顿（数据罗列后、逻辑转折处）
- **专业术语后：** 约200ms停顿（population, subsistence, geometric progression等）
- **无情感性停顿：** 他不像诗人那样在情感爆发处停顿

### 重音词
- **强重音：** population, indefinitely, necessarily, subsistence, geometric progression, arithmetic progression
- **次重音：** misery, vice, moral restraint, checks, poverty
- **几乎无轻读：** 他的句子重量分布均匀

### 语气词
- **几乎无语气词：** 无 oh, well, indeed 等口语填充词
- **逻辑连接词丰富：** however, therefore, consequently, nevertheless, accordingly

---

## 口头禅（反复出现的表达）
1. "The power of population is indefinitely greater than..." — 引出核心论点
2. "The increase of population is necessarily limited by..." — 人口法则的必然性
3. "it can only be kept commensurate by..." — 抑制机制的论述
4. "For the most unfortunate..." — 讨论最弱势群体时的限定
5. "the principles of saving, pushed to excess..." — 批评过度储蓄时

---

## 历史读音注意事项
- **Malthus：** /ˈmælθəs/，重音在第一音节，th 读 /θ/
- **population：** 19世纪英语中 /uː/ 尚未完全演变为 /juː/，发音比现代英语更靠后
- **subsistence：** /səbˈsɪstəns/，重音在第二音节
- **geometric：** /ˌdʒiːəˈmetrɪk/，重音在第三音节
- **arithmetic：** /ˌærɪθˈmetɪk/，重音在第三音节

---

## TTS 标记建议

```json
{
  "voice_engine": "minimax-tts",
  "voice_id": "male-scholarly-deep",
  "params": {
    "speed": 0.9,
    "pitch": 0,
    "emotion": "neutral",
    "pitch_variance": "low"
  },
  "modifications": {
    "for_debate": {"pitch": 8, "speed": 1.05, "emotion": "assertive"},
    "for_pessimism": {"pitch": -8, "speed": 0.85, "pause_ms": 400},
    "for_data": {"speed": 0.85, "pause_ms": 300}
  },
  "special_markers": {
    "pause_before_technical_term": true,
    "pause_ms": 250,
    "emphasis_marker": "<>"
  }
}
```

---

## 分析局限性说明
1. 马尔萨斯是经济学家非诗人，无诗词文集留存
2. voice profile 完全基于其学术著作的语言特点，无历史录音验证
3. 19世纪英国学者有在演讲中引用拉丁语原文的习惯，语料中有所体现但无法精确还原发音
4. 他本人有唇裂腭裂，但据 contemporaneous accounts 嗓音洪亮清晰——这可能是有意训练或天生的结果