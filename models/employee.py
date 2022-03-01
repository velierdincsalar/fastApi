from pydantic import BaseModel

class Employee(BaseModel):
    name:str
    surname:str
    email:str
    password:str