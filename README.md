# ai-local

一个本地部署的小型文字型 AI 助手。

## 功能
- 本地运行，无需云端 API
- 支持中文文字对话
- 基于 HuggingFace 小模型
- 可在普通电脑运行

## 安装

```bash
pip install -r requirements.txt
```

## 运行

```bash
python app.py
```

## 默认模型

使用 `Qwen2.5-0.5B-Instruct` 小参数模型，适合学习、本地测试。

后续可以升级：
- Web UI
- 长期记忆
- 文档知识库 RAG
- 语音输入输出
