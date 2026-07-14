from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton
import sys
from ai_bridge import AIBridge


class AIWorldWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ai = AIBridge()

        self.setWindowTitle("AI文字世界")
        self.resize(900, 600)

        layout = QVBoxLayout()

        self.chat = QTextEdit()
        self.chat.setReadOnly(True)
        self.chat.append("AI世界已启动。请输入你的行动。")

        self.input = QLineEdit()
        self.input.setPlaceholderText("输入你的行动...")

        self.button = QPushButton("发送")
        self.button.clicked.connect(self.send)

        layout.addWidget(self.chat)
        layout.addWidget(self.input)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def send(self):
        text = self.input.text()
        if text:
            self.chat.append("玩家: " + text)
            response = self.ai.chat(text)
            self.chat.append("AI: " + response)
            self.input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AIWorldWindow()
    window.show()
    sys.exit(app.exec())
