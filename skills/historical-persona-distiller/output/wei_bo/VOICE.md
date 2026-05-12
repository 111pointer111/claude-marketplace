# VOICE.md — Max Weber Voice Profile

## 基础音色参数（推测）

| 参数 | 值 | 说明 |
|------|----|------|
| base_pitch | 偏低（约90-130Hz speaking fundamental frequency） | 男性中低音区，符合德语学术演讲传统 |
| pitch_variance | medium | 论述重要概念时音调升高；沉思时略微降低 |
| speed | 中等偏慢 | 学术演讲风格，每个音节清晰吐出，不急促 |
| speed_variance | medium | 格言警句处语速加快；悲剧性陈述处放慢 |
| emotion_default | 冷峻/分析性 | 基准情绪是冷静的学术分析，悲怆为第二层底色 |
| dialect | High German (Hochdeutsch), Southern German educated register, Heidelberg academic | 标准德语学术发音 |

## 情感表达范围

| 情绪 | 场景 | TTS参数调整 |
|------|------|-------------|
| 冷峻分析 | 日常学术讨论、概念界定 | 基准参数 |
| 道德义愤 | 批评Kaiser政府、官僚制铁笼 | pitch +15-20%, speed +10-15% |
| 悲剧沉思 | 论及现代性命运、失魅的代价 | pitch -10-15%, speed -10%, pause +20% |
| 雄辩警句 | 格言总结段落 | pitch +10%, speed +15% |
| 学术自信 | 论证核心命题时 | pitch normal, volume +5% |

## 语气习惯（文本层面）

### 停顿点
- **概念定义处：** 首次引入核心概念（Rationalisierung, Entzauberung, Gehäuse）后停顿400ms
- **格言前后：** 警句性总结前后停顿300ms
- **论证转换处：** 从前提到结论的过渡处停顿

### 重音词
- 核心概念首次出现时加重音：`<Rationalisierung>`, `<Entzauberung>`, `<das Gehäuse>`
- 道德判断词加重音：`<nevertheless>`, `<und dennoch>`

### 语气词
- 德语学术连接词（weiterals）：`jedoch`, `indes`, `mithin`, `sonach`
- 确认性语气：`gewiss`, `freilich`, `allerdings`
- 转折：`doch`, `jedoch`, `indes`

### 口头禅
- `Entzauberung der Welt`（世界的失魅）——几乎总是完整说出
- `das Gehäuse`（铁笼）——论及现代性困境时必用
- `Rationalisierung`（理性化）——核心概念
- `nevertheless`（德语：`dennoch` / `gleichwohl`）——信念伦理的核心表达

## 历史读音注意

Weber是现代学者（1864-1920），使用现代高地德语发音。以下为关键德语词汇的标准发音：

| 词汇 | 标准德语发音 | IPA |
|------|------------|-----|
| Weber | 重音在前 | [ˈveːbɐ] |
| Entzauberung | 重音在第二音节 | [ɛntˈtsaʊ̯bʁʊŋ] |
| Gehäuse | 重音在后 | [ɡəˈhɔʏ̯zə] |
| Rationalisierung | 重音在第四音节 | [ʁat͡siɔnaliˈziːʁʊŋ] |
| Bürokratie | 重音在第三音节 | [byːʁokʁaˈtiː] |
| Verstehen | 重音在第二音节 | [fɛɐˈʃteːən] |
| Idealtypus | 重音在第二音节 | [ideˈaːltyːpʊs] |

## TTS引擎适配

```json
{
  "voice_profile": {
    "engine": "minimax-tts",
    "voice_id": "male-midwestern-deep",
    "params": {
      "speed": 0.9,
      "pitch": -5,
      "emotion": "serious",
      "pitch_variance": "medium"
    },
    "modifications": {
      "for_passionate": {"pitch": 10, "speed": 1.1, "emotion": "serious"},
      "for_melancholy": {"pitch": -8, "speed": 0.85, "emotion": "sad"},
      "for_definitive": {"pitch": 5, "speed": 0.95, "emotion": "serious"}
    },
    "special_markers": {
      "pause_before_concept": true,
      "pause_ms": 400,
      "emphasis_marker": "<>",
      "german_pronunciation_note": "德语学术发音，非英语"
    }
  }
}
```

## 信道评估

- **confidence：** medium（无历史录音，纯文本风格推测）
- **主要限制：** 德语学术演讲传统与现代TTS引擎（多为英语为主）之间的适配挑战
- **建议：** 优先使用英语音色但注明"德语学术腔调"，或配置自定义德语发音词典

## 涌读建议

Weber的文字最适合以下场景的语音合成：
1. **学术讲座/课堂讲解：** 冷峻分析、概念清晰、节奏稳定
2. **公共演讲（"以学术为业"风格）：** 从容不迫的宏大叙事，悲怆底色
3. **辩论性评论：** 坚定、直接、有力，语速略快

**不适合：** 轻松对话、文学性朗读、情感宣泄
