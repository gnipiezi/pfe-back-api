
#external module  import 
from sqlalchemy.orm import Session

#local modul e import 
from ..models import models
from core.schemas import schemas
from sqlalchemy import delete, update, join , select

# def get_ai(db: Session, ai_id: int):
#     return db.query(models.AI).filter(models.AI.id == ai_id).first()

# def get_ais(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.AI).offset(skip).limit(limit).all()


# def delete_ai( ai_id : int, db: Session ):
#     stmt= delete(models.AI).where(models.AI.id == ai_id).execution_options(synchronize_session="fetch")
#     db.execute(stmt)

# def get_ais_request(db: Session, request_id):
#     return db.query(models.AI).filter(models.AI.request_id == request_id).all()

def create_ai(db: Session, ai: schemas.AI):
    db_ai =  models.AI(**ai.dict())
    # print(db_ai)
    db.add(db_ai)
    db.commit()
    db.refresh(db_ai)
    return db_ai
    
