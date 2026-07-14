import json
import os


class KnowledgeRetriever:
    """
    简易知识检索器。
    后续可以替换为 Chroma + Embedding 向量检索。
    """

    def __init__(self, path="knowledge/world.json"):
        self.path = path
        self.data = self.load()

    def load(self):
        if not os.path.exists(self.path):
            return {}

        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)

    def search(self, keyword):
        results = []

        text = json.dumps(self.data, ensure_ascii=False)

        if keyword in text:
            results.append(self.data)

        return results


if __name__ == "__main__":
    rag = KnowledgeRetriever()
    print(rag.search("世界"))
