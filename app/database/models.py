from peewee import (Model, DateTimeField, ForeignKeyField,
                    CharField, IntegerField)
from datetime import datetime
from .database import db


class DatabaseModel(Model):
    created_at = DateTimeField(default= datetime.now)
    updated_at = DateTimeField(default= datetime.now)

    class Meta:
        database = db

class User(DatabaseModel):
    username = CharField(unique=True)
    hashed_password = CharField()

class PDFFile(DatabaseModel):
    filename = CharField() 
    user = ForeignKeyField(User, backref="files")

class Item(DatabaseModel):
    item = IntegerField()
    description = CharField(null = True)
    unit = CharField(null = True)
    amount = IntegerField(null = True)
    file = ForeignKeyField(PDFFile, backref="items")










