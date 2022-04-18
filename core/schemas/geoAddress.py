# external moduls import
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime, timedelta , date
#local modul  import 


class GeoAddressBase(BaseModel):
    country : Optional[str] = None
    postal_code : Optional[str] = None
    city : Optional[ str] = None
    street : Optional[str] = None
    street_number : Optional[str] = None

class GeoAddressCreate(GeoAddressBase):
    pass

class GeoAddressUpdate(GeoAddressBase):
    pass

class GeoAddress(GeoAddressBase):
    id  : Optional[int] = None 
    class Config:
       orm_mode = True