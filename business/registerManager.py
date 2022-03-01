from models.register import Register
from config.db import conn
from schemas.register import registerEntity,registersEntity


def addRegister(register :Register ):
    
    registerEntity(conn.bookstore.register.find_one({}, { "bookId": register.bookId, "EndDAte" : ""}))
    if registerEntity is null
        return registerEntity(conn.bookstore.register.insert_one(dict(register)))
    else
        return print("kitap verildi şuan alınamaz.")

def findAllRegisters():
    return registerEntity(conn.bookstore.register.find())