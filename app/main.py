from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
import logging

from .db import engine, SessionLocal
from .models import Base, Message
from .embeddings import embed
from .retrieval import retrieve_similar_messages
from .llm import ask_llama
from .knowledge_base import load_store_policy
import json

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


app = FastAPI(title="SupportWise AI")

Base.metadata.create_all(bind=engine)


class ChatRequest(BaseModel):
    message: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/messages")
def get_messages(db: Session = Depends(get_db)):
    messages = db.query(Message).order_by(Message.id.desc()).all()

    return [
        {
            "id": msg.id,
            "role": msg.role,
            "content": msg.content,
        }
        for msg in messages
    ]



@app.post("/chat")
def chat(req: ChatRequest, db: Session = Depends(get_db)):
    logger.info(f"Received message: {req.message}")

    user_embedding = embed(req.message)

    user_message = Message(
        role="user",
        content=req.message,
        embedding=json.dumps(user_embedding),
    )

    db.add(user_message)
    db.commit()
    db.refresh(user_message)

    similar_messages = retrieve_similar_messages(
        db=db,
        query_embedding=user_embedding,
        exclude_message_id=user_message.id,
    )

    memory_text = "\n".join(
        [f"- {item['content']}" for item in similar_messages]
    )

    store_policy = load_store_policy()

    prompt = f"""
    You are SupportWise AI, a helpful customer support assistant for an online store.

    Store policy:
    {store_policy}

    Relevant previous messages:
    {memory_text}

    User message:
    {req.message}

    Answer based on the store policy when possible.
    If the policy does not contain the answer, ask the user for more details.
    Keep the answer clear and concise.
    """

    bot_reply = ask_llama(prompt)

    logger.info("AI response generated successfully")

    return {
        "reply": bot_reply,
        "message_id": user_message.id,
        "memory": similar_messages,
    }