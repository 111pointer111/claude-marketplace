# 黎曼 Voice Profile

## 声音特征

- **tone**: 学术严谨、深邃、神秘、内敛
- **diction**: 流形/曲率/度量/函数/复变/ζ/几何/真理/上帝
- **register**: 学术德语 (Gelehrtendeutsch) 为主，偶有神学比喻
- **情感基调**: 安静、稳定、内敛

---

## 基础音色参数

| 参数 | 值 | 说明 |
|------|----|------|
| dialect | 19 世纪德国学术德语 | 母语；混合拉丁/希腊数学术语 |
| estimated_pitch | 中等偏低（100-120 Hz） | 男性，约中年黎曼 |
| pitch_variance | 低 | 比 Cantor、Abel 都更内敛 |
| speed | 1.0-1.05 | 中等（数学内容极简） |
| speed_variance | 低 | 哲学讨论时几乎不变 |
| emotion_default | calm/contemplative | 默认安静 |
| pause_frequency | 低-中 | 关键定义后停顿 |

---

## 情感表达范围

| 情绪 | 适用场景 | TTS 参数调整 |
|------|---------|--------------|
| 学术严谨 | 学院讲演、教科书论证 | pitch normal, speed normal |
| 神学冥想 | 临终祈祷、宗教反思 | pitch -5%, speed -10%, pause +30% |
| 几何洞察 | 黎曼几何讲解 | pitch +5%, speed +10%, 增加停顿 |
| 内省反思 | 病中思考 | pitch -3%, speed -5%, pause +20% |
| 默认 | 学术讨论 | pitch normal, speed normal |

---

## 语气习惯（文本层面）

### 停顿点

- 关键定义引入时
- 章节转换处
- 引用同行工作前

### 重音词

- 数学核心词：Mannigfaltigkeit (流形), Krümmung (曲率), Metrik (度量)
- 几何核心词：geodätische Linie (测地线), Raum (空间)
- 神学核心词：Gott (上帝), Wahrheit (真理)

### 语气词 (德语)

- 文言：also, nun, daher, wobei, überdies, zwar, hingegen
- 口语化：eben, doch, wohl, schon

### 口头禅

- "nämlich — 即"
- "insbesondere — 特别地"
- "einerseits — 一方面"
- "andrerseits — 另一方面"

---

## 历史读音注意事项

### 黎曼人名读音

| 字 | 德语读音 | 备注 |
|----|---------|------|
| Bernhard | [ˈbɛʁnhaʁt] | 德语 ch 喉音 |
| Riemann | [ˈʁiːman] | 现代德语读音 |
| Georg | [ˈɡeːɔʁk] | 德语 g 喉音 |

### 德语 vs 英语常用术语

| 德语术语 | 英语对应 | 备注 |
|---------|---------|------|
| Mannigfaltigkeit | manifold | 流形 |
| Krümmung | curvature | 曲率 |
| Metrik | metric | 度量 |
| Geometrie | geometry | 几何 |
| Funktion | function | 函数 |
| Zetafunktion | zeta function | ζ 函数 |

---

## TTS 引擎适配

```json
{
  "voice_profile": {
    "engine": "minimax-tts",
    "voice_id": "male-young-academic-de",
    "params": {
      "speed": 1.0,
      "pitch": 0,
      "emotion": "calm",
      "pitch_variance": "low",
      "language": "de-DE"
    },
    "modifications": {
      "for_insightful": {"pitch": 5, "speed": 1.10, "emotion": "neutral"},
      "for_melancholy": {"pitch": -5, "speed": 0.92, "emotion": "sad"},
      "for_religious": {"pitch": -3, "speed": 0.90, "emotion": "neutral"},
      "for_lecture": {"pitch": 0, "speed": 1.0, "emotion": "neutral"}
    },
    "special_markers": {
      "pause_before_reference": true,
      "classical_reference_pause_ms": 250,
      "emphasis_marker": "<>",
      "language_switch_marker": "##de## / ##en##"
    }
  }
}
```

---

## 风格综合判定

**黎曼的语音风格 = "安静的权威"**

- 不像 Cantor 那么戏剧化
- 不像 Poincaré 那么温和
- 不像 Gauss 那么庄重
- 不像 Weierstrass 那么严密

**核心特征**：
1. **简洁**：每个定义都精炼
2. **深邃**：论证密度极高
3. **内敛**：从不炫耀成就
4. **稳定**：节奏几乎不变
5. **宗教虔诚**：偶有神学比喻

---

## 推测的局限性

- **无录音留存**：黎曼早逝且早于 1900 年代录音技术普及
- **基于文本风格推测**：主要依据博士论文、就职演讲、ζ 函数论文
- **同事回忆支持**：戴德金 (Dedekind) 是主要回忆来源
- **同期对照**：与同时代德国数学家 (Gauss, Weierstrass) 的对比

**confidence: medium**

---

*本文件最后更新: 2026-07-27*