# This is the entry-point for FastAPI

from fastapi import FastAPI
from app.routes import ai

app = FastAPI()

app.include_router(ai.router)

@app.get("/")
def root():
    return {"message": "AI API is running!"}
