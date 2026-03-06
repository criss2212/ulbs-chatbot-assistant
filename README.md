# 🤖 ULBS Chatbot Assistant - Code4ULBS

![ULBS Shield](https://www.ulbsibiu.ro/wp-content/uploads/2017/10/logo_ulbs_blue.png)

Bun venit la **ULBS Chatbot Assistant**! 👋 
Acest proiect reprezintă un asistent inteligent (RAG) antrenat pe regulamentele, orarele și procedurile Universității "Lucian Blaga" din Sibiu.

## 📋 Table of Contents
- [Core Requirements](#-core-requirements)
- [Tech Stack](#-tech-stack)
- [Development Environment Setup](#-development-environment-setup)
- [Architecture (RAG)](#-architecture-rag)
- [Testing & Quality](#-testing--quality)
- [Deployment](#-deployment)

---

## 🎯 Core Requirements
Acest proiect implementează standardele obligatorii Code4ULBS:
- ✅ **Containerization** - Suport complet Docker & Podman.
- ✅ **CI/CD** - Pipeline-uri automate pe runner-ul `build-01`.
- ✅ **AI Instructions** - Configurație optimizată în `.github/copilot-instructions.md`.

---

## 🚀 Tech Stack
- **Backend:** Python 3.13 + FastAPI
- **Orchestrare AI:** LangChain
- **Vector Database:** ChromaDB (local storage)
- **Embeddings/LLM:** OpenAI API (GPT-4o)
- **PDF Processing:** PyPDF / Unstructured

---

## 💻 Development Environment Setup

### Prerequisites
- Python 3.13+
- Git
- Docker / Podman (pentru producție)

### Instalare Locală
1. **Clonează repository-ul:**
   ```powershell
   git clone [https://github.com/Code4ULBS/ulbs-chatbot.git](https://github.com/Code4ULBS/ulbs-chatbot.git)
   cd "ulbs-chatbot"
