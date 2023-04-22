from schemas.token import TokenData
from datetime import datetime, timedelta
from jose import JWTError, jwt

SECRET_KEY = "04fa3b93f708a69f62cf63bf0f4caa6ca8556c815e096b7a9598e86169d2d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30




class TokenValidator:
    def generate_token(data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def verify_token(token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                return False
            return TokenData(username=username)
        except JWTError:
            return False