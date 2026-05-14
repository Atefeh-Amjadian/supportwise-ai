from sentence_transformers import SentenceTransformer

_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def embed(text: str) -> list[float]:
    vector = _model.encode([text], normalize_embeddings=True)[0]
    return vector.tolist()