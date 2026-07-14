from rag.retriever import KnowledgeRetriever


class RAGPromptBuilder:
    def __init__(self):
        self.retriever = KnowledgeRetriever()

    def build(self, player_input):
        knowledge = self.retriever.search(player_input)

        return f"""
你是一个AI文字游戏世界模拟器。

规则：
1. 根据世界知识回答
2. 不创造未知事实
3. 保持角色一致

世界知识:
{knowledge}

玩家行为:
{player_input}

请生成合理回复。
"""
