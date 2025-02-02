from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import and_
from typing import List, Optional
from db import get_db
from model import WikiData

app = FastAPI()

@app.get("/")
def get_index():
    return "OK"

@app.get("/titles")
def get_wikidata(
    db: Session = Depends(get_db)
):
    """Fetches a list of article titles - only returns titles."""
    result = db.query(WikiData).all()
    return { "titles": [row.title for row in result] }

@app.get("/search/title")
def search_wikidata(
    title: str,
    db: Session = Depends(get_db)
):
    """Fetches a list of articles based on a search of their titles - returns the content."""
    result = db.query(WikiData).filter(WikiData.title.like(f"%{title}%")).all()
    resultArray = []
    for row in result:
        resultArray.append ( {"title": row.title, "content": row.content} )
    return resultArray
