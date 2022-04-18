 #external module  import 
from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float, Enum, Text
from sqlalchemy.orm import relationship, backref
import enum
from sqlalchemy.sql.expression import false

from sqlalchemy.sql.sqltypes import DateTime 
#local modul e import 
from ..database.database import Base

class AIStatus(enum.Enum):
    VOICE = "VOICE",
    ACTION = "ACTION",
    RESSOURCE = "RESSOURCE"
    INFORMATION = "INFORMATION"
    WARNING = "WARNING"


class AI(Base):
    __tablename__ = "ai"
    id = Column(Integer,  primary_key=True) 
    type  = Column(Enum(AIStatus))
    context = Column(String(255))
    user_id =Column(Integer,  ForeignKey("user.id") )



