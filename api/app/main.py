# This is the entry-point for FastAPI

# import app.routes

from fastapi import FastAPI
from app.routes import ai


app = FastAPI()

app.include_router(ai.router)

@app.get("/")
def root():
    return {"message": "API is running!"}
