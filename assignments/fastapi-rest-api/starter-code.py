from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Books API")

books = []


class BookInput(BaseModel):
    title: str
    author: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/books")
def list_books():
    # TODO: Return the current list of books.
    return books


@app.post("/books", status_code=201)
def create_book(book: BookInput):
    # TODO: Assign an ID, add the book to the list, and return it.
    return {"message": "Implement book creation"}


# TODO: Add GET, PUT, and DELETE endpoints for /books/{book_id}.

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
