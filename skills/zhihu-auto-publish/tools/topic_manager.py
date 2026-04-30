"""主题管理器 — 避免内容重复，支持角度轮换"""
import json
import os
from datetime import datetime, timedelta
from pathlib import Path


class TopicManager:
    """管理主题冷却期和角度轮换"""

    def __init__(self, settings: dict):
        self.settings = settings
        state_file = settings.get("TOPIC_STATE_FILE", "/tmp/zhihu_topic_state.json")
        self.state_file = Path(state_file)
        self.state = self._load_state()

    def _load_state(self) -> dict:
        if self.state_file.exists():
            with open(self.state_file) as f:
                return json.load(f)
        return {
            "last_topics": [],
            "topic_angles": {},
        }

    def _save_state(self):
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.state_file, "w", encoding="utf-8") as f:
            json.dump(self.state, f, ensure_ascii=False, indent=2)

    def can_use_topic(self, topic: str) -> bool:
        """主题是否在冷却期内"""
        cooldown = self.settings.get("TOPIC_COOLDOWN_DAYS", 1)
        cutoff = (datetime.now() - timedelta(days=cooldown)).strftime("%Y-%m-%d")

        for item in self.state.get("last_topics", []):
            if item["topic"] == topic and item["date"] >= cutoff:
                return False
        return True

    def get_next_angle(self, topic: str) -> str:
        """获取下一个角度（轮换使用）"""
        angles = self.settings.get(
            "TOPIC_ANGLES",
            ["技术解析", "产业分析", "实战案例", "未来预测", "深度解读", "对比研究"],
        )
        used = self.state.get("topic_angles", {}).get(topic, [])
        used_angles = [a["angle"] for a in used[-len(angles) :]]

        for angle in angles:
            if angle not in used_angles:
                return angle
        return angles[0]  # 轮换一圈后从头开始

    def record_topic(self, topic: str, angle: str, title: str):
        """记录本次使用的主题"""
        now = datetime.now().strftime("%Y-%m-%d")

        self.state.setdefault("last_topics", []).append({
            "topic": topic,
            "angle": angle,
            "title": title,
            "date": now,
        })

        # 只保留 30 天内记录
        cutoff = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
        self.state["last_topics"] = [
            t for t in self.state["last_topics"] if t["date"] >= cutoff
        ]

        self.state.setdefault("topic_angles", {}).setdefault(topic, []).append({
            "angle": angle,
            "date": now,
        })

        self._save_state()
