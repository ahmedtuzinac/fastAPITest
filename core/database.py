# --------- DEPENDENCIES ---------- # 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# -------- PROJECT imports -------- #


SQLALCHEMY_DATABASE_URL = \
"postgresql://postgres:ahmed@localhost:5433/project6th"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()