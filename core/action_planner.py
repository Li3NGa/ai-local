import random

from core.memory import Memory
from world.state import WorldState


class ActionPlanner:
    """
    AI自主决策层

    分析玩家行为:
    - 行为类型
    - 风险
    - 世界影响
    - 记忆变化
    """

    def __init__(self):
        self.memory = Memory()
        self.world = WorldState()

    def analyze(self, player_input):
        action = self.detect_action(player_input)

        return {
            "action": action,
            "world": self.world.get_context(),
            "memory": self.memory.recall()
        }

    def detect_action(self, text):
        keywords = {
            "attack": ["攻击", "杀", "打"],
            "move": ["去", "进入", "前往"],
            "talk": ["说", "问", "聊天"],
            "trade": ["买", "卖", "交易"]
        }

        for action, words in keywords.items():
            for word in words:
                if word in text:
                    return action

        return "unknown"

    def update_after_action(self, event):
        self.memory.save(event, importance=5)
        self.world.state["events"].append(event)
        self.world.save()
