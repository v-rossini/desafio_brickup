from database import models
from schemas.file import PDFFileCreate

def create_file_for_user(file: PDFFileCreate, user_id: int):
    db_file = models.PDFFile(filename = file.filename, user_id=user_id)
    db_file.save()
    return db_file

def get_files_from_user(user_id: int):
    db_user = models.User.filter(models.User.id == user_id).first()
    db_list = list(db_user.files)
    return db_list

def get_file(file_id: int):
    return models.PDFFile.filter(models.PDFFile.id == file_id).first()