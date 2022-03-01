from atexit import register
from fastapi import APIRouter

from models.register import Register
from config.db import conn
from schemas.register import registerEntity,registersEntity
from business.registerManager import addRegister,findAllRegisters

register = APIRouter()

@register.get('/getAllRegister')
async def findAllRegisters():
    return findAllRegisters()

@register.post('/createRegister')
async def createRegister(register : Register):
    return addRegister(register)