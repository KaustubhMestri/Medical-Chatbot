<!-- ====================== Banner / Header ====================== -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0052D4,50:4364F7,100:6FB1FC&height=180&section=header&text=MEDICAL%20CHATBOT&fontSize=48&fontColor=ffffff&desc=AI-Powered%20Healthcare%20Assistant&descFontSize=24" alt="Medical Chatbot Banner" />
</p>

<p align="center">
  <a href="https://github.com/KaustubhMestri/Medical-Chatbot">
    <img src="https://img.shields.io/github/license/KaustubhMestri/Medical-Chatbot?style=for-the-badge&logo=opensourceinitiative&logoColor=white&color=00C897" alt="License" />
    <img src="https://img.shields.io/github/last-commit/KaustubhMestri/Medical-Chatbot?style=for-the-badge&logo=git&logoColor=white&color=00C897" alt="Last Commit" />
    <img src="https://img.shields.io/github/languages/top/KaustubhMestri/Medical-Chatbot?style=for-the-badge&color=00C897" alt="Top Language" />
    <img src="https://img.shields.io/github/languages/count/KaustubhMestri/Medical-Chatbot?style=for-the-badge&color=00C897" alt="Language Count" />
  </a>
</p>

---

## 🏥 Project Overview

**Medical-Chatbot** is an AI assistant that gives **medical information**, **symptom guidance**, and **wellness tips** in conversational style.  
It uses document embeddings and LLMs to answer health queries based on trusted medical literature.

---

## ✨ Features

| Feature                     | Description                                                  |
| --------------------------- | ------------------------------------------------------------ |
| 🧠 **AI Q&A**               | Ask about symptoms, diseases, health advice                  |
| 📄 **Doc-based answers**    | Uses _The Gale Encyclopedia of Medicine_ and other documents |
| ⚡ **Fast responses**       | Uses vector search + LLM to deliver answers quickly          |
| 💬 **Conversational flow**  | Keeps context for follow-ups                                 |
| 🔄 **Modular & extendable** | Add more medical sources, tune prompts, etc.                 |
| 🌐 **Web interface**        | Built with Flask + simple HTML frontend                      |

---

## 🧩 Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
  <img src="https://img.shields.io/badge/LangChain-121212?style=for-the-badge&logo=chainlink&logoColor=00C897" alt="LangChain" />
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" />
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git" />
</p>

---

## 📂 Project Structure

```text
Medical-Chatbot/
├── app.py                 # Flask application entry point
├── store_index.py         # Code to index / embed medical docs
├── src/
│   ├── helper.py          # Loading docs, embeddings, query logic
│   └── prompt.py          # LLM prompt templates
├── data/
│   └── The-Gale-Encyclopedia-of-Medicine.pdf
├── templates/
│   └── chat.html           # Frontend chat UI
├── research/
│   └── trails.ipynb        # Experimentation, notebooks
├── requirements.txt        # Dependencies
├── setup.py
└── template.sh
```
