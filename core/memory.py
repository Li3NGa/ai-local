import sqlite3
from datetime import datetime


class Memory:
    """
    AI游戏长期记忆系统
    保存玩家行为和重要事件
    """

    def __init__(self, db_path="memory.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS memories(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT,
            importance INTEGER,
            created TEXT
        )
        """)
        self.conn.commit()

    def save(self, content, importance=1):
        self.conn.execute(
            "INSERT INTO memories(content,importance,created) VALUES(?,?,?)",
            (content, importance, datetime.now().isoformat())
        )
        self.conn.commit()

    def recall(self, limit=10):
        cursor = self.conn.execute(
            "SELECT content FROM memories ORDER BY importance DESC LIMIT ?",
            (limit,)
        )

        return [row[0] for row in cursor.fetchall()]
