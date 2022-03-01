import imp
from fastapi import FastAPI
from routes.user import user
from routes.employee import employee
from routes.book import book
from routes.register import register
app = FastAPI()

app.include_router(user)
app.include_router(employee)
app.include_router(book)
app.include_router(register)


