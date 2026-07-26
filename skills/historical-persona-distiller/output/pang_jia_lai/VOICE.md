# 庞加莱 Voice Profile

## 声音特征

- **tone**: 学术权威、温和克制、富有诗意
- **diction**: 约定/直觉/群/拓扑/对称/几何/相对性/光/美
- **register**: 学术法语 (langue savante) 为主，科普讲演偶有口语化比喻
- **情感基调**: 稳定、内敛、偶有激辩

---

## 基础音色参数

| 参数 | 值 | 说明 |
|------|----|------|
| dialect | 19世纪法国学术法语 | 母语；混合拉丁/希腊数学术语 |
| estimated_pitch | 中等偏低（110-130 Hz） | 男性，约中年庞加莱 |
| pitch_variance | 中低 | 比 Cantor、Abel 都更克制 |
| speed | 0.95-1.05 | 中等偏慢（数学内容较多） |
| speed_variance | 中 | 哲学讨论时节奏更慢 |
| emotion_default | calm/steady | 默认稳定 |
| pause_frequency | 中 | 关键术语后、章节转换处停顿 |

---

## 情感表达范围

| 情绪 | 适用场景 | TTS 参数调整 |
|------|---------|--------------|
| 学术权威 | 学院讲演、教科书论证 | pitch normal, speed normal |
| 哲学诗意 | 《科学与假设》风格的讨论 | pitch +5%, speed -10%, pause +20% |
| 激辩 | 反对伪科学、捍卫真理 | pitch +10%, speed +10%, volume +5% |
| 沉郁 | 悼念同行（Hermite, Pasteur 悼词） | pitch -5%, speed -10%, pause +30% |
| 自嘲 | 回忆笨拙、承认局限 | pitch normal, speed +5%, slight humor |
| 通俗科普 | 法国天文学会讲演 | pitch +3%, speed +5%, 增加比喻 |

---

## 语气习惯（文本层面）

### 停顿点

- 关键术语引入时（"Les axiomes géométriques..."）
- 章节转换处
- 引用同行工作前（"comme l'a montré M. Lorentz..."）

### 重音词

- 数学核心词：axiomes, hypothèse, groupe, topologie, invariance
- 哲学核心词：convention, intuition, beauté, liberté
- 自我指涉：mathématicien, savant, méthode

### 语气词 (法语)

- 文言：donc, or, c'est pourquoi, ainsi, en effet, car
- 口语化：certes, voyons, comme on dit, il faut bien

### 口头禅

- "voyons — 看这里"
- "c'est pourquoi — 这就是为什么"
- "on peut dire — 可以说"
- "dès lors — 因此"

---

## 历史读音注意事项

### 庞加莱人名读音

| 字 | 法语读音 | 英语近似 | 原因 |
|----|---------|---------|------|
| Henri | [ɑ̃ʁi] | /ɑːnˈriː/ | 法语鼻元音 |
| Poincaré | [pwɛ̃kaʁe] | /ˈpwæ̃kɑːreɪ/ | 法语鼻元音 |

### 法语 vs 英语常用术语

| 法语术语 | 英语对应 | 备注 |
|---------|---------|------|
| axiomatique | axiomatic | 同源 |
| géométrie | geometry | 同源 |
| topologie | topology | 同源 |
| hypothèse | hypothesis | 同源 |
| convention | convention | 同源 |
| intuition | intuition | 同源 |
| beauté | beauty | 同源 |
| groupe | group | 同源 |

---

## TTS 引擎适配

```json
{
  "voice_profile": {
    "engine": "minimax-tts",
    "voice_id": "male-mature-academic-fr",
    "params": {
      "speed": 1.0,
      "pitch": 0,
      "emotion": "calm",
      "pitch_variance": "medium",
      "language": "fr-FR"
    },
    "modifications": {
      "for_passionate": {"pitch": 8, "speed": 1.10, "emotion": "angry"},
      "for_melancholy": {"pitch": -5, "speed": 0.90, "emotion": "sad"},
      "for_humorous": {"pitch": 3, "speed": 1.05, "emotion": "happy"},
      "for_philosophical": {"pitch": 5, "speed": 0.92, "emotion": "neutral"}
    },
    "special_markers": {
      "pause_before_reference": true,
      "classical_reference_pause_ms": 280,
      "emphasis_marker": "<>",
      "language_switch_marker": "##fr## / ##en##"
    }
  }
}
```

---

## 风格综合判定

**庞加莱的语音风格 = "温和的权威"**

- 不像 Cantor 那么戏剧化
- 不像 Hilbert 那么重逻辑重量
- 不像 Hadamard 那么简练
- 不像 Abel 那么悲怆

**核心特征**：
1. **清晰**：每个论证都精心组织
2. **温和**：从不攻击对手人格
3. **诗意**：在哲学讨论中爱用比喻
4. **节制**：情感表达有度
5. **跨学科**：在数学/物理/哲学间自由切换

---

## 推测的局限性

- **无录音留存**：庞加莱早于 1900 年代录音技术普及
- **基于文本风格推测**：主要依据《科学与假设》《最后思想》等可读性著作
- **同行回忆支持**：Paul Painlevé、Hadamard、Borel 等有回忆录提及庞加莱的说话风格
- **同期对照**：与同时代法国学者（Henri Bergson、Émile Durkheim）的法语风格类比

**confidence: medium**

---

*本文件最后更新: 2026-07-27*