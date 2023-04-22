from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash:
    def encrypt(password: str):
        return password_context.hash(password)

    def verify(original_str: str ,hashed_str: str):
        return password_context.verify(original_str, hashed_str)