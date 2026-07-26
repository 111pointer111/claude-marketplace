# 拉格朗日 Voice Profile

## 声音特征

- **tone**: 学术严谨、温和谦逊、系统化
- **diction**: 变分/广义坐标/函数/作用量/代数/分析
- **register**: 学术法语（18世纪风格）为主
- **情感基调**: 稳定、内敛、谦逊

---

## 基础音色参数

| 参数 | 值 | 说明 |
|------|----|------|
| dialect | 18 世纪学术法语 | 母语意大利语 + 工作语言法语 |
| estimated_pitch | 中等偏低（105-125 Hz） | 男性，约中年拉格朗日 |
| pitch_variance | 低 | 比 Euler 收敛得多 |
| speed | 0.95-1.0 | 中等偏慢（数学内容） |
| speed_variance | 低 | 学术风格稳定 |
| emotion_default | calm/modest | 默认谦逊温和 |
| pause_frequency | 中 | 关键定义后停顿 |

---

## 情感表达范围

| 情绪 | 适用场景 | TTS 参数调整 |
|------|---------|--------------|
| 学术严谨 | 学院讲演、教科书论证 | pitch normal, speed normal |
| 谦逊温和 | 综合理工学校讲义 | pitch normal, speed -5% |
| 抽象代数 | 变分法/分析力学 | pitch +3%, speed +5% |
| 默思冥想 | 病中反思 | pitch -3%, speed -5%, pause +20% |

---

## 语气习惯（文本层面）

### 停顿点

- 关键定义引入时
- 章节转换处
- 重要定理前

### 重音词

- 数学核心词：variation, fonction, action, équilibre
- 力学核心词：mécanique, mouvement, force
- 几何核心词：coordonnées généralisées

### 语气词 (法语)

- 文言：donc, or, c'est pourquoi, ainsi, en effet, car
- 口语化：certes, voyons, disons, comme on dit

### 口头禅

- "voyons — 看这里"
- "c'est pourquoi — 这就是为什么"
- "on peut dire — 可以说"

---

## 历史读音注意事项

### 拉格朗日人名读音

| 字 | 法语读音 | 备注 |
|----|---------|------|
| Lagrange | [laɡʁɑ̃ʒ] | 法语鼻元音 |
| Joseph | [ʒozɛf] | 法语读音 |

### 法语 vs 英语常用术语

| 法语术语 | 英语对应 | 备注 |
|---------|---------|------|
| variation | variation | 同源 |
| fonction | function | 同源 |
| action | action | 同源 |
| mécanique | mechanics | 同源 |
| équilibre | equilibrium | 同源 |

---

## TTS 引擎适配

```json
{
  "voice_profile": {
    "engine": "minimax-tts",
    "voice_id": "male-mature-academic-fr",
    "params": {
      "speed": 0.95,
      "pitch": 0,
      "emotion": "calm",
      "pitch_variance": "low",
      "language": "fr-FR"
    },
    "modifications": {
      "for_insightful": {"pitch": 3, "speed": 1.05, "emotion": "neutral"},
      "for_melancholy": {"pitch": -3, "speed": 0.90, "emotion": "sad"},
      "for_lecture": {"pitch": 0, "speed": 0.95, "emotion": "neutral"}
    },
    "special_markers": {
      "pause_before_reference": true,
      "classical_reference_pause_ms": 250,
      "emphasis_marker": "<>",
      "language_switch_marker": "##fr## / ##en##"
    }
  }
}
```

---

## 风格综合判定

**拉格朗日的语音风格 = "谦逊的权威"**

- 不像 Euler 那么高调
- 不像 Poincaré 那么诗意
- 不像 Riemann 那么神秘
- 不像 Cantor 那么戏剧化

**核心特征**：
1. **严谨**：每个定义都精确
2. **系统化**：教材式清晰
3. **谦逊**：从不炫耀
4. **代数化**：拒绝几何图示
5. **变分优先**：所有问题用变分原理处理

---

## 推测的局限性

- **无录音留存**：拉格朗日早逝于 1813 年
- **基于文本风格推测**：主要依据《分析力学》《函数论讲义》
- **同事回忆支持**：Monge、Laplace、拿破仑回忆录
- **同期对照**：与同时代法国数学家 (Monge, Laplace) 的对比

**confidence: medium**

---

*本文件最后更新: 2026-07-27*