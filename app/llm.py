import httpx


OLLAMA_URL = "http://host.docker.internal:11434/api/generate"


def ask_llama(prompt: str) -> str:
    response = httpx.post(
        OLLAMA_URL,
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False,
        },
        timeout=300,
    )

    data = response.json()

    return data["response"]