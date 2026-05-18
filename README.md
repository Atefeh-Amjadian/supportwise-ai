````markdown
# SupportWise AI

A production-style AI customer support assistant backend built with FastAPI, PostgreSQL, Docker, semantic retrieval, and local LLM integration.

---

# Features

- FastAPI REST API
- PostgreSQL conversation storage
- SQLAlchemy ORM
- Dockerized backend environment
- Semantic embeddings with Sentence Transformers
- Cosine similarity retrieval
- Local LLM integration using Ollama + Llama 3.2
- RAG-style prompt construction
- Store policy knowledge base
- Conversation history endpoint
- Logging and error handling
- Swagger API documentation

---

# Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- Sentence Transformers
- Ollama
- Llama 3.2

---

# Current Architecture

User Message  
→ FastAPI `/chat` endpoint  
→ Generate embedding  
→ Store message in PostgreSQL  
→ Retrieve semantically similar messages  
→ Load store policy knowledge  
→ Build contextual prompt  
→ Send prompt to Ollama  
→ Generate AI response  
→ Return JSON response

---

# API Endpoints

## Health Check

```http
GET /health
```

---

## Chat Endpoint

```http
POST /chat
```

Example request:

```json
{
  "message": "How long does shipping take?"
}
```

Example response:

```json
{
  "reply": "According to our store policy, standard shipping takes 3 to 5 business days.",
  "message_id": 14,
  "memory": []
}
```

---

## Conversation History

```http
GET /messages
```

Returns stored conversation history from PostgreSQL.

---

# Store Knowledge Base

The project includes a simple store policy knowledge base:

- Shipping
- Returns
- Refunds
- Support hours
- Payment methods

This information is injected into prompts to create a basic RAG-style AI support assistant.

---

# How To Run

## 1. Clone the repository

```bash
git clone <your-repository-url>
cd supportwise-ai
```

---

## 2. Create environment variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://postgres:your_password@db:5432/supportwise_ai

OLLAMA_URL=http://host.docker.internal:11434/api/generate

MODEL_NAME=llama3.2
```

---

## 3. Start Ollama

Make sure Ollama is installed and running:

```bash
ollama serve
```

Pull the model if needed:

```bash
ollama pull llama3.2
```

---

## 4. Start Docker services

```bash
docker compose up -d --build
```

---

## 5. Open Swagger Docs

```text
http://localhost:8000/docs
```

---

# Project Structure

```text
supportwise-ai/
│
├── app/
│   ├── main.py
│   ├── db.py
│   ├── models.py
│   ├── embeddings.py
│   ├── retrieval.py
│   ├── llm.py
│   └── knowledge_base.py
│
├── data/
│   └── store_policy.txt
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
├── PROJECT_PLAN.md
└── README.md
```

---

# Current Limitations

- Uses a local CPU-based model
- No authentication system yet
- No vector database yet
- Retrieval is still basic
- No frontend UI yet

---

# Future Improvements

- Vector database integration
- Advanced RAG pipeline
- Authentication and user accounts
- Streaming responses
- Frontend dashboard
- Admin panel
- Better semantic retrieval
- Deployment to cloud infrastructure

---

# Learning Goals Behind This Project

This project was built to learn:

- Backend engineering practices
- AI system architecture
- Retrieval-Augmented Generation (RAG)
- Dockerized AI services
- Database integration
- Semantic search concepts
- Production-style API development

---

# Status

This project is currently under active development and continuously improving.
````
