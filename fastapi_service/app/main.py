from fastapi import FastAPI, Depends, status
from typing import List
from database import engine, get_db
import models
from schemas import UserBase
from models import User
from sqlalchemy.orm import Session
from datetime import datetime

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get('/')
def index():
    return { 'message': 'Hola Karstec!', 'time': datetime.now() }

@app.get('/users', status_code=status.HTTP_200_OK, response_model=List[UserBase])
def get_all_users(db: Session = Depends(get_db)):
    all_users = db.query(User).all()
    return all_users

@app.post('/users', status_code=status.HTTP_201_CREATED, response_model=UserBase)
def create_user(post_user: UserBase , db: Session = Depends(get_db)):
    new_user = User(**post_user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user.__dict__