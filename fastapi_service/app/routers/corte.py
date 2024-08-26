from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud, models
from ..database import get_db

router = APIRouter()

@router.get("/detalles_titulos_deuda/", response_model=List[schemas.DetallesTitulosDeuda])
def read_detalles_titulos_deuda(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    detalles_titulos_deuda = crud.get_detalles_titulos_deuda(db, skip=skip, limit=limit)
    return detalles_titulos_deuda
