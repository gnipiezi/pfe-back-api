#external module  import 
from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float, Enum, Text
from sqlalchemy.orm import relationship, backref
import enum
from sqlalchemy.sql.expression import false

from sqlalchemy.sql.sqltypes import DateTime 
#local modul e import 
from ..database.database import Base


class GeoAddress(Base):
    __tablename__ = "geoAddress"
    id = Column(Integer,  primary_key=True) 
    country = Column(String(255))
    postal_code = Column(String(255))
    city = Column(String(255))
    street = Column(String(255))
    street_number = Column(String(255))

