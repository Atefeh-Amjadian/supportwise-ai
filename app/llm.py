import os
import httpx


OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://host.docker.internal:11434/api/generate"
)

MODEL_NAME = os.getenv("MODEL_NAME", "llama3.2")

def ask_llama(prompt: str) -> str:
    try:
        response = httpx.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False,
            },
            timeout=300,
        )

        response.raise_for_status()

        data = response.json()

        return data.get("response", "No response from model.")

    except httpx.TimeoutException:
        return "AI service timeout. Please try again."

    except httpx.ConnectError:
        return "AI service is currently unavailable."

    except Exception as e:
        return f"Unexpected AI error: {str(e)}"