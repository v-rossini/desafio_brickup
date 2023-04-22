from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing_extensions import Annotated
from repositories import userRepository
from utils.JWT import TokenValidator


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")

credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    token_data = TokenValidator.verify_token(token)
    if not token_data:
        raise credentials_exception
    user = userRepository.get_user_by_username(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user