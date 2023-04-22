from database import models
from schemas.user import UserCreate
from utils.hashing import Hash

def get_user(user_id: int):
    return models.User.filter(models.User.id == user_id).first()

def get_user_by_username(username: str):
    return models.User.filter(models.User.username == username).first()

def create_user(user: UserCreate):
    hashed_pw = Hash.encrypt(user.password)
    db_user = models.User(username = user.username, hashed_password = hashed_pw)
    db_user.save()
    return db_user

