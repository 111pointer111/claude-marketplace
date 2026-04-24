---
name: horror-narrator
description: >
  恐怖故事视频创作工坊 — 把任意恐怖故事变成1分钟视频。帧帧有画，句句有声。
  提供恐怖叙事技巧、画风规范、配音节奏、BGM设计等全套创作规则，
  并通过 MiniMax mmx CLI 执行：搜故事→拆帧→生图→配音→配乐。
  触发词：恐怖故事视频，鬼故事制作，灵异视频，有声鬼故事，恐怖插画视频。
type: skill
user-invocable: true
argument-hint: '[<故事主题或已有故事文本>]'
---

# Horror Narrator — 恐怖故事视频创作工坊

把任意恐怖故事变成一段约 60 秒的视频：6 帧画面 + 6 段旁白 + 1 段氛围 BGM。

**本 skill 是一套创作系统，不生成故事本身。** 故事由用户直接提供，或由 skill 从网上搜索改编。
skill 负责：拆帧技巧、旁白编写、插画规范、配音节奏、BGM 设计、执行生成。

---

## 创作目标

| 元素 | 时长 | 说明 |
|------|------|------|
| 每帧旁白 | 8-10 秒 | 65-80 中文字符，speed 0.85 |
| 总旁白 | ~54 秒 | 6 帧 |
| BGM | 全程 | 恐怖氛围背景音乐 |
| **总时长** | **~60 秒** | |

---

## 环境检查

每次加载 skill 按顺序检查：

1. mmx CLI 是否安装：`command -v mmx && mmx --version || echo "mmx_not_found"`
2. mmx 是否已认证：`mmx quota show --output json --quiet 2>/dev/null || echo "mmx_not_authed"`

| 状态 | 动作 |
|------|------|
| 未安装 | `npm install -g mmx-cli` |
| 未认证 | `mmx auth login --api-key <你的 Key>` |
| 认证失败 | https://platform.minimaxi.com/user-center/basic-information/interface-key |
| 就绪 | 继续流程 |

---

# 第一部分：创作规则手册

> 以下规则是恐怖内容创作的核心理论，适用于所有恐怖故事视频。

---

## 规则 1：60 秒恐怖内容的叙事结构

60 秒必须讲完一个完整故事。用 **6 帧叙事弧线**：

```
帧1 铺垫 → 帧2 异兆 → 帧3 加剧 → 帧4 高潮 → 帧5 反转 → 帧6 收尾
```

**每帧只做一件事：**

| 帧 | 任务 | 禁忌 |
|----|------|------|
| 铺垫 | 建世界、让主角可信 | 不要上来就恐怖，太平无事才衬得出后面的恐怖 |
| 异兆 | 第一次不对劲 | 不要明说是鬼，让观众隐约感觉有问题 |
| 加剧 | 更多异常，恐惧积累 | 不要直接给答案，保持悬念 |
| 高潮 | 最恐怖的时刻 | 克制比直白更有效——声音/影子/痕迹 > 完整显形 |
| 反转 | 意外转折 | 反转要有逻辑支撑，不能为反转而反转 |
| 收尾 | 细思极恐 | 不要说完，用余韵让人睡不着 |

---

## 规则 2：旁白（Narration）的写作技巧

旁白是恐怖视频的灵魂。画面配合声音，声音带动情绪。

### 2.1 长度控制

- **每帧 65-80 中文字符**（不含标点）
- 超过 80 字：TTS 语速被迫加快，恐怖感消失
- 低于 65 字：内容太薄，撑不起 8-10 秒

### 2.2 五感写作法

不要只写"看到"什么。恐怖内容要让观众**身临其境**：

| 感官 | 示例 | 效果 |
|------|------|------|
| 视觉 | "镜子里，那个影子比他慢了半拍" | 最直接的恐怖触发 |
| 听觉 | "身后传来脚步声，但回头时，空无一人" | 想象比看见更恐怖 |
| 触觉 | "后背一阵阴冷，像是有人站在三步之外" | 身体本能恐惧 |
| 嗅觉 | "空气里弥漫着腐朽的甜腻气味" | 潜意识恐怖触发 |
| 第六感 | "他本能地停下脚步——没有理由，但他就是不敢再往前" | 原始恐惧 |

### 2.3 句式节奏

- **铺垫帧**：陈述句为主，舒缓，留白，营造假象平静
- **异兆帧**：疑问句或省略句，"似乎……""好像……"，制造不确定感
- **加剧帧**：短句增多，节奏加快，"突然……""然后……"，制造压迫感
- **高潮帧**：极短的片段，词与词之间留停顿，"它……转过头来……"
- **反转帧**：突然换视角或揭示真相，用"原来……""其实……"
- **收尾帧**：开放式或留白，"他再也没有……"（不说完）

### 2.4 避免平铺直叙

❌ 差："他走进老宅，发现有鬼。"
✅ 好："他推开那扇门，屋里空荡荡的。角落里，一杯茶还在冒着热气——但这里已经废弃了二十年。"

**核心原则**：旁白要"展示"（show），不要"告知"（tell）。告诉观众有鬼，恐怖感减半；让观众自己推断有鬼，恐怖感翻倍。

### 2.5 主角名字的使用

- 铺垫帧、异兆帧、加剧帧中**必须出现主角名字**（建立代入感）
- 高潮帧、反转帧、收尾帧**可以省略名字**（制造疏离感，增强恐怖）
- 名字通常是 2-3 个字，符合故事时代背景（书生/旅人/女孩/阿贵）

### 2.6 旁白 → 插画的对应关系

旁白描述的内容必须能在插画中**视觉化呈现**。每写完一段旁白，问自己：
- "这句话的画面感是什么？"
- "观众看到这张图，能不能不靠旁白就猜到发生了什么？"

---

## 规则 3：视觉风格规范

### 3.1 画风预设

| 风格 | 英文关键词 | 适用类型 |
|------|-----------|---------|
| **暗黑国风**（默认） | `dark Chinese ink painting, eerie traditional atmosphere, fog, temple, ancient Chinese horror` | 民间志怪、聊斋、老宅 |
| **哥特西式** | `gothic horror, Victorian mansion, candlelight, dark fantasy, oil painting style` | 洋房、吸血鬼、古堡 |
| **现代都市** | `cinematic horror, dim neon, modern apartment, urban legend, photorealistic, rain` | 都市怪谈、深夜电梯 |
| **像素复古** | `pixel art, 16-bit horror game, dark dungeon, retro game aesthetic, eerie` | 复古恐怖、游戏感 |

### 3.2 插画 Prompt 公式

所有插画 prompt 必须遵循以下结构：

```
dark, [STYLE_KEYWORDS], [SCENE_SPECIFIC_DESCRIPTION],
[EMOTION/ATMOSPHERE], [LIGHTING], cinematic composition, high detail
```

示例（暗黑国风，第 4 帧高潮）：

```
dark, Chinese ink painting style, eerie traditional atmosphere, foggy night,
abandoned temple interior, red-robed female ghost descending from the ceiling,
long black hair covering face, flickering candle light, terrified lone traveler,
horror atmosphere, dramatic lighting, cinematic composition, high detail
```

### 3.3 插画风格注意事项

- **始终以 `dark` 开头**（MiniMax 图片模型对 dark 关键词响应最好）
- 包含**情绪词**（terrified/uneasy/horror/suspense）引导氛围
- **不要在 prompt 里写"血"**（gore/blood）——触发内容过滤且降低美学质量
- **避免全黑画面**——至少要有一点光源（烛光/月光/霓虹）让场景可辨识
- 暗黑国风优先用 `fog` / `lantern` / `traditional architecture`
- 现代都市优先用 `rain` / `neon` / `film grain`

### 3.4 各帧画面设计要点

| 帧 | 画面重点 | 构图建议 |
|----|---------|---------|
| 铺垫 | 交代场景，建立可信环境 | 广角，平静构图，留白 |
| 异兆 | 轻微异常，要细看才能发现 | 构图略微失衡，引导线指向异常处 |
| 加剧 | 明确的不对劲 | 俯视/仰视角度增加压迫感 |
| 高潮 | 恐怖来源核心画面 | 中心构图，光源在恐怖存在身后（逆光），或完全黑暗中的两点光 |
| 反转 | 揭示真相的关键画面 | 视角转换，揭示观众不知道的视角 |
| 收尾 | 余韵画面，空镜或悬念 | 留白多，暗示故事未完 |

---

## 规则 4：配音设计

### 4.1 恐怖配音三要素

| 要素 | 设置 | 效果 |
|------|------|------|
| **语速** | 正常或略慢（0.9-1.0） | 不要低于 0.9，会太拖 |
| **音调** | 偏低（pitch -1 ~ -2） | 低沉 = 沙哑 = 古老/来自黑暗 |
| **情绪** | 根据帧的阶段 | 从平静→疑问→恐惧→最压抑→突变→余韵 |

### 4.2 帧级配音参数

| 帧 | speed | pitch | 语气 |
|----|-------|-------|------|
| 1 铺垫 | 1.0 | 0 | 正常语速，像在叙述 |
| 2 异兆 | 1.0 | 0 | 正常，稍有疑问感 |
| 3 加剧 | 0.95 | -1 | 轻微紧张，压低声调 |
| 4 高潮 | 0.9 | -2 | 缓慢，压抑 |
| 5 反转 | 0.9 | -2 | 揭示真相，节奏稳定 |
| 6 收尾 | 0.95 | -1 | 余韵，留白感 |

### 4.3 配音音色选择

| 音色 | 适用场景 | 说明 |
|------|---------|------|
| `Chinese_expressive_narrator`（默认） | 所有类型 | 情感丰富，适合恐怖叙述 |
| 沙哑男声 | 民间志怪 | 古老感，像老人讲故事 |
| 空灵女声 | 诡异氛围 | 都市怪谈，有飘渺感 |
| 冷静男声 | 反差恐怖 | 越平静越恐怖，越慢越压抑 |

先查询可用音色：
```bash
mmx speech list-voices | head -50
```

---

## 规则 5：背景音乐设计

### 5.1 BGM 的功能层次

恐怖 BGM 不是一首曲子，而是**三层声音叠加**：

| 层次 | 内容 | 特点 |
|------|------|------|
| **底层** | 低频嗡鸣/持续低音 | 制造持续的不安感，人耳几乎不感知但身体能感受 |
| **中层** | 弦乐/钢琴/环境音 | 旋律或和声，随剧情起伏 |
| **顶层** | 特殊音效 | 脚步声、风声、远处低语、时钟滴答 |

### 5.2 BGM prompt 公式

```
[底层音色], [中层音色], [顶层音效], [节奏], [情绪], no lyrics, cinematic horror score
```

示例：
```
low drone, slow cello, distant whispers, wind howling, tension building,
eerie atmosphere, no lyrics, cinematic horror score, 60 seconds
```

### 5.3 BGM 与帧的对应

60 秒 BGM 建议分段落：

| 时段 | 对应帧 | 音乐状态 |
|------|--------|---------|
| 0-10s | 铺垫 | 极轻，几乎只有低频嗡鸣 |
| 10-20s | 异兆 | 弦乐开始，节奏极慢 |
| 20-35s | 加剧+高潮 | 低频增强，节奏加快，突然的静默（比声音更恐怖） |
| 35-50s | 反转 | 旋律突变，调性转换 |
| 50-60s | 收尾 | 回归低频，留白，没有完整的结束感 |

### 5.4 声音静默的力量

**最恐怖的时刻，往往是声音消失的那一秒。** 在高潮帧之后、反转帧开始前，可以考虑生成一段 1-2 秒的纯静默BGM片段，然后在反转帧突然爆发。不要让 BGM 从头到尾一直响。

---

## 规则 6：恐怖内容吸引力的底层逻辑

### 6.1 恐怖的两条路径

| 类型 | 机制 | 示例 |
|------|------|------|
| **Jump Scare** | 瞬间惊吓，肾上腺素激增 | 突然出现的鬼脸 |
| **Slow Burn** | 逐渐积累的不安感，事后回想更恐怖 | 镜子里慢半拍的倒影 |

**推荐走 Slow Burn 路线**——Jump Scare 只能吓人一次，Slow Burn 能让人睡不着。

### 6.2 恐怖内容的 6 大吸引力机制

1. **熟悉中的陌生**："这是我家，但不是我记忆中的样子"——安全感被打破
2. **不可名状的恐惧**："那个东西不是鬼，不是人，是……"——想象比已知更恐怖
3. **时间错位**："二十年前的照片里，有今天在场的人"——不合理的存在
4. **循环宿命**："他以为自己逃出来了，但……"——无法逃脱的宿命感
5. **旁观者视角**："他看到的，和我们看到的是同一件事吗"——视角欺骗
6. **细思极恐**："结尾了，但观众开始想：如果是我……"——代入后的恐惧

### 6.3 观众为什么会在 60 秒内看完

| 时间点 | 观众的期待 | 创作者的任务 |
|--------|-----------|------------|
| 0-5s | 这故事值不值得看 | 铺垫帧要设置"钩子"——一个奇怪但不解释的问题 |
| 5-20s | 会发生什么 | 异兆帧持续给线索，吊胃口 |
| 20-40s | 高潮够不够恐怖 | 高潮帧是核心，要克制但有力 |
| 40-55s | 反转够不够意外 | 反转帧要打破观众预期 |
| 55-60s | 值不值得分享 | 收尾帧要有"我也想吓别人"的冲动 |

**开场钩子技巧**（第 1 帧旁白结尾）：
- "那是我最后一次见到阿贵——或者说，最后一次见到看起来像阿贵的人。"
- "那栋楼没有第十三层。但我确实按了。"
- "如果你在深夜听到有人在洗手间哭泣，记住：不要回应。"

### 6.4 中式恐怖的独特美学

中式恐怖有别于西方血腥恐怖的核心：**文化禁忌 + 日常熟悉感**。

| 西方恐怖 | 中式恐怖 |
|---------|---------|
| 血腥、暴力、怪物 | 日常物件（镜子/照片/灯笼）承载诅咒 |
| 直面怪物 | 怪物不直接露面，通过痕迹表现 |
| 物理伤害 | 精神侵蚀、宿命、无法逃脱 |
| 个人英雄逃脱 | "善恶有报"的道德恐怖，或无解的宿命 |
| 明确的怪物形象 | "红衣女鬼""纸人""枯井冤魂"的民间想象 |

**推荐用中式恐怖路线**——暗黑国风的视觉 + 民间志怪的故事 + 文化禁忌的设定，是当前内容市场最受欢迎的组合。

---

## 规则 7：故事来源与改编

### 7.1 故事来源优先级

| 优先级 | 来源 | 说明 |
|--------|------|------|
| 1 | 用户直接提供 | 质量最可控，直接跳 Step 1 |
| 2 | 网络搜索改编 | 用 `mmx search` 搜民间故事，AI 改写 |
| 3 | 经典故事重述 | 聊斋、目游、民间传说改写（注意版权边界）|

### 7.2 搜索改编流程

```bash
mmx search query --q "<关键词> 恐怖故事 民间 灵异 惊悚" --output json --quiet
```

找到素材后：
1. 提取核心恐怖元素（什么在吓人？为什么吓人？）
2. 保留核心，压缩/改写叙事结构适配 6 帧格式
3. 角色名和细节按需调整

### 7.3 故事筛选标准

好的恐怖故事素材具备：
- **一个核心恐怖点**（一个核心恐惧，贯穿全篇）
- **可视觉化的场景**（能画出画面）
- **有反转或悬念空间**（不是一眼看到头）
- **60 秒内可讲完**（情节不要太复杂）

---

# 第二部分：执行流程

> 规则手册到此结束。以下是执行流水线。

---

## 流程总览

```
Step 0: 输入故事
Step 1: 解析故事 → 拆成 6 帧（含旁白编写）
Step 2: 编写插画 prompt
Step 3: 确认脚本（用户审核）
Step 4: 并行生成画面 + 配音
Step 5: 生成 BGM
Step 6: 展示成果
Step 7: 播放 & 反馈
```

---

## Step 0：输入故事

**方式 1：用户提供故事文本**
直接粘贴完整故事 → 进入 Step 1

**方式 2：用户提供主题，skill 搜索改编**
用户给关键词（如"深夜电梯恐怖故事"）→ skill 搜索 → 改编 → 进入 Step 1

**方式 3：用户给模糊需求**
"随便来一个恐怖故事" → skill 随机选择类型+场景+角色 → 搜索改编 → 进入 Step 1

---

## Step 1：解析故事 → 6 帧结构

将故事拆成 6 帧，每帧包含：
- **帧标题**（2-4 字）
- **旁白文本**（65-80 中文字符，按规则 2 技巧编写）
- **画面描述**（插画 prompt 的核心内容）

**拆帧方法**：
1. 找到故事的**核心恐怖点**（是什么在吓人？）
2. 找到故事的**反转点**（哪里出人意料？）
3. 分配到 6 帧中：铺垫 → 异兆 → 加剧 → 高潮 → 反转 → 收尾
4. 用**五感写作法**改写旁白
5. 为主角取一个符合故事背景的名字（2-3 字）

**输出格式**：

```
《故事标题》

【第1帧 — 铺垫】入宅
旁白："王生推开那扇老宅的木门，院子里杂草丛生。二十年前这里还是镇上最气派的宅子，如今只剩下他和房东两个人。"

【第2帧 — 异兆】旧照
旁白："客厅的墙上挂着一张老照片。他凑近看——照片里的女人穿着红嫁衣，但她的脸……被人刮花了。"

【第3帧 — 加剧】回声
旁白："楼上传来脚步声。他抬头，天花板的灰尘簌簌落下。脚步声越来越近，越来越近——然后，突然停了。"

【第4帧 — 高潮】现身
旁白："他转身。一个红衣身影就站在他身后，近到能闻到腐朽的气息。她慢慢抬起头——"

【第5帧 — 反转】旧照
旁白："他猛然想起房东说的那句话：'这宅子里的女人，二十年前穿着红嫁衣上吊死了。'他低头看向那张照片——照片里，刮花的脸，正是他自己。"

【第6帧 — 收尾】空宅
旁白："第二天，村里的人推开了这扇门。院子里空无一人，只有墙上那张老照片，又多了一张新的面孔。"
```

---

## Step 2：编写插画 Prompt

为每帧旁白编写英文插画 prompt（按规则 3）。

Prompt 结构：`dark, [STYLE], [SCENE], [EMOTION], [LIGHTING], cinematic, high detail`

**示例（暗黑国风，第 4 帧）**：
```
dark, Chinese ink painting style, eerie traditional atmosphere,
abandoned mansion interior, red-robed female ghost standing inches from a terrified man,
long flowing red dress, pale ghostly face, flickering candlelight,
horror atmosphere, dramatic low-angle lighting, cinematic composition, high detail
```

---

## Step 3：确认脚本

展示完整的 6 帧脚本（旁白 + 画面 prompt）供用户确认：

```
故事标题：xxx
类型：xxx | 风格：xxx

第1帧 — 铺垫
  旁白："xxx"
  画面：xxx（英文 prompt）

第2帧 — 异兆
  ...

确认后开始生成？
```

用户可选择：
1. 开讲！（确认 → Step 4）
2. 修改第 X 帧旁白
3. 换故事/换风格

---

## Step 4：并行生成画面 + 配音

脚本确认后，**6 帧画面和 6 段配音同时并行生成**。

### 4.1 插图生成（并行）

```bash
mmx image generate \
  --prompt "<frame_N_illustration_prompt>" \
  --aspect-ratio 16:9 \
  --out-dir <OUTPUT_DIR>/frames \
  --out-prefix "frame_<N>" \
  --quiet
```

- 输出：`frame_01.png` ~ `frame_06.png`
- prompt 必须英文，以 `dark,` 开头

### 4.2 配音生成（并行）

```bash
mmx speech synthesize \
  --text "<narration>" \
  --voice <voice_id> \
  --model speech-2.8-hd \
  --speed <speed_from_frame_table> \
  --pitch <pitch_from_frame_table> \
  --format mp3 \
  --out <OUTPUT_DIR>/audio/frame_<N>.mp3 \
  --quiet
```

**帧级参数**（自然语速优先，pitch 控制恐怖感）：

| 帧 | speed | pitch | 说明 |
|----|-------|-------|------|
| 1 | 1.0 | 0 | 正常语速，像在叙述 |
| 2 | 1.0 | 0 | 正常，稍有疑问感 |
| 3 | 0.95 | -1 | 轻微紧张，压低声调 |
| 4 | 0.9 | -2 | 缓慢，压抑 |
| 5 | 0.9 | -2 | 揭示真相，节奏稳定 |
| 6 | 0.95 | -1 | 余韵，留白感 |

**原则**：speed 不低于 0.9，pitch 控制恐怖感

**进度展示**：
```
正在生成...
[██████░░░░] 画面 4/6
[████░░░░░░] 配音 3/6
```

---

## Step 5：生成 BGM

```bash
mmx music generate \
  --prompt "low drone, slow cello, distant whispers, wind howling,
    tension building, eerie atmosphere, no lyrics,
    cinematic horror score, 60 seconds" \
  --mood "terrifying, suspenseful" \
  --genre "horror ambient, dark cinematic" \
  --instrumental \
  --out <OUTPUT_DIR>/audio/bgm.mp3 \
  --quiet
```

---

## Step 6：展示成果

```
✨ 恐怖故事视频已合成！

《故事标题》
类型：xxx | 风格：xxx
📁 保存位置：<OUTPUT_DIR>/<SLUG>.mp4
总时长：xxx秒

画面（6帧）：
  frame_01_001.jpg — 铺垫
  frame_02_001.jpg — 异兆
  frame_03_001.jpg — 加剧
  frame_04_001.jpg — 高潮
  frame_05_001.jpg — 反转
  frame_06_001.jpg — 收尾

音频（7段）：
  frame_01.mp3 ~ frame_06.mp3（旁白）
  bgm.mp3（背景音乐，已与旁白混音）

最终成品：<SLUG>.mp4（可直接发布）
```

---

## Step 6b：ffmpeg 合成视频

ffmpeg 将帧图片、配音、BGM 合成为一段完整 MP4 视频。**三步完成，无需剪辑软件。**

### 前置条件

```bash
command -v ffmpeg || brew install ffmpeg
```

### 完整合成命令

在 `OUTPUT_DIR`（含 `frames/` 和 `audio/` 子目录）下执行：

```bash
cd <OUTPUT_DIR>

# Step 1：生成每帧的视频片段（图片 + 该帧配音）
for i in 1 2 3 4 5 6; do
  dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 audio/frame_0${i}.mp3)
  ffmpeg -loop 1 -i frames/frame_0${i}_001.jpg -i audio/frame_0${i}.mp3 \
    -t ${dur} \
    -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2" \
    -pix_fmt yuv420p -c:v libx264 -preset fast -r 30 \
    -c:a aac -b:a 192k -shortest \
    -y segment_0${i}.mp4
done

# Step 2：拼接所有视频片段
cat > concat.txt << 'EOF'
file 'segment_01.mp4'
file 'segment_02.mp4'
file 'segment_03.mp4'
file 'segment_04.mp4'
file 'segment_05.mp4'
file 'segment_06.mp4'
EOF
ffmpeg -f concat -safe 0 -i concat.txt -c copy concat_raw.mp4

# Step 3：拼接所有配音
cat > audio/narration_list.txt << 'EOF'
file 'frame_01.mp3'
file 'frame_02.mp3'
file 'frame_03.mp3'
file 'frame_04.mp3'
file 'frame_05.mp3'
file 'frame_06.mp3'
EOF
ffmpeg -f concat -safe 0 -i audio/narration_list.txt -c copy audio/narration_all.mp3

# Step 4：裁 BGM 到视频时长，加淡入淡出，音量压到 30%
video_dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 concat_raw.mp4)
fade_start=$(echo "$video_dur - 5" | bc)
ffmpeg -i audio/bgm.mp3 -t ${video_dur} \
  -af "volume=0.3,afade=t=in:st=0:d=2,afade=t=out:st=${fade_start}:d=5" \
  -ar 44100 -ac 2 -c:a aac -b:a 128k /tmp/bgm_std.aac

# Step 5：标准化配音（统一采样率和声道）
ffmpeg -i audio/narration_all.mp3 -ar 44100 -ac 2 -c:a aac -b:a 128k /tmp/narration_std.aac

# Step 6：混音（配音为主 + BGM 为辅，权重 1:0.3）
ffmpeg -i /tmp/narration_std.aac -i /tmp/bgm_std.aac \
  -filter_complex "[0:a]volume=1.0[na];[1:a]volume=0.3[ba];[na][ba]amix=inputs=2:duration=first:weights=1 0.3:normalize=0[m]" \
  -map "[m]" -ar 44100 -c:a aac -b:a 192k /tmp/mixed.aac

# Step 7：合并视频（无音）+ 混音音频 → 最终成品
ffmpeg -i concat_raw.mp4 -i /tmp/mixed.aac \
  -map 0:v -map 1:a \
  -c:v copy -c:a aac -b:a 192k -shortest \
  -y <SLUG>.mp4
```

**注意**：
- `stream_loop -1` 在 filter_complex 里会导致卡死，**不要用**
- 配音和 BGM 必须先标准化（采样率/声道统一）再混音
- 中间文件放 `/tmp` 避免覆盖问题
- 最终成品自动打开：`open <SLUG>.mp4`

### 命令详解

| 步骤 | 关键命令 | 作用 |
|------|---------|------|
| 1 | `ffprobe -show_entries format=duration` | 读取每段配音的实际时长 |
| 1 | `ffmpeg -loop 1 -i image.jpg -i audio.mp3 -t ${dur} ... -shortest` | 图片持续整段配音时长 |
| 1 | `-vf "scale=...force_original_aspect_ratio=decrease,pad=...:(ow-iw)/2:(oh-ih)/2"` | 将任意比例图片填充为 1920×1080 |
| 1 | `-r 30` | 输出 30fps 视频 |
| 2 | `ffmpeg -f concat -c copy` | 无重新编码拼接，速度快 |
| 3 | `ffmpeg -f concat -c copy` | 拼接所有配音为一条音频 |
| 4 | `ffmpeg -t ${video_dur} -af "volume=0.3,afade=in,afade=out"` | 裁 BGM 到视频时长，加淡入淡出，音量 30% |
| 4 | `-ar 44100 -ac 2` | BGM 重采样为 44.1kHz 立体声 |
| 5 | `ffmpeg -ar 44100 -ac 2` | 配音标准化（统一采样率和声道） |
| 6 | `amix=inputs=2:weights=1 0.3:normalize=0` | 配音(权重1) + BGM(权重0.3) 混音 |
| 7 | `-map 0:v -map 1:a` | 精确指定：视频流+混音音频流合并 |

### 参数调整说明

| 参数 | 调整方法 |
|------|---------|
| **视频分辨率** | 将 `1920:1080` 改为 `1080:1920`（竖屏 9:16）或 `1280:720`（720p） |
| **BGM 音量** | 将 `0.3` 改为 `0.2`（更轻）或 `0.4`（更重） |
| **ffmpeg 编码速度** | 将 `preset fast` 改为 `preset slow`（更小文件）或 `preset ultrafast`（最快） |
| **视频质量** | 将 `-preset fast -b:v 0` 改为 `-preset slow -b:v 3000k`（固定码率 3Mbps） |
| **帧率** | 将 `30` 改为 `24`（电影感）或 `60`（更流畅） |

### 输出文件

合成完成后输出 `<SLUG>.mp4`，即为最终恐怖故事视频。**自动打开播放**：

```bash
open <OUTPUT_DIR>/<SLUG>.mp4
```

---

## Step 7：播放 & 反馈

合成完成后，直接播放最终成品 `<SLUG>.mp4`：

```bash
open <OUTPUT_DIR>/<SLUG>.mp4
```

或用 ffplay 播放：
```bash
ffplay <OUTPUT_DIR>/<SLUG>.mp4
```

**播放后选项**：
```
还想做什么？
  1. 🔄 重新生成第 X 帧（指定帧号）
  2. 🔄 重新生成第 X 帧配音
  3. 🎵 换个 BGM
  4. 🎬 换个旁白文字后重新配音
  5. 📖 另一个恐怖故事
```

---

## 输出目录结构

```
~/Music/minimax-gen/horror-narrator/<TIMESTAMP>_<slug>/
├── script.txt              # 6帧脚本（旁白 + prompt）
├── frames/
│   ├── frame_01_001.jpg
│   ├── frame_02_001.jpg
│   ├── frame_03_001.jpg
│   ├── frame_04_001.jpg
│   ├── frame_05_001.jpg
│   └── frame_06_001.jpg
├── audio/
│   ├── frame_01.mp3
│   ├── frame_02.mp3
│   ├── frame_03.mp3
│   ├── frame_04.mp3
│   ├── frame_05.mp3
│   ├── frame_06.mp3
│   └── bgm.mp3
├── segment_01.mp4 ~ segment_06.mp4  # 中间产物（Step 6b Step 1 产出）
├── concat.txt                            # 中间产物（Step 6b Step 2 产出）
├── concat_raw.mp4                        # 中间产物（Step 6b Step 2 产出）
└── <SLUG>.mp4                            # 最终成品（Step 6b Step 3 产出）
```

---

## Step 8：发布到小红书（可选）

使用 `social-auto-upload` 项目的 `sau` CLI，通过 Playwright 浏览器自动化上传视频到小红书。

### 8.1 安装依赖

**安装 social-auto-upload**（只需执行一次）：

```bash
git clone https://github.com/dreammis/social-auto-upload.git
cd social-auto-upload
uv pip install -e .
```

**安装 patchright Chromium**（只需执行一次）：

```bash
PLAYWRIGHT_DOWNLOAD_HOST="https://npmmirror.com/mirrors/playwright" patchright install chromium
```

### 8.2 登录小红书（只需执行一次，之后 cookie 持久化）

```bash
sau xiaohongshu login --account <你的账号名>
# 例如：sau xiaohongshu login --account horror_story
```

首次运行会弹出浏览器窗口，用小红书 App 扫码登录。登录后 cookie 自动保存。

### 8.3 检查登录状态

```bash
sau xiaohongshu check --account <你的账号名>
# 输出 valid = cookie 有效；invalid = 需要重新登录
```

### 8.4 上传视频

```bash
sau xiaohongshu upload-video \
  --account <你的账号名> \
  --file <OUTPUT_DIR>/<SLUG>.mp4 \
  --title "<故事标题>" \
  --desc "<故事简介，1-2句话>" \
  --tags <标签1>,<标签2>,<标签3> \
  [--thumbnail <封面图>] \
  [--headless | --headed]
```

**参数说明**：

| 参数 | 必填 | 说明 |
|------|------|------|
| `--account` | 是 | 登录时指定的账号名 |
| `--file` | 是 | 视频文件路径 |
| `--title` | 是 | 视频标题，≤20字 |
| `--desc` | 否 | 视频描述，正文内容 |
| `--tags` | 否 | 标签，逗号分隔，如 `恐怖故事,民间志怪,深夜电台` |
| `--thumbnail` | 否 | 封面图，建议用高潮帧 frame_04 |
| `--schedule` | 否 | 定时发布，格式 `YYYY-MM-DD HH:MM` |
| `--headless` | 否 | 无头模式（不弹浏览器窗口） |
| `--headed` | 否 | 有头模式（显示浏览器，可调试） |

**小红书发布建议**：
- 标题：悬念式，如「深夜路过这片坟地后，他再也没能回家」
- 标签：`恐怖故事` `民间灵异` `吓人` `深夜故事` `惊魂`
- 封面：用高潮帧 frame_04（最恐怖的画面），或 frame_06（余韵画面）

### 8.5 自动化工作流

如果已安装并登录，整个发布流程可以自动化：

```bash
# 1. 检查 cookie
status=$(sau xiaohongshu check --account <账号> --output json | jq -r '.status')
if [ "$status" != "valid" ]; then
  sau xiaohongshu login --account <账号> --headed
fi

# 2. 上传视频
sau xiaohongshu upload-video \
  --account <账号> \
  --file <OUTPUT_DIR>/<SLUG>.mp4 \
  --title "<标题>" \
  --desc "<描述>" \
  --tags "恐怖故事,民间灵异,深夜故事" \
  --thumbnail <OUTPUT_DIR>/frames/frame_04_001.jpg \
  --headless
```

### 8.6 定时发布

设置未来某个时间自动发布：

```bash
sau xiaohongshu upload-video \
  --account <账号> \
  --file <OUTPUT_DIR>/<SLUG>.mp4 \
  --title "<标题>" \
  --schedule "2026-04-25 21:00"
```

---

## 错误处理

| 错误 | 处理 |
|------|------|
| mmx 未安装 | 提示 `npm install -g mmx-cli` |
| mmx 未认证 | 提示 `mmx auth login` |
| 插图生成失败 | 报告失败帧号，用户重试或跳过 |
| 配音生成失败 | 报告失败帧号，用户重试或跳过 |
| BGM 生成失败 | 跳过 BGM，继续流程 |
| ffmpeg 缺失 | `brew install ffmpeg`（macOS）或 `apt install ffmpeg`（Linux） |
| sau 未安装 | 提示安装 social-auto-upload（见 Step 8.1） |
| 小红书 cookie 无效 | `sau xiaohongshu login --account <账号> --headed` 重新扫码登录 |
| 网络错误 | 重试一次，失败则报告详情 |

---

## 重要规则

1. **规则第一**：执行前先读规则手册，不确定时按规则来
2. **旁白是灵魂**：插画和 BGM 是辅助，旁白是核心——先写好旁白，再生成画面
3. **自然节奏优先**：旁白长度由内容自然决定，不硬卡时长；每帧 8-30 秒均可
4. **并行生成**：6 帧画面 + 6 段配音同时生成，不串行
5. **prompt 必须英文**：英文生成质量显著优于中文
6. **五感写作**：旁白要调动了/听/触/嗅/第六感，不只是"看到"
7. **克制的高潮**：声音/影子/痕迹 > 完整显形；想象比已知更恐怖
8. **开场钩子**：第 1 帧旁白结尾要留悬念，让人想继续看
9. **中式恐怖优先**：暗黑国风 + 民间志怪 + 文化禁忌是市场最喜欢的组合
10. **本地存储**：`~/Music/minimax-gen/horror-narrator/`
11. **mmx agent flags**：所有 mmx 命令必须加 `--quiet --non-interactive`
12. **ffmpeg 合成**：生成完素材后自动执行 ffmpeg 合成，无需用户手动操作
13. **小红书发布**：视频生成完成后主动询问用户是否发布到小红书，用 sau CLI 自动上传
