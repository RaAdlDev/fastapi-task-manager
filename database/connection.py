from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from core.settings import settings
engine = create_engine(settings.database_url)
SesionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
def get_db():
    db = SesionLocal()
    try:
        yield db
    finally:
        db.close()