from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite+pysqlite:///todolisto.db")
SesionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
def get_db():
    db = SesionLocal()
    try:
        yield db
    finally:
        db.close()