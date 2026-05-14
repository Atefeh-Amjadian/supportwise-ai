import json
import math
from sqlalchemy.orm import Session

from .models import Message


def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))

    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))

    if norm_a == 0 or norm_b == 0:
        return 0.0

    return dot / (norm_a * norm_b)


def retrieve_similar_messages(
    db: Session,
    query_embedding: list[float],
    top_k: int = 3,
):
    messages = (
        db.query(Message)
        .filter(Message.embedding.isnot(None))
        .filter(Message.role == "user")
        .all()
    )

    scored_messages = []

    for message in messages:
        stored_embedding = json.loads(message.embedding)
        score = cosine_similarity(query_embedding, stored_embedding)

        scored_messages.append(
            {
                "id": message.id,
                "content": message.content,
                "score": score,
            }
        )

    scored_messages.sort(key=lambda item: item["score"], reverse=True)

    return scored_messages[:top_k]