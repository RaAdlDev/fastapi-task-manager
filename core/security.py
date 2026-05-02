from core.settings import settings
from fastapi import HTTPException, Depends
from jose import JWTError, jwt 
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
oauth = OAuth2PasswordBearer(tokenUrl="login")
ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 60


pswrd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def hash_pswrd(password: str):
    return pswrd_context.hash(password)

def create_token(data: dict):
    to_encode = data.copy()
    time = datetime.utcnow() + timedelta(minutes= ACCESS_TOKEN_DURATION)
    to_encode.update({"exp": time})
    return jwt.encode(to_encode, settings.secret_key, algorithm=ALGORITHM)

def verify_pswrd(plain_password, code_pasword):
    return pswrd_context.verify(plain_password, code_pasword)

def decode(token: str = Depends(oauth)):
    try:
        load = jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM] )
        username = load.get("sub")
        if not username:
            raise HTTPException(status_code = 401, detail= "User Not Found")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Not Allowed")
        