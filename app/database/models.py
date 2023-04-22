from peewee import (Model, DateTimeField, ForeignKeyField,
                    CharField, IntegerField, UUIDField)
from datetime import datetime
from .database import db


class DatabaseModel(Model):
    created_at = DateTimeField(default= datetime.now)
    updated_at = DateTimeField(default= datetime.now)

    class Meta:
        database = db

class User(DatabaseModel):
    username = CharField(unique=True)
    password = CharField()

class PDFFile(DatabaseModel):
    filename = CharField() 
    user = ForeignKeyField(User, backref="files")

class Item(DatabaseModel):
    item = IntegerField(primary_key=True)
    description = CharField()
    unity = CharField()
    quantity = IntegerField()
    file = ForeignKeyField(PDFFile, backref="items")










