# MiniMax — CodingPlan 全模态能力包

MiniMax 全模态 AI 能力包，所有多模态能力（语音合成、音色克隆、音色设计、音乐生成、视频生成、图片生成）统一通过 MiniMax MCP 调用。

## 一键配置

```bash
# 1. 复制环境变量模板
cp skills/.env.example skills/.env

# 2. 编辑 skills/.env，填入你的 API Key
# MINIMAX_API_KEY=你的API_KEY

# 3. MCP 自动安装（如未安装），Agent 会引导你完成
```

## MCP 工具一览

| 工具 | 功能 |
|------|------|
| `text_to_audio` | 文本转语音，多音色 + 情绪控制 |
| `list_voices` | 查询所有可用音色 |
| `voice_clone` | 克隆音色（上传音频文件） |
| `voice_design` | AI 生成全新音色 |
| `play_audio` | 播放音频 |
| `music_generation` | 生成音乐，支持歌词 + 旋律描述 |
| `generate_video` | 文生视频 / 图生视频，多模型可选 |
| `image_to_video` | 图片转视频（仅 JS 版 MCP） |
| `query_video_generation` | 查询视频生成任务状态 |
| `text_to_image` | 图片生成，多宽高比 |

## 快速开始

直接告诉 Agent 你想做什么：

- **语音合成**：`/tts 你好，欢迎使用 MiniMax`
- **克隆音色**：上传音频文件，说"克隆这个音色"
- **生成音乐**：说"帮我生成一首欢快的流行音乐"
- **视频生成**：说"生成一个海边日落的视频"
- **图片生成**：说"画一只可爱的橘猫"

## 首次配置

1. 获取 API Key：https://platform.minimaxi.com/user-center/basic-information/interface-key
2. 编辑 `skills/.env`，填入 `MINIMAX_API_KEY`
3. 设置 `MINIMAX_MCP_BASE_PATH`（文件输出目录，如 `~/Desktop/MiniMax-Output`）
4. Agent 会自动检测并安装 MiniMax MCP

## 视频生成模型参考

| 模型 | 类型 | 分辨率 | 时长 |
|------|------|--------|------|
| MiniMax-Hailuo-02 | 文/图生视频 | 512P / 768P / 1080P | 6s / 10s |
| T2V-01-Director | 文生视频 | — | 6s |
| I2V-01-Director | 图生视频 | — | 6s |
| S2V-01 | 主体驱动 | — | 6s |

## 项目结构

```
minimax_model_skill/
├── SKILL.md      # 核心指令文件（MCP 工具 + REST API）
└── README.md     # 本文件
```
