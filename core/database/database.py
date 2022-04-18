#external module  import 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#local modul e import 
from ..settings import SERVER_URL, USER_NAME , USER_PASSWORD , DB_NAME
SQLALCHEMY_DATABASE_URL = f"mysql://{USER_NAME}:{USER_PASSWORD}@{SERVER_URL}/{DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()