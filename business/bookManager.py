from models.book import Book
from config.db import conn
from schemas.book import bookEntity,booksEntity


def addBook(book :Book ):
    return bookEntity(conn.bookstore.book.insert_one(dict(book)))

def findAllBooks():
    return bookEntity(conn.bookstore.book.find())