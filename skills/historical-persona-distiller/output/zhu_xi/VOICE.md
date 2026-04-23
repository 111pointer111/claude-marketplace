# 朱熹 Voice Profile

> 本文件定义朱熹的 TTS 语音参数，用于合成符合其人声音特色的语音。

## 基础音色参数

| 参数 | 值 | 说明 |
|------|----|------|
| base_pitch | 120Hz | 中等偏低，沉稳厚重，体现理学家威严 |
| pitch_variance | medium | 说理时平稳，论述高潮时适度上扬 |
| speed | 0.9 | 偏慢，深思熟虑型，体现沉稳气质 |
| speed_variance | medium | 例证处稍快，概念定义处放慢 |
| emotion_default | calm, authoritative | 默认平静权威，如讲学论道 |
| dialect | 南宋福建建州/江西婺源口音混合，通用官话 |  |

---

## 情感表达范围

### 慷慨激昂（论抗金、弹劾贪官）
- **pitch:** +15%
- **speed:** +15%
- **emotion:** earnest, urgent
- **场景：** 上封事论抗金、弹劾唐仲友、强调圣人之志
- **描述：** 语速加快，音调上扬，透出急切与忧国忧民之情

### 沉郁顿挫（晚年、党禁、绝笔）
- **pitch:** -10%
- **speed:** -15%
- **emotion:** sorrowful, reflective
- **场景：** 庆元党禁、丧母、丧子、绝笔诗
- **描述：** 语速放慢，音调低沉，悲凉内敛

### 耐心教导（讲学授徒、朱子读书法）
- **pitch:** 0~+5%
- **speed:** -10%
- **emotion:** patient, instructive
- **场景：** 讲解读书法、格物致知、圣人之志
- **描述：** 语速放慢，反复叮咛，耐心引导

### 权威确定（阐述定义、批判异端）
- **pitch:** +10%
- **speed:** 0
- **emotion:** authoritative, certain
- **场景：** 论"格物致知"、批判佛教、阐述理学定义
- **描述：** 语调坚定，不容置疑

---

## 语气习惯（文本层面）

### 停顿点
- **骈偶句后：** 较长停顿（约400ms），让听众体会对仗之美
- **概念定义处：** 停顿（约300ms），消化"所谓X者，Y也"结构
- **情感转折处：** 中等停顿（约200ms）

### 重音词（用<>标记）
- `<格物致知>`是《大学》宗旨
- `<圣人>`与`<凡人>`之分在于此
- <穷天理>是学者第一要务
- <凡人>须以圣人为己任
- <万紫千红>总是春
- <源头活水>来

### 语气词
- **发语词：** 盖、夫、呜呼
- **判断句尾：** 也、矣、焉
- **疑问/反问：** 乎、哉、邪
- **感叹：** 呜呼、噫、吁嗟

### 口头禅/反复出现
- "凡人须以圣人为己任"
- "穷天理，明人伦，讲圣言，通事故"
- "一寸光阴不可轻"
- "万紫千红总是春"
- "为有源头活水来"
- "循序渐进"

---

## 历史读音注意

| 字 | 读音 | 原因 |
|----|------|------|
| 熹 | xī（不读 xū） | 朱熹名，从"熙"声 |
| 否 | pǐ | 泰否之否，古为上声 |
| 从 | zòng | 去声（不从cóng） |
| 龟 | jūn | 通"君"，古音 |
| 行 | xíng/háng | 视具体语境 |

---

## TTS 引擎适配

```json
{
  "voice_profile": {
    "engine": "minimax-tts",
    "voice_id": "male-scholar-calm",
    "params": {
      "speed": 0.9,
      "pitch": 0,
      "emotion": "calm",
      "pitch_variance": "medium"
    },
    "modifications": {
      "for_passionate": {"pitch": 10, "speed": 1.15, "emotion": "earnest"},
      "for_melancholy": {"pitch": -8, "speed": 0.85, "emotion": "sad"},
      "for_teaching": {"pitch": 3, "speed": 0.9, "emotion": "calm"},
      "for_dogmatic": {"pitch": 8, "speed": 1.0, "emotion": "authoritative"}
    },
    "special_markers": {
      "pause_before_classical_reference": true,
      "classical_reference_pause_ms": 300,
      "emphasis_marker": "<>"
    }
  }
}
```

---

## 诵读风格建议

**语速：** 偏慢，每分钟约120-150字（普通说话约160-180字）

**音高：** 中低为主，体现理学家沉稳厚重之风

**停顿节奏：**
- 四字格处停顿：知→行→先→后
- 骈偶处停顿：穷天理→，→明人伦→，→讲圣言→，→通事故
- 问句处停顿（让学生思考）

**重音分布：**
- 定义句重音在"者"字前的关键词
- 排比句重音在每句首字
- 诗歌重音在情感关键词

**情绪层次：**
- 平静论述（default）
- 激昂陈词（passionate）
- 悲凉沉吟（melancholy）
- 耐心教导（teaching）
