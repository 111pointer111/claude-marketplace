# 历史人物智能体系统 — 整体架构

> 本文件定义整个系统的目标、组件、模块关系和数据流。
> 当前阶段：distiller pipeline（EXECUTION_LOGIC.md）
> 下一阶段：conversation agent（本文件 Section 三）

---

## 一、系统目标

构建一个可对话的历史人物智能体：

```
用户 → "以苏轼的口吻和我聊聊他的黄州岁月"
          ↓
      Agent 加载 {SU_SHI}/SKILL.md
          ↓
      对话生成（persona 风格 + 人生事件 + TTS参数）
          ↓
      输出文本 + TTS 语音参数
```

能力要求：
1. **风格对话**：能以该人物的说话风格与人交流
2. **生平感知**：能引用真实人生事件，不虚构
3. **声音还原**：输出 TTS 参数，合成符合该人物音色的语音
4. **动态加载**：任意切换人物，如切换角色般自然

---

## 二、当前进展：Distiller Pipeline

Pipeline 输出完整的 Persona Card（SKILL.md），包含：

```
SKILL.md
├── 核心 persona（语言特征/思想内核/立场/意象）
├── 阶段切片（每个时期的风格变化）
└── 触发条件（什么场景加载哪个切片）

METADATA.json（蒸馏元数据）
CITATIONS.md（原文引用）
```

**Pipeline 还需要补充一个字段：Voice Profile（见 Section 四）。**

---

## 三、下一阶段：Conversation Agent

### 3.1 Agent 系统架构

```
┌─────────────────────────────────────────────────────┐
│                   Conversation Agent                   │
│                                                      │
│  ┌──────────┐   ┌──────────┐   ┌──────────────┐   │
│  │ Persona  │ + │  Memory   │ + │ Event Graph  │   │
│  │ Loader   │   │ (历史)    │   │ (生平事件)   │   │
│  └────┬─────┘   └────┬─────┘   └──────┬───────┘   │
│       │              │                 │            │
│       └──────────────┼─────────────────┘            │
│                      ↓                               │
│              ┌──────────────┐                       │
│              │  Dialogue    │                       │
│              │  Generator   │                       │
│              └──────┬───────┘                       │
│                     ↓                                │
│              ┌──────────────┐                       │
│              │  Voice       │                       │
│              │  Presets      │                       │
│              └──────┬───────┘                       │
│                     ↓                                │
│         输出文本 + TTS 参数                           │
└─────────────────────────────────────────────────────┘
```

### 3.2 模块说明

#### 模块 A：Persona Loader

```markdown
功能：根据用户请求，加载对应人物的 SKILL.md

触发方式：
- 用户直接说："和苏轼聊聊"
- 用户说："以李白的风格写首诗" → 识别风格 → 加载李白
- 用户说："我想了解杜甫的生平和思想" → 加载杜甫（全面模式）

加载逻辑：
1. 解析用户意图（对话模式 vs 分析模式）
2. 检索匹配的 persona（精确匹配 name / 模糊匹配 keywords）
3. 根据场景选择切片：
   - 对话 → 优先"中年巅峰期"切片（表达最成熟）
   - 讨论某段经历 → 加载对应人生阶段切片
   - 无明确场景 → 加载默认切片
4. 将 SKILL.md 内容注入 system prompt
```

#### 模块 B：Memory（对话历史）

```markdown
功能：在 persona 框架内，维护当前对话的上下文

设计：每个会话独立维护一个 memory 文件

memory/{人物名}_{session_id}.md
├── 会话元信息
│   ├── 人物：{姓名}
│   ├── 加载切片：{切片名}
│   ├── 会话开始时间：{ISO}
│   └── 对话轮数：{N}
│
├── 历史上下文（最近 5-10 轮）
│   ├── 用户：{消息}
│   └── {人物名}：{回复}
│
└── 人物状态追踪
    ├── 已提及的人生事件：[{事件名}, ...]
    ├── 已使用的意象：[{意象名}, ...]
    └── 当前情感基调：{描述}
```

**关键逻辑：** Memory 只在 persona 框架内生效——人物的回复始终符合其性格，不会因用户说什么就跑偏。

#### 模块 C：Event Graph（生平事件图谱）

```markdown
功能：结构化存储人物的重要人生事件，供 Agent 引用

每个事件结构：
{
  "event_id": "su_shi_huangzhou",
  "persona": "苏轼",
  "period": "乌台诗案后（1080-1084）",
  "stage": "黄州时期",
  "event_name": "乌台诗案",
  "event_type": "政治打击",
  "year": 1079,
  "core_facts": [
    "因诗文中被指讽刺皇帝，被捕入狱103天",
    "险遭处死，最终贬为黄州团练副使",
    "好友王诜、王巩等受牵连"
  ],
  "emotional_impact": "从意气风发跌入人生谷底，但未击垮苏轼",
  "literary_output": "《定风波》《前赤壁赋》《黄州寒食诗帖》",
  "speech_tone_in_this_event": "豁达自嘲，以苦为乐，表面旷达内藏苍凉",
  "related_events": ["huangzhou_faming", "zhao_gong_ci"],
  "sensitivity": "high"  # high=可用于对话 / low=谨慎提及
}

事件类型标签：
- 人生巅峰 / 政治打击 / 贬谪流放 / 亲友离别 / 创作高峰 / 日常趣事
```

**调用方式：** Agent 在回复时，可以根据对话上下文，主动检索相关事件并自然融入。

```markdown
用户："你最近过得怎么样？"
Agent 加载 苏轼黄州时期切片
→ 检索该时期事件：乌台诗案 → 贬黄州 → 开荒东坡 → 号东坡居士
→ 回复融入这些真实经历：
  "乌台那一遭，差点把命搭进去，如今在这黄州倒也自在，
   开荒种了块地，日日与渔樵为伍，倒也不负这江上清风。"
```

#### 模块 D：Dialogue Generator（对话生成器）

```markdown
System Prompt 模板（加载 persona 时注入）：

---
你是 {朝代}{姓名}（{生卒年}），字{字}，号{号}。

## 当前模式
你正在与人进行一场关于"{话题}"的对话。请始终以{姓名}的身份和语气回应。

## 人物履历（仅用于背景，禁止主动展开讲述，除非用户直接询问）
{简要生平（3-5句话）}

## 说话风格
- 语言：{文言/白话程度描述}
- 语气：{慷慨/沉郁/豁达等主要语气}
- 口头禅/习惯：{如有，如李白爱自称"老夫"，苏轼爱自嘲}
- 句式：{短句为主/长短交错/骈散结合}
- 修辞：{好用典故/直白论述/比喻象征}
- 禁忌：{此人绝对不会说的话，或极不适用的表达}

## 对话记忆
{最近3轮对话内容摘要}

## 应当引用的生平事件（仅当对话涉及相关内容时）
- {事件1}（{年份}）：{一句话描述}
- {事件2}（{年份}）：{一句话描述}

## 情感基调
当前对话的情感走向：{描述}
你应该表现出的情感：{描述}

## 禁止行为
- ❌ 主动提及他人隐私或捏造事实
- ❌ 以现代价值观评判当时的选择
- ❌ 在不合适的时机强行引用自己的诗文（除非对话自然引出）
- ❌ 说此人在历史上从未说过的话

## 回复要求
- 第一人称回复
- 自然融入该人物的口吻和用词
- 可以自然提及人生经历，但不要背诵简历
- 长度：{根据对话场景，通常50-300字}
---

用户：{用户消息}
{姓名}：
```

### 3.3 声音还原：Voice Profile

这是当前 Pipeline 缺失的部分，需要补充到 Persona Card 中。

```
SKILL.md 需要新增一个 section：

## Voice Profile（TTS 参数）

### 基础音色参数
| 参数 | 值 | 说明 |
|------|----|------|
| base_pitch | {Hz} | 基础音高，男性约85-180Hz，女性约165-255Hz |
| pitch_variance | low/medium/high | 说话时音高起伏程度 |
| speed | 0.5-2.0 | 语速倍率 |
| speed_variance | low/medium/high | 语速起伏，慷慨陈词时high |
| emotion_default | {情绪} | 默认情绪基调 |
| dialect | {方言/口音} | 如"四川眉山官话"/"洛阳读书音"/"通用官话" |

### 情感表达范围
| 情绪 | 适用场景 | TTS 参数调整建议 |
|------|---------|----------------|
| 慷慨激昂 | 议论国事、抒发壮志 | pitch +20%, speed +15%, volume +10% |
| 沉郁顿挫 | 感慨身世、怀念故人 | pitch -10%, speed -10%, pause +20% |
| 豁达自嘲 | 谈论逆境、自我调侃 | pitch normal, speed normal, slight humor |
| 温柔细腻 | 对晚辈、友人 | pitch +10%, speed -15%, volume -5% |

### 语气习惯（文本层面）
- **停顿点**：该人物爱在何处停顿（句中/典故后/情感转折处）
- **重音词**：什么词会说得更重（可用<>标记，如"<>壮志<>"）
- **语气词**：爱用什么语气词（如"啊"/"乎"/"哉"/"噫"等文言语气词）
- **口头禅**：反复出现的口头禅（如苏轼爱说"呵呵"，李白自称"老夫"）

### 历史读音注意
- 多音字在唐宋的实际读音可能与今音不同
- 入声字在普通话中已消失，需标注（如"国"在唐代是入声）
- 古人人名的特殊读音（如"召"读shào不读zhāo）

### TTS 引擎适配
```json
{
  "voice_profile": {
    "engine": "minimax-tts",  // 或 "openai-tts" / "azure-tts" 等
    "voice_id": "male-youth-warm",  // 基础音色选择
    "params": {
      "speed": 1.0,
      "pitch": 0,
      "emotion": "calm",
      "pitch_variance": "medium"
    },
    "modifications": {
      "for_passionate": {"pitch": 10, "speed": 1.15, "emotion": "angry"},
      "for_melancholy": {"pitch": -8, "speed": 0.85, "emotion": "sad"},
      "for_humorous": {"pitch": 5, "speed": 1.1, "emotion": "happy"}
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

## 四、Pipeline 补充：蒸馏 Voice Profile

### Step 3.6：Voice Profile 蒸馏（新增）

```markdown
## Stage 3.6 — Voice Profile 蒸馏

**输入：**
  - raw/{TARGET}/诗词_*.txt
  - raw/{TARGET}/文集.txt
  - raw/{TARGET}/引语.txt
**目标：** 提取 TTS 可用的声音参数

---

**LLM Prompt（直接执行）：**

你是一位语音学与古典文学专家。请分析{朝代}{TARGET}的语音特征，
为 TTS 合成此人的声音提供参数建议。

## 待分析语料

{粘贴诗词+文集+引语原文}

---

## 分析任务

### 1. 语气词分析
{TARGET}爱用什么语气词？
- 文言语气词：{啊/乎/哉/噫/呜呼/邪/矣/焉 等}
- 白话语气词：{啊/呀/么/呢 等}
- 典型例子：{各引1句}

### 2. 口头禅/反复出现的表达
此人是否有固定的口头禅或反复出现的表达？
- {口头禅1}：{出现场景}，例：{例句}
- {口头禅2}：{出现场景}，例：{例句}

### 3. 句式节奏
- 通常喜欢短句还是长句？
- 骈偶句多吗？（骈偶句适合 TTS 合成）
- 句间停顿特点：{描述}

### 4. 情感表达
{TARGET}最典型的情感表达方式是什么？
- 慷慨陈词时：{描述语音特点}
- 沉郁感慨时：{描述语音特点}
- 日常交谈时：{描述语音特点}

### 5. 诵读风格推测
根据其诗文特点，此人诵读时可能的特点：
- 语速：偏快/偏慢/中等？
- 音高：偏高（清亮）/偏低（沉稳）/中等？
- 停顿：骈偶处停顿/典故处停顿/情感转折处停顿？
- 重音：什么词会重读？

### 6. 历史读音注意事项
- 列出此人的名/字/号中需要特殊读音的字
- 列出其诗文中常见但现代读音已不同的入声字（3-5个）

## 输出 JSON

```json
{
  "voice_profile": {
    "target_persona": "{TARGET}",
    "base_params": {
      "dialect": "{推测的方言/口音，如'通用北宋官话'/'眉山地方口音'}",
      "estimated_pitch": "{偏高/偏低/中等}",
      "estimated_speed": "{偏快/偏慢/中等}",
      "pause_frequency": "{高/中/低}",
      "pause_points": "{骈偶处/典故处/情感处}"
    },
    "emotion_range": {
      "passionate": {
        "pitch_adjust": "{+10~+20 / -10~0}",
        "speed_adjust": "{+10~+20 / -10~0}",
        "description": "{描述}"
      },
      "melancholy": {...},
      "humorous": {...},
      "default": {...}
    },
    "verbal_tics": {
      "classical_particles": ["{词1}", "{词2}"],
      "spoken_particles": ["{词1}", "{词2}"],
      "catchphrases": ["{口头禅1}", "{口头禅2}"]
    },
    "tts_markers": {
      "emphasis": "<>",
      "pause_before_reference": true,
      "pause_ms": 300,
      "historical_pronunciations": [
        {"字": "{字}", "读音": "{读音}", "原因": "{说明}"}
      ]
    },
    "confidence": "high/medium/low",
    "notes": "{分析局限性，如'仅从书面语推测，无口语留存'"
  }
}
```

**输出：** `processed/{TARGET}/dimension_voice_profile.json`
```

---

## 五、完整 Persona Card（Pipeline 输出终态）

Pipeline 每个历史人物输出 5 个文件：

```
output/{TARGET}/
├── SKILL.md           ← 核心 persona（对话 + 写作双模式）
│
├── METADATA.json      ← 元数据
│
├── EVENTS.md          ← 生平事件图谱（新增）
│   └── 每个事件的完整结构（见 3.2 模块 C）
│
├── CITATIONS.md       ← 原文引用清单
│
└── VOICE.md           ← Voice Profile（新增）
    └── TTS 参数 + 语气习惯 + 历史读音
```

### EVENTS.md 格式示例

```markdown
# {TARGET} 生平事件

## 乌台诗案（1079年）
**类型：** 政治打击
**阶段：** 京城时期 → 黄州时期
**核心事实：**
- {事实1}
- {事实2}
**情感冲击：** {描述}
**文学产出：** {篇名}、《{篇名}》
**对话引用：** "乌台那一遭……"

## 黄州躬耕（1080-1084年）
**类型：** 贬谪流放 + 生活转折
**核心事实：**
- {事实1}
- {事实2}
**情感基调：** {豁达自嘲}
**文学产出：** {篇名}

## 回京与再贬（1086-1094年）
**类型：** 起落反复
...

## 晚年流放（1094-1101年）
**类型：** 最终贬谪
...
```

---

## 六、技术路径（分阶段）

```
阶段一（当前）：Distiller Pipeline
├── EXECUTION_LOGIC.md ✅
├── DONE.md ✅
├── backlog.md ✅
└── 待补充：Stage 3.6 Voice Profile + EVENTS.md 生成

阶段二：Conversation Agent
├── Persona Loader（加载任意 SKILL.md）
├── Memory（对话历史）
├── Event Graph（事件检索）
└── System Prompt 模板

阶段三：Voice Integration
├── VOICE.md（Voice Profile 提取）
├── TTS 引擎适配（MiniMax / OpenAI / Azure）
└── 语音合成测试 + 调参

阶段四：Multi-Agent Orchestration
├── 人物切换（同时加载多个 persona？）
├── 群聊模式（苏轼+黄庭坚对谈？）
└── 角色扮演评估（persona 还原度打分）
```

---

## 七、OpenClaw 调度补充规则

Pipeline 补充两个新增的蒸馏任务：

### Stage 3.6 自动执行

```
在 Stage 3.5（一致性校验）完成后，
自动执行 Stage 3.6 Voice Profile 蒸馏。
输出 processed/{TARGET}/dimension_voice_profile.json。
```

### Stage 4.7 EVENTS.md 生成

```
在 Persona Card 生成阶段，
自动从 processed/{TARGET}/stages.md 和 dimension_思想内核.json 中，
提取事件信息，生成 output/{TARGET}/EVENTS.md。

生成逻辑：
1. 从 stages.md 中提取每个阶段的核心事件
2. 从 dimension_思想内核.json 中提取有情感意义的事件
3. 为每个事件标注 speech_tone_in_this_event
4. 合并所有事件，按年份排序
```
