from fastapi import FastAPI, Depends, HTTPException
from typing import List
from schemas  import user, item, file
from database.dbConnection import start_db, get_db
from repositories import userRepository, fileRepository, itemRepository
from database import models
from router import userRouter, fileRouter, itemRouter

start_db()

app = FastAPI()
app.include_router(userRouter.router) 
app.include_router(fileRouter.router) 
app.include_router(itemRouter.router)


@app.get("/")
def index():
    return "olar!"

