from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class DetallesTitulosDeuda(BaseModel):
    TITID: int
    OBNID: str
    DTDIMPORTE: int
    DTDOBSERVACIONES: str
    BOAID: int

class TituloDeudaBase(BaseModel):
    titcaso: str
    titfechageneracion: datetime
    lipojtid: int

class TituloDeudaCreate(TituloDeudaBase):
    pass

class TituloDeuda(TituloDeudaBase):
    titid: int

    class Config:
        orm_mode = True

class ObjetoBase(BaseModel):
    ojtidentificador1: str
    ojtdistrito: str
    ojtruta: str

class ObjetoCreate(ObjetoBase):
    pass

class Objeto(ObjetoBase):
    ojtid: int
    titulos_deuda: List[TituloDeuda] = []

    class Config:
        orm_mode = True