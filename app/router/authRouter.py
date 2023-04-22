from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from schemas import user, token
from database.dbConnection import get_db 
from repositories.userRepository import get_user_by_username
from utils.hashing import Hash
from utils.JWT import TokenValidator


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/", dependencies=[Depends(get_db)])
def auth(credentials: OAuth2PasswordRequestForm = Depends()):
#def auth(credentials: user.UserAuth):
    db_user = get_user_by_username(credentials.username)
    if (db_user is None):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if not Hash.verify(credentials.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = TokenValidator.generate_token( data={"sub": db_user.username} )
    return {"access_token": access_token, "token_type": "bearer", "user_id": db_user.id}