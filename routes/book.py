from fastapi import APIRouter

from models.book import Book
from config.db import conn
from schemas.book import bookEntity,booksEntity
from business.bookManager import findAllBooks,addBook

book = APIRouter()

@book.get('/getAllBook')
async def findAllBooks():
    return findAllBooks()

@book.post('/createBook')
async def createBook(book : Book):
    return addBook(book)