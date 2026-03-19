

🤖 ULBS Chatbot Assistant 

This project is an intelligent assistant built using RAG (Retrieval-Augmented Generation) architecture, orchestrated via n8n. It provides precise answers based on the official regulations, schedules, and procedures of the "Lucian Blaga" University of Sibiu.

📋 Table of Contents
Core Requirements

Tech Stack

Architecture (RAG via n8n)

Development & Setup

Project Structure

Deployment

🎯 Core Requirements
This project implements the mandatory Code4ULBS standards:

✅ Containerization - Full support for Docker & Podman (self-hosted n8n & DB).

✅ CI/CD - Automated pipelines running on the build-01 runner.

✅ AI Orchestration - Low-code workflow logic for transparency and easy maintenance.

🚀 Tech Stack
Orchestrator: n8n.io (Self-hosted via Docker)

AI Engine: OpenAI API (Model: gpt-4o or gpt-3.5-turbo)

Vector Database: Pinecone (Cloud) or Postgres + pgvector (Local Docker)

Embeddings: OpenAI text-embedding-3-small

Data Sources: Official ULBS PDFs, CSV/JSON files for schedules.

🏗️ Architecture (RAG via n8n)
The system operates by connecting university data sources to a Large Language Model (LLM) using n8n as the "brain" to orchestrate the flow in real-time.

Ingestion Phase: n8n reads official documents, performs Chunking (splitting text into manageable pieces), and saves them as Vectors in the database.

Query Phase: User asks a question → n8n performs a Similarity Search in the Vector Store → Retrieves relevant context → Sends context + question to ChatGPT → Returns the final response.

💻 Development & Setup
Prerequisites
Docker & Docker Compose

OpenAI API Key

Pinecone Account (or a local Vector DB instance)

Local Installation
Clone the repository:

Bash
git clone https://github.com/Code4ULBS/ulbs-chatbot-n8n.git
cd ulbs-chatbot-n8n
Launch the Infrastructure:

Bash
docker-compose up -d
This will start n8n and the required database containers.

Import Workflows:

Access n8n at http://localhost:5678.

Import the .json files located in the /workflows folder.

⚙️ Project Structure
The project is divided into two main automated workflows:

Ingestion Workflow (ingest_ulbs_data.json):

Read Binary File Node: Loads PDF/Excel sources.

Recursive Character Text Splitter: Prepares text chunks.

Vector Store Sender: Populates the database with embeddings.

Chat Workflow (ulbs_ai_agent.json):

Webhook Input: Triggered by a web UI or Telegram bot.

AI Agent Node: The core node managing conversation memory and the Vector Store Tool.

Final Output: Delivers the response back to the user.

🛠️ Testing & Quality
Prompt Engineering: The "System Prompt" is optimized to maintain a professional, academic tone.

Source Verification: The bot is instructed to cite the specific regulation or link from which it extracted the information.

🚀 Deployment
The CI/CD pipeline on build-01 ensures that any changes to the workflow JSON files are version-controlled and ready for staging/production deployment.
