# Routes related to AI

import requests
from fastapi import APIRouter

router = APIRouter(prefix="/ai", tags=["AI"])

OLLAMA_URL = "http://ollama_ai:11434/api/generate"

@router.post("/generate")
def generate_response(prompt: str):
    data = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=data)
    return response.json()
