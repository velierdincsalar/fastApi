
from models.user import User
from config.db import conn
from schemas.user import userEntity,usersEntity


def addUser(user :User ):
        return usersEntity(conn.bookstore.user.insert_one(dict(user)))

def findAllBooks():
    return usersEntity(conn.bookstore.user.find())