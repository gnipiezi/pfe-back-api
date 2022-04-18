# external moduls import
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime, timedelta , date
from .geoAddress import GeoAddressBase, GeoAddressCreate, GeoAddress
#local modul  import 



class TokenData(BaseModel):
    username: Optional[str] = None




# class that contains the main information about User 
class UserBase(BaseModel):
    email: str
    first_name :str
    last_name : str
    born_date : date
    address : str
    phone_number : str
    cell_phone_number : str
    id_geoaddress : Optional[int] = None
    geo_address : Optional[GeoAddress] = None
    is_active: Optional[bool] =  True


# this class provides Supplement information that will be used for user creation 
class UserCreate(UserBase):
    password: str
    
class UserUpdate(BaseModel):
    email: Optional[str] 
    first_name :Optional[str] 
    last_name : Optional[str] 
    born_date : Optional[date] 
    address : Optional[str] 
    phone_number : Optional[str] 
    cell_phone_number : Optional[str] 
    id_geoaddress : Optional[int] 
    geo_address : Optional[GeoAddress] 
    is_active: Optional[bool] 
    id: Optional[int] 
    class Config:
        orm_mode = True
class UserShow(BaseModel):
    email: Optional[str] 
    first_name :Optional[str] 
    last_name : Optional[str] 
    born_date : Optional[date] 
    address : Optional[str] 
    phone_number : Optional[str] 
    cell_phone_number : Optional[str] 
    id_geoaddress : Optional[int] 
    geo_address : Optional[GeoAddress] 
    is_active: Optional[bool] 
    id: Optional[int] 
    class Config:
        orm_mode = True




# this is only used for user authorization, this class in not a db model 
class Login(BaseModel):
    username: str
    password: str
        
    class Config:
        orm_mode = True

# definitive user class
class User(UserBase):
    id: int
    is_active: bool
    class Config:
        orm_mode = True

# this class is an response_model for Token 
class Token(BaseModel):
    token: str
    token_type: str
    user : UserShow
