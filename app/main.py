from fastapi import FastAPI

from database.dbConnection import start_db

from router import userRouter, fileRouter, itemRouter

start_db()

app = FastAPI()
app.include_router(userRouter.router) 
app.include_router(fileRouter.router) 
app.include_router(itemRouter.router)


@app.get("/")
def index():
    return "olar!"

