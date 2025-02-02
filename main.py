from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import and_
from typing import List, Optional
from db import get_db
from model import WikiData

app = FastAPI()

@app.get("/wikidata")
def get_wikidata(
    db: Session = Depends(get_db)
):
    """Fetch wiki data by a specific key-value pair."""
    result = db.query(WikiData).all()
    return { "wiki": [row.title for row in result] }


