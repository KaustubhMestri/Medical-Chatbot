# 🩺 RAG-based Medical Chatbot

**Medical Chatbot** is a Python-based healthcare assistant using Retrieval-Augmented Generation (RAG) to provide accurate medical insights and symptom analysis from "The Gale Encyclopedia of Medicine."

**Disclaimer**: For informational use only. Consult a doctor for medical advice.

## Overview

A smart chatbot that uses RAG to deliver context-aware, reliable answers to medical questions by searching a medical knowledge base (PDF) with semantic search.

## Key Features

- Fact-based answers from medical documents
- Semantic search for precise results
- Scalable for cloud deployment
- Fine-tuned for medical accuracy

## Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white" alt="Flask"/>
  <img src="https://img.shields.io/badge/LangChain-121212?style=flat-square&logo=chainlink&logoColor=00C897" alt="LangChain"/>
  <img src="https://img.shields.io/badge/Sentence%20Transformers-FF6F61?style=flat-square&logo=huggingface&logoColor=white" alt="Sentence Transformers"/>
  <img src="https://img.shields.io/badge/Pinecone-008080?style=flat-square&logo=pinecone&logoColor=white" alt="Pinecone"/>
  <img src="https://img.shields.io/badge/Mixtral-412991?style=flat-square&logo=ai&logoColor=white" alt="Mixtral"/>
</p>

## Installation

Install:

- **Git**: [Download](https://git-scm.com/download/win)

### Clone Repository

1. Open CLI.
2. Run:
   ```bash
   git clone https://github.com/KaustubhMestri/Medical-Chatbot
   cd Medical-Chatbot
   ```

### Set Up Environment

1. Create a virtual environment:
   ```bash
   python3 -m venv medbot
   ```
2. Activate:
   ```bash
   source medbot/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up `.env`:
   ```bash
   cp .env.example .env
   ```
   Add: `PINECONE_API_KEY=your-key`

### Run App

```bash
python app.py
```

Open `http://127.0.0.1:5000`.

## Contributing

1. Create an [issue](https://github.com/KaustubhMestri/Medical-Chatbot/issues).
2. Branch: `feature/<name>` or `bugfix/<name>`
   ```bash
   git checkout -b feature/<name>
   ```
3. Commit:
   ```bash
   git add .
   git commit -m "#<issue> message"
   ```
4. Push:
   ```bash
   git push origin feature/<name>
   ```
5. Submit PR to `main`.

## License

MIT License. See [LICENSE](LICENSE).
