"""Starter code for the FastAPI REST APIs assignment.

Run locally after installing dependencies:
    pip install fastapi uvicorn
    uvicorn starter-code:app --reload
"""

from typing import Dict, List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Books API")


class BookCreate(BaseModel):
    title: str
    author: str


# In-memory store: id -> book payload
books: Dict[int, Dict[str, str | int]] = {}
next_id = 1


@app.get("/health")
def health() -> Dict[str, str]:
    return {"status": "ok"}


@app.get("/books")
def list_books() -> List[Dict[str, str | int]]:
    return list(books.values())


@app.post("/books")
def create_book(payload: BookCreate) -> Dict[str, str | int]:
    global next_id

    book = {"id": next_id, "title": payload.title, "author": payload.author}
    books[next_id] = book
    next_id += 1
    return book


@app.put("/books/{book_id}")
def update_book(book_id: int, payload: BookCreate) -> Dict[str, str | int]:
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")

    books[book_id]["title"] = payload.title
    books[book_id]["author"] = payload.author
    return books[book_id]


@app.delete("/books/{book_id}")
def delete_book(book_id: int) -> Dict[str, str | int]:
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")

    deleted = books.pop(book_id)
    return {"id": deleted["id"], "status": "deleted"}
