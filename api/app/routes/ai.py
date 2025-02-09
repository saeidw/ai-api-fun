# Routes related to AI

import requests
from fastapi import APIRouter, Request

router = APIRouter(prefix="/ai", tags=["AI"])

OLLAMA_URL = "http://ollama_ai:11434/api/generate"

# Simple route to test if the API is running
@router.get("/")
def root():
    return {"message": "AI API is running!"}

@router.post("/generate")
async def generate_response(request: Request):
    promptBody = await request.json()
    data = {
        "model": "mistral",
         "prompt": promptBody["prompt"],
          "stream": False
          }
    response = requests.post(OLLAMA_URL, json=data)
    return response.json()
