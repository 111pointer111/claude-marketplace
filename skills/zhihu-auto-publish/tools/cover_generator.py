"""封面图生成器 — 调用 mmx image generate 生成封面"""
import subprocess
import os
import time
from pathlib import Path


def generate_cover(topic: str, title: str, settings: dict) -> str | None:
    """生成封面图，返回本地保存路径。失败返回 None。"""
    upload_dir = Path(settings.get("UPLOAD_DIR", "/tmp/openclaw/uploads"))
    upload_dir.mkdir(parents=True, exist_ok=True)

    style = settings.get(
        "COVER_STYLE",
        "赛博朋克，未来科技感，霓虹灯光，AI脑神经，网络数字世界，高清，概念艺术",
    )
    prompt = f"{topic}，{title}，{style}"
    aspect_ratio = settings.get("COVER_ASPECT_RATIO", "1:1")
    out_prefix = f"cover_{int(time.time())}"
    out_dir = str(upload_dir)

    cmd = [
        "mmx", "image", "generate",
        "--prompt", prompt,
        "--aspect-ratio", aspect_ratio,
        "--out-dir", out_dir,
        "--out-prefix", out_prefix,
        "--quiet",
    ]

    # API key 必须从环境变量读取
    api_key = os.environ.get("MINIMAX_API_KEY")
    if api_key:
        cmd.extend(["--api-key", api_key])

    print(f"🎨 正在生成封面图...")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if result.returncode != 0:
            print(f"   mmx image error: {result.stderr}")
            return None

        output = result.stdout.strip()
        if not output:
            print("   mmx 未返回文件路径")
            return None

        cover_path = output.split("\n")[0].strip()
        if cover_path and Path(cover_path).exists():
            print(f"✅ 封面图已保存: {cover_path}")
            return cover_path
        else:
            print(f"   文件不存在: {cover_path}")
            return None

    except subprocess.TimeoutExpired:
        print("   mmx 封面图生成超时（120s）")
        return None
    except Exception as e:
        print(f"   mmx 封面图生成失败: {e}")
        return None
