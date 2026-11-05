from fastapi import FastAPI
from models.chat import ChatRequest
from services.chat_service import generate_response


app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def version():
    return {
        "project_name": "ai-api-service",
        "version": "0.1.0"
    }


@app.post("/chat")
def chat(data: ChatRequest):
    response = generate_response(data.prompt)
    return {"response": response}