from database.database import db, db_state_default
from fastapi import Depends
from database import models

def start_db():
    db.connect()
    db.create_tables([models.User, models.PDFFile, models.Item])
    db.close()


async def reset_db_state():
    db._state._state.set(db_state_default.copy())
    db._state.reset()


def get_db(db_state=Depends(reset_db_state)):
    try:
        db.connect()
        yield
    finally:
        if not db.is_closed():
            db.close()