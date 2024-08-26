### Microservicio de Gestión de Objetos y Deudas utilizando FastAPI y SQLAlchemy para interactuar con la base de datos.

#### 1. Preparación del Entorno
- Lo primero es crear el entorno
<pre> python -m venv fastapi_env </pre>
- Debe activarse 
  - *En Windows*
<pre> fastapi_env\Scripts\activate.bat </pre>
- Ahora es posible la instalación de dependencias:

<pre>pip install fastapi uvicorn sqlalchemy oracledb alembic psycopg2-binary python-dotenv</pre>

- Crear Estructura de Proyecto:
Estructura básica del proyecto:

<pre>
microservice/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   ├── routers/
│   │   ├── __init__.py
│   │   └── objects.py
├── alembic/
│   └── ...
├── Dockerfile
├── requirements.txt
└── docker-compose.yml
</pre>

#### 2. Configuración de la Base de Datos
***database.py:*** Configura la conexión con la base de datos.
<pre>
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_ORACLE = "oracle+oracledb://username:password@host:port/service_name"

DATABASE_POSTGRESQL = "postgresql://username:password@host:port/database_name"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
</pre>

#### 3. Modelado de Datos
***models.py:*** Define las tablas de la base de datos como clases de SQLAlchemy.
<pre>
from database import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    name = Column(String,nullable=False)
    surname = Column(String,nullable=False)
    email = Column(String,nullable=False)
    password = Column(String,nullable=False)
</pre>

#### 4. Esquemas de Datos (Schemas)
***schemas.py:*** Define los esquemas de entrada y salida de datos.
<pre>
from pydantic import BaseModel

class UserBase(BaseModel):
  name: str
  surname: str
  email: str
  password: str

  class Config:
    orm_mode = True

class UserRequest(UserBase):
  class Config:
    orm_mode = True

class UserResponse(UserBase):
  id: int

  class Config:
    orm_mode = True
</pre>

#### 5. Crear endpoints
***main.py:*** Punto de entrada de la aplicación.
<pre>
from fastapi import FastAPI, Depends, status
from typing import List
from database import engine, get_db
import models
from .schemas import UserRequest, UserResponse
from models import User
from sqlalchemy.orm import Session
from datetime import datetime

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get('/')
def index():
    return { 'message': 'Hola Karstec!', 'time': datetime.now() }

@app.get('/users', status_code=status.HTTP_200_OK, response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    all_users = db.query(User).all()
    return all_users

@app.post('/users', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(post_user: UserRequest, db: Session = Depends(get_db)):
    new_user = User(**post_user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user.__dict__
</pre>

#### 8. Ejecución Local
Ejecuta la aplicación localmente para probar:
bash

<pre> uvicorn main:app --reload </pre>

#### 9. Dockerización
***Dockerfile:***

<pre>
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
</pre>

***docker-compose.yml:***

<pre>
yaml
Copiar código
version: '3.7'

services:
  db:
    image: oracleinanet/oracle-12c
    environment:
      - ORACLE_PWD=yourpassword
    ports:
      - "1521:1521"

  api:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - db
</pre>

#### 10. Despliegue y Pruebas
***Ejecuta Docker Compose:***
<pre> docker-compose up --build </pre>