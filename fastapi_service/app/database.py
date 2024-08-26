from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv();

user = os.getenv('USER')
password = os.getenv('PASS')
host = os.getenv('HOST')
port = os.getenv('PORT')
domain = os.getenv('DOMAIN')
db = os.getenv('DB')

#SQLALCHEMY_DATABASE_URL = 'oracle+oracledb://{user}:{password}@{host}/{db}'
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:postgres@localhost/test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 
