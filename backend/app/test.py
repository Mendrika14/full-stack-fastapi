from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

plain_password = "password"
hashed_password = pwd_context.hash(plain_password)

print(hashed_password)