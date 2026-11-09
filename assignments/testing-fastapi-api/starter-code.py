from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Books API for Testing")
books = []
next_book_id = 1


class BookInput(BaseModel):
    title: str
    author: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/books")
def list_books():
    return books


@app.post("/books", status_code=201)
def create_book(book: BookInput):
    global next_book_id
    new_book = {"id": next_book_id, **book.model_dump()}
    next_book_id += 1
    books.append(new_book)
    return new_book


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.put("/books/{book_id}")
def update_book(book_id: int, book_update: BookInput):
    for book in books:
        if book["id"] == book_id:
            book.update(book_update.model_dump())
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book["id"] == book_id:
            return books.pop(index)
    raise HTTPException(status_code=404, detail="Book not found")
