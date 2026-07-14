from rag.prompt_builder import RAGPromptBuilder
from core.llm import LocalLLM


class GameAgent:
    """
    AI文字游戏决策代理
    负责连接RAG和本地模型
    """

    def __init__(self):
        self.rag = RAGPromptBuilder()
        self.llm = LocalLLM()

    def respond(self, player_input):
        prompt = self.rag.build(player_input)

        response = self.llm.generate(prompt)

        return response
