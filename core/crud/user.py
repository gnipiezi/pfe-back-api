#external module  import 
from sqlalchemy.orm import Session

#local modul e import 
from ..models import models
from core.schemas import schemas
from ..helper  import get_password_hash
from sqlalchemy import delete, update

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()
def delete_user(db: Session, user_id:  int ):
    # user  = get_user(db, user_id )
    stmt= delete(models.User).where(models.User.id == user_id).execution_options(synchronize_session="fetch")
    db.execute(stmt)
def update_user(db: Session, user_id:  int , values : schemas.UserUpdate ):
    # print(values)
    stmt = update(models.User).where(models.User.id == user_id).values(email = values.email , first_name = values.first_name, last_name = values.last_name, address =values.address, is_active =values.is_active,
    born_date = values.born_date , cell_phone_number = values.cell_phone_number, phone_number = values.phone_number, id_geoaddress = values.id_geoaddress).execution_options(synchronize_session="fetch")
    result  = db.execute(stmt)
    # print(result.last_updated_params())
    return result.last_updated_params()
def patch_user(db: Session, user_id:  int , values : schemas.UserUpdate ):
    # print(values)
    stmt = update(models.User).where(models.User.id == user_id).values(values).execution_options(synchronize_session="fetch")
    result  = db.execute(stmt)
    # print(result.last_updated_params())
    return result.last_updated_params()
def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = get_password_hash(user.password)
    # user_geoAddress = { user. geo_address.country ,  user. geo_address.city , user. geo_address.postal_code, user. geo_address.street , user. geo_address.street_number}
    db_user = models.User(email = user.email , first_name = user.first_name, last_name = user.last_name, address =user.address, password=fake_hashed_password,is_active=user.is_active,
    born_date = user.born_date , cell_phone_number = user.cell_phone_number, phone_number = user.phone_number, id_geoaddress = user.id_geoaddress)                                                                   
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    # db_user[born_date] =  db_user.born_date.strftime("%%Y/%m/%d")
    return db_user



