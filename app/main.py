from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from .db import engine, SessionLocal
from .models import Base, Message

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


@app.post("/chat")
def chat(req: ChatRequest, db: Session = Depends(get_db)):
    user_message = Message(
        role="user",
        content=req.message,
    )

    db.add(user_message)
    db.commit()
    db.refresh(user_message)

    return {
        "reply": "Message received ✅",
        "message_id": user_message.id,
    }