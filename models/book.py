from pydantic import BaseModel

class Book(BaseModel):
    name:str
    category:str
    author:str
    pages:str