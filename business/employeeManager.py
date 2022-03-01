
from models.employee import Employee
from config.db import conn
from schemas.employee import employeeEntity,employeesEntity


def addEmployee(employee :Employee ):
        return employeeEntity(conn.bookstore.employee.insert_one(dict(employee)))

def findAllEmployees():
    return employeeEntity(conn.bookstore.employee.find())