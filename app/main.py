from fastapi import FastAPI

app = FastAPI(title="SupportWise AI")


@app.get("/health")
def health_check():
    return {"status": "ok"}