````markdown
# SupportWise AI

A production-style AI customer support assistant backend built with FastAPI, PostgreSQL, Docker, semantic retrieval, and local LLM integration.

## What This Project Does

SupportWise AI receives user messages, stores conversation history, retrieves semantically similar previous messages, and generates AI-powered responses using a local LLM through Ollama.

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- Sentence Transformers
- Ollama / Llama 3.2

## Core Features

- REST API with FastAPI
- Chat endpoint
- PostgreSQL message storage
- Semantic embeddings
- Cosine similarity retrieval
- Local LLM response generation
- Docker Compose setup
- Swagger API documentation

## Current Architecture

User message  
→ FastAPI `/chat` endpoint  
→ PostgreSQL message storage  
→ Sentence embedding generation  
→ Semantic memory retrieval  
→ Prompt construction  
→ Ollama / Llama 3.2  
→ AI response

## API Endpoints

### Health Check

```http
GET /health
```

### Chat

```http
POST /chat
```

Example request:

```json
{
  "message": "I need help tracking my order."
}
```

## Project Roadmap

See `PROJECT_PLAN.md` for sprint history and future improvements.

## Status

This project is currently under active development.
````
