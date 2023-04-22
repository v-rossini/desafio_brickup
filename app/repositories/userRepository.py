from database import models
from schemas.user import UserCreate

def get_user(user_id: int):
    return models.User.filter(models.User.id == user_id).first()

def get_user_by_username(username: str):
    return models.User.filter(models.User.username == username).first()

def create_user(user: UserCreate):
    fake_hash = user.password + "1"
    db_user = models.User(username = user.username, hashed_password = fake_hash)
    db_user.save()
    return db_user

def get_files_from_user(user_id: int):
    return list(models.User.filter(models.User.id == user_id).items)