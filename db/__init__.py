import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_url = os.getenv("DB_CONNECTION_URL")
if db_url is None:
    print("empty db url")
    exit(1)
    
engine = create_engine(db_url)
session = sessionmaker(bind=engine,autocommit=False)
Base = declarative_base()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()