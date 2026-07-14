from rag.prompt_builder import RAGPromptBuilder


class AIBridge:
    """
    Windows界面与AI系统连接层
    后续接入本地LLM模型
    """

    def __init__(self):
        self.rag = RAGPromptBuilder()

    def chat(self, user_text):
        prompt = self.rag.build(user_text)

        # TODO:
        # 在这里调用 core/llm.py
        # 返回真实模型生成内容

        return "AI分析完成:\n" + prompt
