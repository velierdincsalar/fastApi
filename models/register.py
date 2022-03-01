from pydantic import BaseModel

class Register(BaseModel):
    userId:str
    bookId:str
    employeeId: str
    startDate:str
    endDate:str