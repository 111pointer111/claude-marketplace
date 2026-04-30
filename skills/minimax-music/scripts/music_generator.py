"""MiniMax AI 音乐生成器 — 调用 mmx music generate 生成音乐"""
import subprocess
import json
import re
import os
import yaml
from datetime import datetime
from pathlib import Path
from typing import Optional


def load_settings(skill_dir: str) -> dict:
    """加载 settings.yaml 配置"""
    settings_path = Path(skill_dir) / "settings.yaml"
    if not settings_path.exists():
        raise FileNotFoundError(f"配置文件不存在: {settings_path}")
    with open(settings_path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def build_mmx_command(
    prompt: str,
    lyrics: Optional[str],
    vocals: Optional[str],
    genre: Optional[str],
    mood: Optional[str],
    instruments: Optional[str],
    tempo: Optional[str],
    bpm: Optional[int],
    key: Optional[str],
    use_case: Optional[str],
    references: Optional[str],
    structure: Optional[str],
    avoid: Optional[str],
    extra: Optional[str],
    aigc_watermark: bool,
    output_path: str,
    format: str,
    bitrate: str,
    sample_rate: str,
    settings: dict,
) -> list:
    """构建 mmx music generate 命令"""
    cmd = ["mmx", "music", "generate"]

    # 歌词/器乐模式判断
    if lyrics == "___LYRICS_OPTIMIZER___":
        cmd.extend(["--lyrics-optimizer"])
    elif lyrics:
        cmd.extend(["--lyrics", lyrics])
    else:
        cmd.extend(["--instrumental"])

    cmd.extend(["--prompt", prompt])

    if vocals:
        cmd.extend(["--vocals", vocals])
    if genre:
        cmd.extend(["--genre", genre])
    if mood:
        cmd.extend(["--mood", mood])
    if instruments:
        cmd.extend(["--instruments", instruments])
    if tempo:
        cmd.extend(["--tempo", tempo])
    if bpm:
        cmd.extend(["--bpm", str(bpm)])
    if key:
        cmd.extend(["--key", key])
    if use_case:
        cmd.extend(["--use-case", use_case])
    if references:
        cmd.extend(["--references", references])
    if structure:
        cmd.extend(["--structure", structure])
    if avoid:
        cmd.extend(["--avoid", avoid])
    if extra:
        cmd.extend(["--extra", extra])

    if aigc_watermark:
        cmd.append("--aigc-watermark")

    cmd.extend(["--format", format])
    cmd.extend(["--sample-rate", sample_rate])
    cmd.extend(["--bitrate", bitrate])
    cmd.extend(["--out", output_path])

    # API key 必须从环境变量读取，禁止硬编码
    api_key = os.environ.get("MINIMAX_API_KEY")
    if api_key:
        cmd.extend(["--api-key", api_key])

    return cmd


def run_mmx(cmd: list, timeout: int) -> tuple:
    """执行 mmx 命令，返回 (returncode, stdout, stderr)"""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return -1, "", f"命令执行超时（{timeout}s）"
    except Exception as e:
        return -2, "", str(e)


def extract_song_title(prompt: str, genre_input: str, mood_input: str) -> str:
    """从 prompt 中提取歌名（≤8字）"""
    import re
    match = re.search(r'歌名[：:](.+?)(?:[\n。，]|$)', prompt)
    if match:
        title = match.group(1).strip().strip('"\'')
        if len(title) <= 8:
            return title
        return title[:8]

    hook_match = re.search(
        r'[Hh][Oo][Oo][Kk]\s*[：:]?\s*["\u201c](.+?)["\u201d]|副歌[Hh][Oo][Oo][Kk]\s*[：:]?\s*["\u201c](.+?)["\u201d]',
        prompt
    )
    if hook_match:
        title = next(g for g in hook_match.groups() if g)
        title = title.strip().strip('"\'')
        if len(title) > 8:
            return title[:8]
        if title:
            return title

    q_matches = re.findall(r'["\u201c\u2018]([^"\u201c\u2018\']{2,10})["\u201d\u2019]', prompt)
    if q_matches:
        for m in q_matches:
            m = m.strip()
            if 2 <= len(m) <= 8 and '歌' not in m:
                return m

    type_map = {
        "instrumental": "纯音乐",
        "ambient": "氛围",
        "piano": "钢琴曲",
    }
    genre_lower = (genre_input or "").lower()
    for key, val in type_map.items():
        if key in genre_lower:
            return val

    return "未命名"


def generate_music(
    prompt: str,
    settings: dict,
    lyrics: Optional[str] = None,
    vocals: Optional[str] = None,
    genre: Optional[str] = None,
    mood: Optional[str] = None,
    instruments: Optional[str] = None,
    tempo: Optional[str] = None,
    bpm: Optional[int] = None,
    key: Optional[str] = None,
    use_case: Optional[str] = None,
    references: Optional[str] = None,
    structure: Optional[str] = None,
    avoid: Optional[str] = None,
    extra: Optional[str] = None,
    aigc_watermark: bool = True,
    output_filename: Optional[str] = None,
    output_dir: Optional[str] = None,
    song_type: Optional[str] = None,
    song_title: Optional[str] = None,
) -> dict:
    """
    生成一首音乐，返回结果字典：
    {
        "file_path": str,   # 音频文件完整路径
        "duration": str,   # 音频时长
        "style": str,      # 风格描述
        "success": bool,
        "error": str,      # 失败时原因
    }
    """
    # 输出目录
    out_dir = Path(output_dir or settings.get("OUTPUT_DIR", "./music_output"))
    out_dir.mkdir(parents=True, exist_ok=True)

    date_str = datetime.now().strftime("%Y%m%d")

    type_tag = song_type
    if not type_tag:
        genre_raw = genre or ""
        if lyrics is None:
            type_tag = "纯音乐"
        else:
            first_genre = genre_raw.split(",")[0].split("/")[0].strip()
            if first_genre and len(first_genre) <= 6:
                type_tag = first_genre
            else:
                type_tag = "歌曲"

    title = song_title or extract_song_title(prompt, genre or "", mood or "")

    ext = settings.get("DEFAULT_FORMAT", "mp3")
    if not output_filename:
        safe_title = re.sub(r'[\\/:*?"<>|\u2019]', '', title)
        safe_title = safe_title.strip()
        if not safe_title:
            safe_title = "无题"
        output_filename = f"{date_str}_{type_tag}_{safe_title}.{ext}"

    output_path = str(out_dir / output_filename)

    format = settings.get("DEFAULT_FORMAT", "mp3")
    bitrate = settings.get("DEFAULT_BITRATE", "256000")
    sample_rate = settings.get("DEFAULT_SAMPLE_RATE", "44100")
    timeout = settings.get("MMX_TIMEOUT", 300)

    cmd = build_mmx_command(
        prompt=prompt,
        lyrics=lyrics,
        vocals=vocals,
        genre=genre,
        mood=mood,
        instruments=instruments,
        tempo=tempo,
        bpm=bpm,
        key=key,
        use_case=use_case,
        references=references,
        structure=structure,
        avoid=avoid,
        extra=extra,
        aigc_watermark=aigc_watermark,
        output_path=output_path,
        format=format,
        bitrate=bitrate,
        sample_rate=sample_rate,
        settings=settings,
    )

    print(f"🎵 正在生成音乐...")
    print(f"   prompt: {prompt[:100]}...")
    if lyrics == "___LYRICS_OPTIMIZER___":
        print(f"   lyrics: (自动生成)")
    elif lyrics:
        print(f"   lyrics: {lyrics[:50]}...")
    print(f"   output: {output_path}")

    returncode, stdout, stderr = run_mmx(cmd, timeout)

    if returncode != 0:
        print(f"   ❌ mmx error: {stderr}")
        return {"file_path": None, "success": False, "error": stderr, "style": prompt}

    file_path = stdout.strip().split("\n")[-1]
    if not file_path or not Path(file_path).exists():
        file_path = output_path

    print(f"   ✅ 音乐已保存: {file_path}")
    return {
        "file_path": file_path,
        "success": True,
        "style": prompt,
        "duration": "unknown",
        "output_filename": output_filename,
        "song_type": type_tag,
        "song_title": title,
    }


def get_daily_theme(index: int, settings: dict) -> dict:
    """获取指定索引的每日主题（按顺序轮换）"""
    themes = settings.get("DAILY_THEMES", [])
    if not themes:
        return {
            "name": "每日音乐",
            "prompt": "优美的中文流行音乐，温暖愉悦",
            "type": "song",
            "genre": "pop",
            "mood": "uplifting",
        }
    return themes[index % len(themes)]


def generate_daily_music(
    skill_dir: str,
    date: Optional[str] = None,
) -> list:
    """
    每日三首音乐生成主函数。
    参数：
        skill_dir: skill 根目录（settings.yaml 所在目录）
        date: 可选，指定日期（格式 YYYY-MM-DD），默认今天
    返回：
        [result1, result2, result3]
    """
    settings = load_settings(skill_dir)
    output_dir = settings.get("OUTPUT_DIR", "./music_output")
    date = date or datetime.now().strftime("%Y-%m-%d")

    results = []

    for i in range(3):
        theme = get_daily_theme(i, settings)
        name = theme.get("name", f"第{i + 1}首")
        prompt = theme.get("prompt", "优美的中文音乐")
        mtype = theme.get("type", "song")
        print(f"\n{'='*50}")
        print(f"📅 今日第 {i + 1} 首: {name}")
        print(f"{'='*50}")

        type_tag = "歌曲" if mtype == "song" else "纯音乐"
        name_lower = name.lower()
        if "唤醒" in name or "清晨" in name or "早晨" in name:
            type_tag = "晨间"
        elif "专注" in name or "深夜" in name or "工作" in name or "书房" in name:
            type_tag = "专注"
        elif "独处" in name or "午后" in name:
            type_tag = "午后"

        theme_title = theme.get("song_title")

        if mtype == "instrumental":
            result = generate_music(
                prompt=prompt,
                settings=settings,
                lyrics=None,
                vocals=None,
                genre=theme.get("genre"),
                mood=theme.get("mood"),
                instruments=theme.get("instruments"),
                tempo=theme.get("tempo"),
                bpm=theme.get("bpm"),
                key=theme.get("key"),
                use_case=theme.get("use_case"),
                avoid=theme.get("avoid"),
                extra=theme.get("extra"),
                aigc_watermark=True,
                output_dir=output_dir,
                song_type=type_tag,
                song_title=theme_title,
            )
        else:
            vocals = theme.get("vocals") or settings.get("DEFAULT_VOCALS", "温暖男中音")
            result = generate_music(
                prompt=prompt,
                settings=settings,
                lyrics="___LYRICS_OPTIMIZER___",
                vocals=vocals,
                genre=theme.get("genre"),
                mood=theme.get("mood"),
                instruments=theme.get("instruments"),
                tempo=theme.get("tempo"),
                bpm=theme.get("bpm"),
                key=theme.get("key"),
                use_case=theme.get("use_case"),
                references=theme.get("references"),
                structure=theme.get("structure"),
                avoid=theme.get("avoid"),
                extra=theme.get("extra"),
                aigc_watermark=True,
                output_dir=output_dir,
                song_type=type_tag,
                song_title=theme_title,
            )

        result["theme_name"] = name
        result["date"] = date
        results.append(result)

    log_path = Path(output_dir) / f"daily_log_{date}.json"
    log_data = {
        "date": date,
        "generated_at": datetime.now().isoformat(),
        "results": [
            {
                "theme_name": r["theme_name"],
                "file_path": r.get("file_path"),
                "success": r["success"],
                "error": r.get("error", ""),
                "style": r.get("style", ""),
            }
            for r in results
        ],
    }
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(log_data, f, ensure_ascii=False, indent=2)
    print(f"\n📝 日志已保存: {log_path}")

    return results
