#external module  import 
from core.models.models import User
from typing import List,Optional
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.sql.expression import null
from core.schemas import schemas
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

#local modul e import 
from core.crud import crud
from  core.settings import  SECRET_KEY , ALGORITHM , ACCESS_TOKEN_EXPIRE_MINUTES 
from  core.helper import  create_access_token, authenticate_user, get_current_active_user
from core.database.session import current_db
app = FastAPI()
import enum 

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://192.168.234.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




# User Block 

class AIStatus(enum.Enum):
    VOICE = "VOICE",
    ACTION = "ACTION",
    RESSOURCE = "RESSOURCE"
    INFORMATION = "INFORMATION"
    WARNING = "WARNING"


# set up  of a post route for user creation
@app.post("/users/", response_model=schemas.UserShow)
async def create_user(user: schemas.UserCreate, db: Session = Depends(current_db) ):
    db_user =  crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    else : 
        if user.geo_address:
            geo_address =  crud.create_geoAddress(db, user.geo_address)
            user.id_geoaddress = geo_address.id
    return  crud.create_user(db=db, user=user)
    
# set up  of a post route to retrieve all user collections in a db
@app.get("/users/",response_model=List[schemas.UserShow])
async def get_all_users(db: Session = Depends(current_db),  token: str = Depends(get_current_active_user)):
    db_users =  crud.get_users(db)
    return db_users

@app.get("/users/{user_id}", response_model=schemas.UserShow,)
async def get_user(user_id: int, db: Session = Depends(current_db), token: str = Depends(get_current_active_user)):
    db_user =  crud.get_user(db, user_id=user_id)
    return db_user

@app.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(current_db), token: str = Depends(get_current_active_user)):
    db_user =  crud.get_user(db, user_id=user_id)
    if not db_user :
           raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"User with id {user_id} does not exist",
        )
    crud.delete_user(db, user_id= user_id)
    return { "detail" : f"User With id {user_id} was successfully deleted", "user" :  db_user }
#  Update User with provide all user's modified information 
@app.put("/users/{user_id}")
async def update_user(user_id: int, user : schemas.UserUpdate, db: Session = Depends(current_db) ,  token: str = Depends(get_current_active_user)):
    db_user = crud.get_user(db, user_id=user_id)
    
    if not db_user :
           raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"User with id {user_id} does not exist",
        )
    user.id  = user_id
    if user.geo_address:
        if not db_user.id_geoaddress :
            geo_address =  crud.create_geoAddress(db, user.geo_address)
            user.id_geoaddress = geo_address.id
        else :
            user.geo_address.id = db_user.id_geoaddress
            geo_address =  crud.update_geoAddress(db, db_user.id_geoaddress,  user.geo_address)
            user.id_geoaddress = geo_address["id"]
    new_user = crud.update_user(db, user_id= user_id, values=user )
    # print(user)
    return { "detail" : f"User With id {user_id} was successfully updated", "user" :  new_user }

#  Update User with provide only user's modified information 
@app.patch("/users/{user_id}")
async def update_user(user_id: int, user : schemas.UserUpdate, db: Session = Depends(current_db), token: str = Depends(get_current_active_user)):
    db_user = crud.get_user(db, user_id=user_id)
    
    if not db_user :
           raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"User with id {user_id} does not exist",
        )
    update_user = user.dict(exclude_unset=True)
    new_user = crud.patch_user(db, user_id= user_id, values=update_user )
    # print(user)
    return { "detail" : f"User With id {user_id} was successfully updated", "user" :  new_user }
    
# set up  of a post route for user authentication, this route return an JWT token 
@app.post("/login_check/", response_model=schemas.Token)
async def  login_check(login: schemas.Login, db: Session = Depends(current_db)):

    # this function check if the user exist in databse and if credentials are right
    user =  authenticate_user(login, db)
    # if authenticate_user get something else except a user 
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires =  timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token =   create_access_token(
        data={"sub":  user.email  }, expires_delta=access_token_expires
    )
    return { "user" : user,"token": access_token, "token_type": "bearer" }


#Propostion Block
@app.post("/ai/", response_model=schemas.AIShow)
def create_ai(ai: schemas.AICreate, db: Session = Depends(current_db), token: str = Depends(get_current_active_user)):
    current_user = token
    if not (hasattr(schemas.AIStatus ,ai.type)) :
        raise HTTPException(status_code=400, detail=f"type of ai must be VOICE , INFORMATION ,WARNING...")
    db_ai =   crud.create_ai(db, ai)
    fake_res = {"id" :db_ai.id,"type" : AIStatus.VOICE, "context" : "ia talk to you" }
    return fake_res



