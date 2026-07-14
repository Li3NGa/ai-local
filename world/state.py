import json
import os


class WorldState:
    """
    游戏世界状态管理
    """

    def __init__(self, path="world_state.json"):
        self.path = path
        self.state = self.load()

    def load(self):
        if os.path.exists(self.path):
            with open(self.path, "r", encoding="utf-8") as f:
                return json.load(f)

        return {
            "time":"morning",
            "weather":"clear",
            "location":"unknown",
            "events":[],
            "player":{
                "health":100,
                "money":0,
                "reputation":0
            }
        }

    def update(self, key, value):
        self.state[key] = value
        self.save()

    def save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.state, f, ensure_ascii=False, indent=2)

    def get_context(self):
        return self.state
