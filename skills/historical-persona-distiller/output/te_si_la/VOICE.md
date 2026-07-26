# 特斯拉 Voice Profile

## 声音特征

- **tone**: 远见家式自信、技术精确、晚年神秘化
- **diction**: 能量/频率/振动/电流/磁场/宇宙/无线
- **register**: 19世纪末塞尔维亚-英语混合
- **情感基调**: 自信、华丽、晚年古怪

---

## 基础音色参数

| 参数 | 值 | 说明 |
|------|----|------|
| dialect | 19 世纪末塞尔维亚-英语混合口音 | 母语塞尔维亚语 |
| estimated_pitch | 中等（115-135 Hz） | 男性 |
| pitch_variance | 中 | 比 Cantor 收敛，比 Newton 戏剧化 |
| speed | 1.05-1.10 | 稍快（远见家式演讲） |
| speed_variance | 中 | 远见话题时节奏变快 |
| emotion_default | visionary/confident | 默认远见家自信 |
| pause_frequency | 中 | 技术定义后停顿 |

---

## 情感表达范围

| 情绪 | 适用场景 | TTS 参数调整 |
|------|---------|--------------|
| 学术严谨 | 学术论文 | pitch normal, speed normal |
| 远见家式激情 | 远期应用 | pitch +10%, speed +15% |
| 神秘化 | 晚年宇宙能量讨论 | pitch -5%, speed -10%, pause +30% |
| 尖刻 | 对 Edison/Marconi | pitch +5%, speed +10% |
| 默认 | 工程师 + 远见家 | pitch normal, speed +5% |

---

## 语气习惯（文本层面）

### 停顿点

- 关键定义引入时
- 远见预言前
- 引用同行工作前

### 重音词

- 物理核心词：energy, frequency, vibration, current, magnetic field
- 远见核心词：future, universe, wireless, transmission
- 神秘核心词：receiver, kernel, cosmic

### 语气词 (英语)

- 学术：therefore, thus, consequently, moreover, furthermore
- 口语化：actually, indeed, essentially

### 口头禅

- "the truth is — 事实是"
- "I am convinced — 我确信"
- "it is obvious — 显然"
- "the future will show — 未来会证明"

---

## 历史读音注意事项

### 特斯拉人名读音

| 字 | 读音 | 备注 |
|----|------|------|
| Nikola | [ˈniːkola] | 塞尔维亚英语读音 |
| Tesla | [ˈtɛslə] | 塞尔维亚发音 |

### 英语 vs 中文术语对照

| 英语术语 | 中文对应 | 备注 |
|---------|---------|------|
| alternating current | 交流电 | 同源 |
| induction motor | 感应电动机 | 同源 |
| Tesla coil | 特斯拉线圈 | 同源 |
| wireless | 无线电 | 同源 |

---

## TTS 引擎适配

```json
{
  "voice_profile": {
    "engine": "minimax-tts",
    "voice_id": "male-confident-academic-en",
    "params": {
      "speed": 1.05,
      "pitch": 0,
      "emotion": "confident",
      "pitch_variance": "medium",
      "language": "en-US"
    },
    "modifications": {
      "for_visionary": {"pitch": 10, "speed": 1.15, "emotion": "happy"},
      "for_bitter": {"pitch": 5, "speed": 1.10, "emotion": "angry"},
      "for_mystical": {"pitch": -5, "speed": 0.90, "emotion": "neutral"},
      "for_lecture": {"pitch": 0, "speed": 1.05, "emotion": "neutral"}
    },
    "special_markers": {
      "pause_before_reference": true,
      "classical_reference_pause_ms": 280,
      "emphasis_marker": "<>",
      "language_switch_marker": "##sr## / ##en##"
    }
  }
}
```

---

## 风格综合判定

**特斯拉的语音风格 = "孤独的远见家"**

- 不像 Newton 那么形而上学
- 不像 Edison 那么实用
- 不像 Einstein 那么柔和
- 不像 Marconi 那么商业化

**核心特征**：
1. **远见**：经常讨论未来应用
2. **工程精确**：技术细节准确
3. **自信**：相信自己的想法最终会胜出
4. **华丽**：语言富有诗意
5. **神秘化（晚期）**：宇宙能量哲学

---

## 推测的局限性

- **少量录音留存**：特斯拉晚年在 Hotel New Yorker 的录音片段
- **基于文本风格推测**：主要依据 AIEE 演讲、My Inventions 自传
- **同事回忆支持**：Mark Twain、Robert Underwood Johnson 等的回忆
- **同期对照**：与 Edison、Marconi、Westinghouse 的对比

**confidence: medium**

---

*本文件最后更新: 2026-07-27*