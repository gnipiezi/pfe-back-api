#external module  import 
from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float, Enum, Text
from sqlalchemy.orm import relationship, backref
import enum
from sqlalchemy.sql.expression import false

from sqlalchemy.sql.sqltypes import DateTime 
#local modul e import 
from ..database.database import Base

# User table definition

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255))
    first_name =Column(String(255) )
    last_name =Column(String(255))
    last_name =Column(String(255))
    password = Column(String(255))
    born_date =  Column(Date())
    address = Column(String(255))
    phone_number = Column(String(255))
    cell_phone_number = Column(String(255))
    is_active = Column(Boolean, default=True)
    id_geoaddress = Column(Integer,  ForeignKey("geoAddress.id") , nullable= True)
    geo_address = relationship("GeoAddress",backref=backref("user", uselist=False))
