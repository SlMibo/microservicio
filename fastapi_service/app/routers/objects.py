from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud
from ..database import get_db

router = APIRouter()

@router.post("/users/", response_model=schemas.UserResponse, summary="Crear un usuario")
def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

# @router.put("/objetos/{ojtid}/", response_model=schemas.ObjetoUpdated, summary="Actualizar un Objeto")
# def update_objeto(ojtid: int, update: schemas.ObjetoUpdated, db: Session = Depends(get_db)):
#     db_objeto = crud.update_objeto(db=db, ojtid=ojtid, update=update)
#     if db_objeto is None:
#         raise HTTPException(status_code=404, detail="Objeto no encontrado")
#     return db_objeto