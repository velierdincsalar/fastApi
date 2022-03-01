from fastapi import APIRouter


from models.employee import Employee
from config.db import conn
from schemas.user import userEntity,usersEntity
from schemas.employee import employeeEntity,employeesEntity
from business.employeeManager import addEmployee,findAllEmployees
employee = APIRouter()

@employee.get('/getAllEmployee')
async def findAllEmployees():
    return findAllEmployees()

@employee.post('/createEmploye')
async def addEmployee(employee : Employee):
    return addEmployee(employee)