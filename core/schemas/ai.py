 # external moduls import
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime, timedelta , date
import enum 
#local modul  import 
from  .user import User
class AIStatus(enum.Enum):
    VOICE = "VOICE",
    ACTION = "ACTION",
    RESSOURCE = "RESSOURCE"
    INFORMATION = "INFORMATION"
    WARNING = "WARNING"


class AIBase(BaseModel):
    type  : Optional[str] = "VOICE"
    context : Optional[str]


class AICreate(AIBase):
    pass
# class AIShow(BaseModel):
#     id  : Optional[int] = None 
#     type  : Optional[enum.Enum] 
#     context : Optional[str]
#     class Config:
#       orm_mode = True
class AIShow(BaseModel):
    id  : Optional[int] = None 
    type  : Optional[enum.Enum] 
    context : Optional[str]
    class Config:
      orm_mode = True

  
class AI(BaseModel):
    id  : int 
    class Config:
        orm_mode = True

