# SupportWise AI - Project Plan

## Project Goal

SupportWise AI is a production-style AI customer support assistant backend.

The goal is to build a real-world backend system that can receive user messages, store conversation history, retrieve relevant context, and generate AI-powered responses using a local LLM.

## Main Objectives

- Learn backend engineering practices
- Build a portfolio-ready AI backend project
- Practice FastAPI, PostgreSQL, SQLAlchemy, Docker, embeddings, and LLM integration
- Prepare for Junior AI Backend / Python Engineer roles

## Current Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- Sentence Transformers
- Ollama / Llama 3.2

## Completed Sprints

### Sprint 1: FastAPI Foundation
- Created FastAPI app
- Added `/health` endpoint
- Tested Swagger API docs

### Sprint 2: PostgreSQL Integration
- Added SQLAlchemy
- Created Message model
- Connected FastAPI to PostgreSQL
- Stored chat messages in database

### Sprint 3: Dockerization
- Added Dockerfile
- Added docker-compose.yml
- Containerized FastAPI and PostgreSQL

### Sprint 4: Semantic Memory
- Added sentence embeddings
- Stored embeddings in database
- Implemented cosine similarity
- Added semantic retrieval

### Sprint 5: LLM Integration
- Connected backend to Ollama
- Built prompt from user message and retrieved memory
- Generated AI response using Llama 3.2

## Upcoming Improvements

### Sprint 6: Production Readiness
- Improve README
- Add environment configuration
- Add logging
- Improve project structure and documentation

### Sprint 7: Retrieval Quality
- Add similarity threshold
- Exclude current message from memory
- Improve prompt formatting
- Tune top_k retrieval

### Future Features
- PDF/text document support
- Authentication
- pgvector
- Deployment
- Frontend chat widget