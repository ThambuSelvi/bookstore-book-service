from fastapi import FastAPI

app = FastAPI(title="Book Service")

books = {
    101: {"id": 101, "title": "DevOps Guide", "price": 29.99},
    102: {"id": 102, "title": "Microservices 101", "price": 39.99}
}

@app.get("/")
def home():
    return {"service": "Book Service", "status": "Running"}

@app.get("/books/{book_id}")
def get_book(book_id: int):
    book = books.get(book_id)
    if book:
        return book
    return {"error": "Book not found"}
