from rag.prompt_builder import RAGPromptBuilder
from core.llm import LocalLLM
from core.action_planner import ActionPlanner


class GameAgent:
    """
    AI游戏智能代理
    """

    def __init__(self):
        self.rag = RAGPromptBuilder()
        self.llm = LocalLLM()
        self.planner = ActionPlanner()

    def respond(self, player_input):
        analysis = self.planner.analyze(player_input)

        prompt = self.rag.build(player_input)
        prompt += f"\n\n行动分析:\n{analysis}"

        response = self.llm.generate(prompt)

        self.planner.update_after_action(
            f"玩家执行行为:{player_input}"
        )

        return response
