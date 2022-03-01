
from fastapi import APIRouter

from models.user import User
from business.userManager import addUser,findAllUsers
user = APIRouter()

@user.get('/getAllBook')
async def findAllUsers():
    return findAllUsers()

@user.post('/createUser')
async def createUser(user : User):
    return addUser(user)