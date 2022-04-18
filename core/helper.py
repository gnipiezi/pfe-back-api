#external module  import 
from core.schemas import schemas
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime, timedelta , date
from passlib.context import CryptContext
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, FastAPI, HTTPException,status
from sqlalchemy.orm import Session

#local modul e import 
from  .settings import  SECRET_KEY , ALGORITHM  
from core.crud import crud
from core.database.session import current_db 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login_check")

# compare hash password to plain text password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# use to hash password , then this will be useful for persist the hashed password in db 
def get_password_hash(password):
    return pwd_context.hash(password)

# check if user exist in the database or if the password is correct 
def authenticate_user(login, db: Session = Depends(current_db) ):
    user  = crud.get_user_by_email(db, email =login.username)
    if not user:
        return False
    if not verify_password(login.password,  user.password):
        return False
    return user
# create token after provide right user authentication
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
def get_current_user(token: str = Depends(oauth2_scheme) ,  db: Session = Depends(current_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        # exp  = payload.get("exp")
        # print(exp)
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = crud.get_user_by_email(db=db, email=email)
    if user is None:
        raise credentials_exception
    return user

def get_current_active_user(current_user:  schemas.User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
