from sqlalchemy.sql.functions import current_user
from core.database.database  import SessionLocal, engine
from core.models import  models
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

current_db = get_db