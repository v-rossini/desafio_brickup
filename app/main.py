from fastapi import FastAPI
from schemas.user import User
from schemas.item import Item
from schemas.file import PDFFile
from database.dbConnection import start_db

start_db()

app = FastAPI()

@app.get("/")
def index():
    return "olar"

@app.post("/user")
def create_user(body: User):
    return "bla"

@app.post("/item")
def create_user(body: Item):
    return "bla"

@app.post("/file")
def create_user(body: PDFFile):
    return "bla"