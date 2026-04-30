---
name: minimax-music
description: MiniMax AI 音乐生成 Skill。支持根据不同音乐类型、风格、情绪生成带歌词歌曲或纯音乐，调用 `mmx music generate` 命令输出到本地目录。用于：用户要求"生成音乐"、"写首歌"、"制作BGM"、"每日音乐任务"等场景。
user-invocable: true
---

# MiniMax AI 音乐生成 Skill

## 核心方法论

### AI 音乐生成三大规律

1. **约束叠加 > 单一描述**：同时给 2-3 个相互制约的风格条件，AI 会做出更精确的创造性选择
2. **Hook-First**：先设计副歌记忆点（≤7字，具体画面），再倒推全曲结构
3. **迭代比一次到位更可靠**：固定 tempo+mood+song length，每次只改一个变量

### 歌词四轴法则

高质量歌词必须同时满足：**叙事性 + 意象性 + 韵律感 + 情感共鸣**
检查标准：有没有具体的时间/地点/人物/物品？有没有直接说"心痛/悲伤"？

### 克制原则

用具体物品和动作替代抽象情绪词：
- ❌ "我的心好痛" → ✅ "输入法还记得你的名字"
- ❌ "时间过得好快" → ✅ "校服领口松了两颗扣"

## 目录结构
```
skills/minimax-music/
├── SKILL.md
├── settings.example.yaml    # 配置模板
├── scripts/
│   └── music_generator.py
└── references/
    └── prompt_templates.md  # 完整方法论（必读）
```

## 快速开始

### 环境配置

1. 复制配置模板：
```bash
cp settings.example.yaml settings.yaml
```

2. 在 `settings.yaml` 中配置输出目录：
```yaml
OUTPUT_DIR: "/path/to/your/music/output"
```

3. 确保 `MINIMAX_API_KEY` 已设置在环境变量中（脚本从 `os.environ` 读取）

### 单首生成
```python
from scripts.music_generator import generate_music
import yaml

settings = yaml.safe_load(open("settings.yaml"))
result = generate_music(
    prompt="中文民谣，关于清晨便利店独自喝咖啡的场景...",
    lyrics="___LYRICS_OPTIMIZER___",
    vocals="沙哑男声，有岁月感，有呼吸感",
    genre="folk",
    mood="melancholic, warm",
    instruments="木吉他，指弹风格",
    tempo="moderate",
    structure="verse - verse - pre-chorus - chorus - bridge - chorus",
    avoid="'心痛' or '悲伤' or '眼泪', 情歌套路, 说教结尾",
    settings=settings,
)
```

### 每日三首
```python
from scripts.music_generator import generate_daily_music
results = generate_daily_music("/path/to/skills/minimax-music/")
```

## mmx music generate 核心参数

### 人声音乐（含 --lyrics-optimizer）
```bash
mmx music generate \
  --prompt "<场景+情绪描述，禁止项>" \
  --lyrics-optimizer \
  --vocals "<人声：音域+质感+每段落发声策略>" \
  --genre "<流派>" \
  --mood "<情绪>" \
  --structure "<verse-chorus-verse-chorus-bridge-chorus>" \
  --avoid "<具体要排除的元素>" \
  --out "/path/to/output.mp3"
```

### 器乐
```bash
mmx music generate \
  --prompt "<音色+层次+情绪曲线+场景描述>" \
  --instrumental \
  --genre "<流派>" \
  --mood "<情绪>" \
  --instruments "<乐器层次>" \
  --avoid "<不要的元素>" \
  --structure "<intro - main theme - ending>" \
  --out "/path/to/output.mp3"
```

### --vocals 写法模板

专业写法：**音域 + 音色质感 + 各段落发声策略**

```
--vocals "男高音 tenor，略带沙哑有力量感。
          主歌 chest voice 叙事，接近说话的语气；
          预副歌 mixed voice 慢慢叠加能量；
          副歌 strong belt 爆发，高音有穿透力；
          桥段 head voice 轻唱，脆弱感；
          尾副歌 belt 推到最高，最后长音 vibrato 收尾"
```

**核心原则**：主歌收 → 预副歌蓄 → 副歌放 → 桥段收 → 尾副歌最放

详见 `references/prompt_templates.md` — 完整声乐术语和模板

## 歌词禁止清单

必须禁止：
- 抽象情绪词：心痛、悲伤、难过、崩溃、绝望
- 陈词滥调：飞蛾扑火、遍体鳞伤、沧海桑田、海枯石烂
- 说教结尾：珍惜当下、把握今天、勇敢前行
- 过度煽情：直接哭喊、直接说"我爱你爱到死"

## 参考资料

完整方法论、意象库、prompt 模板、速查表：
→ `references/prompt_templates.md`

## 注意事项

- `mmx music generate` 超时 **300 秒**，耐心等待
- `--lyrics-optimizer` 的 prompt 必须包含**场景+禁止项**，不能太笼统
- API Key 从环境变量 `MINIMAX_API_KEY` 读取，**禁止硬编码**
- `--aigc-watermark` 推荐开启
- 歌词生成后对照**四轴法则**自检
- 每日生成建议**每次只改一个变量**迭代优化
