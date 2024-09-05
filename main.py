from fastapi import FastAPI, HTTPException
from models import Book
from data import books

app = FastAPI()



#Endpoint para obter todos os livros
@app.get("/books/")
def get_books():
    return books

#Endpoint para obter um livro pelo ID
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book

    raise HTTPException(status_code=404, detail="Book not Found")

#Endpoint para criar um novo livro

@app.post("/books/")
def create_book(book: Book):
    books.append(book)
    return book

#Endpoint para deletar um livro pelo ID

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book.id == book_id:
            books.remove(book)
            return {"message": "Book deleted succesfuly"}

    raise HTTPException(status_code=404, detail="Bool Not Found")


