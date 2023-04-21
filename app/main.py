from fastapi import FastAPI
from models.user import User
from models.item import Item


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