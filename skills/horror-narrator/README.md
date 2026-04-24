# Horror Narrator — 恐怖故事视频创作工坊

把任意恐怖故事变成一段约 60 秒的视频：6 帧画面 + 6 段旁白 + 1 段氛围 BGM，支持一键发布到小红书。

## 这是一个创作系统

- **不生成故事**——故事由你提供，或从网上搜索改编
- **输出创作规则**——旁白技巧、视觉规范、配音节奏、BGM 设计
- **执行生成**——通过 mmx CLI 生成图片、配音、BGM
- **一键发布**——通过 social-auto-upload 自动上传小红书

## 核心规则

| 规则 | 内容 |
|------|------|
| 6 帧结构 | 铺垫 → 异兆 → 加剧 → 高潮 → 反转 → 收尾 |
| 旁白技巧 | 五感写作、句式节奏、开场钩子、主角名字 |
| 视觉规范 | 4 种画风、prompt 公式、各帧构图要点 |
| 配音设计 | 帧级 speed/pitch 参数（speed 1.0 基准）|
| BGM 设计 | 三层声音、静默的力量、与帧的对应 |
| 吸引力逻辑 | Slow Burn > Jump Scare、中式恐怖美学 |

## 完整流程

1. 你提供故事（或给主题搜索改编）
2. AI 解析故事，拆成 6 帧，编写旁白 + 画面 prompt
3. 你确认脚本
4. 并行生成 6 帧插图 + 6 段配音
5. 生成恐怖 BGM
6. ffmpeg 自动合成 MP4 视频
7. 可选：一键发布到小红书

## 依赖

- [mmx-cli](https://www.npmjs.com/package/mmx-cli)：`npm install -g mmx-cli`
- MiniMax API Key：`mmx auth login --api-key <your-key>`
- [social-auto-upload](https://github.com/dreammis/social-auto-upload)：小红书自动发布

## 小红书发布（可选）

```bash
# 首次安装
git clone https://github.com/dreammis/social-auto-upload.git && cd social-auto-upload && uv pip install -e .
PLAYWRIGHT_DOWNLOAD_HOST="https://npmmirror.com/mirrors/playwright" patchright install chromium

# 首次登录（扫码一次即可）
sau xiaohongshu login --account horror_story

# 上传视频
sau xiaohongshu upload-video \
  --account horror_story \
  --file output.mp4 \
  --title "深夜路过这片坟地后..." \
  --tags "恐怖故事,民间灵异,深夜故事" \
  --thumbnail frame_04.jpg \
  --headless
```

## 小红书发布建议

- **标题**：悬念式，如「深夜路过这片坟地后，他再也没能回家」
- **标签**：`恐怖故事` `民间灵异` `深夜故事` `吓人` `惊魂`
- **封面**：用高潮帧（frame_04）或收尾帧（frame_06）作为封面图
