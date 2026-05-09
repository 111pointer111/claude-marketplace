# MiniMax — CodingPlan 全模态能力包（mmx CLI）

MiniMax 全模态 AI 能力包，所有多模态能力（语音合成、音乐生成、视频生成、图片生成）统一通过 `mmx` CLI 调用。

## 一键配置

```bash
# 1. 安装 mmx CLI
npm install -g mmx-cli

# 2. 复制环境变量模板
cp skills/.env.example skills/.env

# 3. 编辑 skills/.env，填入你的 API Key
# MINIMAX_API_KEY=你的API_KEY

# 4. 登录认证
mmx auth login --api-key <你的API_KEY>
```

## CLI 命令一览

| 命令 | 功能 |
|------|------|
| `mmx speech synthesize` | 文本转语音，多音色 + 情绪控制 |
| `mmx music generate` | 生成音乐，支持歌词 + 旋律描述 |
| `mmx video generate` | 文生视频 / 图生视频，多模型可选 |
| `mmx video task get` | 查询视频生成任务状态 |
| `mmx video download` | 下载已完成的视频 |
| `mmx image generate` | 图片生成，多宽高比 |
| `mmx vision describe` | 图片理解 / OCR |
| `mmx search query` | 网页搜索 |
| `mmx quota show` | 查看配额 |

## 快速开始

直接告诉 Agent 你想做什么：

- **语音合成**：`帮我生成一段语音，内容是"你好，欢迎使用 MiniMax"`
- **生成音乐**：`帮我生成一首欢快的流行音乐`
- **视频生成**：`生成一个海边日落的视频`
- **图片生成**：`画一只可爱的橘猫`

## 视频生成模型参考

| 模型 | 类型 | 分辨率 | 时长 |
|------|------|--------|------|
| MiniMax-Hailuo-2.3 | 文/图生视频 | 512P / 768P / 1080P | 6s / 10s |
| MiniMax-Hailuo-2.3-Fast | 文/图生视频 | — | 6s |

## 项目结构

```
minimax_model_skill/
├── SKILL.md      # 核心指令文件（mmx CLI 命令 + REST API 备用）
└── README.md     # 本文件
```
