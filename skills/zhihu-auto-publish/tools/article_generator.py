"""文章生成器 — 抓取 HN AI 热点 + MiniMax mmx 生成文章"""
import subprocess
import os
import requests
from datetime import datetime
from pathlib import Path


def fetch_rss_items(url: str, limit: int = 5) -> list:
    """从 RSS 源抓取条目"""
    import xml.etree.ElementTree as ET
    try:
        resp = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        if resp.status_code != 200:
            return []
        root = ET.fromstring(resp.content)
        ns = {"": "http://www.w3.org/2005/Atom"}
        items = []
        # 兼容 RSS 2.0 和 Atom
        for entry in root.findall(".//item", {}) or []:
            title_el = entry.find("title")
            link_el = entry.find("link")
            items.append({
                "title": title_el.text if title_el is not None else "",
                "url": link_el.text if link_el is not None else "",
            })
        for entry in root.findall(".//atom:entry", {"atom": "http://www.w3.org/2005/Atom"}):
            title_el = entry.find("atom:title", {"atom": "http://www.w3.org/2005/Atom"})
            link_el = entry.find("atom:link", {"atom": "http://www.w3.org/2005/Atom"})
            link_href = link_el.get("href", "") if link_el is not None else ""
            items.append({
                "title": title_el.text if title_el is not None else "",
                "url": link_href,
            })
        return items[:limit]
    except Exception as e:
        print(f"  RSS 抓取失败 ({url}): {e}")
        return []


def fetch_zh_ai_topics(limit: int = 10) -> list:
    """抓取中文 AI 热点（机器之心 + 量子位 RSS）"""
    sources = [
        ("机器之心", "https://www.jiqizhixin.com/feed"),
        ("量子位", "https://www.qbitai.com/feed"),
    ]
    topics = []
    seen_titles = set()

    for source_name, rss_url in sources:
        items = fetch_rss_items(rss_url, limit=5)
        for item in items:
            title = item.get("title", "").strip()
            if not title or title in seen_titles:
                continue
            seen_titles.add(title)
            # 简单 AI 关键词过滤
            ai_kws = ["ai", "人工智能", "大模型", "gpt", "llm", "openai", "claude",
                      "gemini", "agent", "神经网络", "深度学习", "机器学习",
                      "量化", "智谱", "深度求索", "kimi", "通义", "文心",
                      "星火", "百川", "月之暗面", "rag", "多模态", "具身"]
            if not any(kw in title.lower() for kw in ai_kws):
                continue
            topics.append({
                "id": f"zh_{source_name}_{len(topics)}",
                "title": title,
                "url": item.get("url", ""),
                "source": source_name,
                "score": 100 - len(topics) * 5,
                "descendants": 0,
            })
            if len(topics) >= limit:
                break
        if len(topics) >= limit:
            break

    return topics


def fetch_hn_ai_topics(limit: int = 10):
    """抓取 Hacker News AI 相关热点（作为备用英文源）"""
    try:
        resp = requests.get(
            "https://hacker-news.firebaseio.com/v0/topstories.json", timeout=10
        )
        if resp.status_code != 200:
            return []

        story_ids = resp.json()[:50]
        topics = []

        for sid in story_ids:
            story = requests.get(
                f"https://hacker-news.firebaseio.com/v0/item/{sid}.json", timeout=5
            ).json()
            if story and _is_ai_related(story):
                raw_title = story.get("title", "")
                cn_title = translate_to_chinese(raw_title)
                topics.append({
                    "id": sid,
                    "title": cn_title,
                    "url": story.get("url", ""),
                    "score": story.get("score", 0),
                    "descendants": story.get("descendants", 0),
                    "source": "Hacker News",
                    "raw_title": raw_title,
                })
            if len(topics) >= limit:
                break

        return topics if topics else []
    except Exception:
        return []


def _is_ai_related(story: dict) -> bool:
    title = story.get("title", "").lower()
    text = story.get("text", "").lower()
    ai_kws = ["ai", "llm", "gpt", "openai", "claude", "gemini",
              "machine learning", "neural", "model", "agent",
              "anthropic", "deepmind", "mistral", "meta ai"]
    return any(kw in title or kw in text for kw in ai_kws)


def generate_article_prompt(topic: dict, angle: str) -> str:
    """构建文章生成 Prompt — v3：面向普通读者的生动硬核知乎文"""
    source = topic.get('source', 'Hacker News')
    return f"""你是一位知乎高赞答主，擅长把最硬的科技话题用最「人话」的方式讲得清清楚楚。请根据以下热点写一篇知乎文章。

## 热点资讯
- 标题: {topic['title']}
- 来源: {source}
- URL: {topic.get('url', '无')}
- 热度: {topic.get('score', 0)} 分 / {topic.get('descendants', 0)} 评论

## 铁律 — 先看懂这几条再动笔

### 1. 这篇文章是写给「普通人」看的
你对面坐的是一个对 AI 感兴趣但不懂技术的普通人。他不是工程师，不是投资人，就是一个刷知乎的普通用户。

你的任务：
- 把专业术语翻译成人话 — 不要用「全域数据利用范式」，要说「把散落的数据统一管理起来」
- 技术概念必须配比喻 — 每个核心概念都要有一个生活化的类比，比如：
  - 大模型就像「一个读过所有书的实习生」
  - 数据标准化就像「给全世界统一度量衡」
  - 平台化就像「安卓系统让所有人能做 App」
- 看不懂就重写 — 写完后问自己：一个高中文凭的人能看懂这一段吗？

### 2. 每一个核心观点，必须配一个生活化的比喻
格式：先说观点 → 然后「打个比方」→ 再回到技术本身。

比如要讲「跨本体大模型」：
> 传统做法是，每种机器人单独训一个模型。就像你学开车，教练让你学完手动挡再学自动挡，再学电动车——每换一种车就重学一遍。
>
> 跨本体大模型的思路是：直接让你学会「开车」这件事本身。不管是手动挡、自动挡还是电动车，都会开。这才是真正解决了问题。

### 3. 标题要让人想点进来
- **第一行写你自己取的标题**，不要原文标题，不要任何多余文字
- 不要论文标题（❌「银河通用LDA定义全域数据利用范式…」）
- 要用所有人都能懂的话提炼观点（✅「机器人终于学会了举一反三，看懂这篇你就明白了」）
- 可以用悬念、反问、颠覆认知的角度
- 长度 15-25 字最佳

### 4. 全文用 Markdown 格式
- 标题行直接写标题（不加 # 前缀，它在文章开头以大标题展示）
- 小标题用 ##
- 重点用 **加粗**
- 比喻/引用用 > 块引用

### 5. 结构清晰但有呼吸感
- **开头**：用一个具体的场景/故事/问题切入，让读者想说「这跟我有关系」
- **正文**：3-4 个小节，每个小节 = 一个观点 + 一个比喻 + 数据/事实 + 简短分析
- **结尾**：用一句有力的话总结，让读者看完感觉「我懂了」

### 6. 字数 1500-2500，别啰嗦
每个字都要有价值。一个比喻 3 句话说完，别展开成一个小说。

## 角度：{angle}

现在请开始写："""


def call_mmx(prompt: str, settings: dict) -> str | None:
    """调用 mmx text chat 生成文章"""
    model = settings.get("MINIMAX_TEXT_MODEL", "MiniMax-M2.7")
    max_tokens = settings.get("MINIMAX_MAX_TOKENS", 8192)
    temperature = settings.get("MINIMAX_TEMPERATURE", 0.7)

    cmd = [
        "mmx", "text", "chat",
        "--message", f"user:{prompt}",
        "--model", model,
        "--max-tokens", str(max_tokens),
        "--temperature", str(temperature),
        "--quiet",
    ]

    # API key 必须从环境变量读取
    api_key = os.environ.get("MINIMAX_API_KEY")
    if api_key:
        cmd.extend(["--api-key", api_key])

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        if result.returncode != 0:
            print(f"   mmx error: {result.stderr}")
            return None

        output = result.stdout.strip()
        if not output:
            if result.stderr.strip():
                print(f"   mmx stderr: {result.stderr[:300]}")
            return None

        lines = output.split("\n")
        while lines and lines[0].strip() in ("---", "```"):
            lines.pop(0)
        while lines and lines[-1].strip() in ("---", "```"):
            lines.pop()
        content = "\n".join(lines).strip()

        if not content:
            return None

        if len(content) < 100:
            print(f"   文章内容过短（{len(content)} 字符），可能失败")
            return None

        print(f"   文章生成成功，共 {len(content)} 字符")
        return content

    except subprocess.TimeoutExpired:
        print("   mmx 调用超时（180s）")
        return None
    except Exception as e:
        print(f"   mmx 调用失败: {e}")
        return None


def translate_to_chinese(title: str) -> str:
    """将英文标题翻译为中文表述（非直译，中文语境化）"""
    prompt = f"""请将以下英文标题翻译为中文科技媒体的表述风格。
要求：
- 不是直译，而是用中文科技媒体的语气重新表达
- 保留关键术语（如模型名、公司名）的原文
- 结果控制在 30 字以内

原文：{title}

中文表述："""
    try:
        result = subprocess.run(
            ["mmx", "text", "chat",
             "--message", f"user:{prompt}",
             "--model", "MiniMax-M2.7",
             "--max-tokens", "100",
             "--temperature", "0.3",
             "--quiet"],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0:
            translated = result.stdout.strip().strip('"').strip("'")
            if translated:
                return translated
        return title
    except Exception:
        return title


def save_article(title: str, content: str, settings: dict) -> tuple:
    """保存文章到文件"""
    output_dir = Path(settings.get("OUTPUT_DIR", "/tmp/zhihu-output"))
    output_dir.mkdir(parents=True, exist_ok=True)

    lines = content.strip().split('\n')
    generated_title = ''
    body_start = 0
    for i, line in enumerate(lines):
        stripped = line.strip()
        if (stripped and not stripped.startswith('#')
                and not stripped.startswith('---')
                and not stripped.startswith('***')
                and not stripped.startswith('—')
                and not stripped.startswith('-')
                and len(stripped) > 5):
            generated_title = stripped
            body_start = i + 1
            break

    body = '\n'.join(lines[body_start:]).strip()
    final_title = generated_title if generated_title else title

    filename = f"zhihu_article_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    filepath = output_dir / filename

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"{final_title}\n\n{body}")

    return str(filepath), final_title


def generate_article(topic: dict, angle: str, settings: dict) -> tuple:
    """
    生成文章，返回 (文章文件路径, 文章标题) 元组。
    save_article 会从 AI 生成内容中提取更好的标题。
    如 mmx 不可用，返回 (None, None)。
    """
    prompt = generate_article_prompt(topic, angle)
    content = call_mmx(prompt, settings)

    if not content:
        return None, None

    return save_article(topic["title"], content, settings)
