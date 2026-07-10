from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Books API")


class BookCreate(BaseModel):
    title: str
    author: str
    year: int


# In-memory storage for assignment practice.
books = []
next_id = 1


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/books")
def create_book(payload: BookCreate):
    global next_id

    book = {
        "id": next_id,
        "title": payload.title,
        "author": payload.author,
        "year": payload.year,
    }
    books.append(book)
    next_id += 1
    return book


@app.get("/books")
def list_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.put("/books/{book_id}")
def update_book(book_id: int, payload: BookCreate):
    for index, book in enumerate(books):
        if book["id"] == book_id:
            updated = {
                "id": book_id,
                "title": payload.title,
                "author": payload.author,
                "year": payload.year,
            }
            books[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book["id"] == book_id:
            books.pop(index)
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
