#external module  import 
from sqlalchemy.orm import Session

#local modul e import 
from ..models import models
from core.schemas import schemas
from sqlalchemy import delete, update

def create_geoAddress(db: Session, geo_address: schemas.GeoAddress):
    db_geo_address = models.GeoAddress(**geo_address.dict())
    db.add(db_geo_address)
    db.commit()
    db.refresh(db_geo_address)
    return db_geo_address

def update_geoAddress(db: Session, geo_address_id : int  ,  values: schemas.GeoAddressUpdate):
    stmt = update(models.GeoAddress).where(models.GeoAddress.id == geo_address_id).values(**values.dict()).execution_options(synchronize_session="fetch")
    result  = db.execute(stmt)
    #  stmt = update(models.GeoAddress).where(models.GeoAddress.id == geo_address_id).values(id = values.id , postal_code = values.postal_code , country = values.country,street = values.street, street_number = values.street_number
    #    , city = values.city
    
    # ).execution_options(synchronize_session="fetch")
    print(result.last_updated_params())
    return result.last_updated_params()
