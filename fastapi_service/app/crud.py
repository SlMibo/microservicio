from sqlalchemy.orm import Session
from . import models, schemas, events
import json

def create_user(db: Session, user: schemas.UserBase):
    event_payload = user.dict()
    event = models.Event(event_type="UserCreated", payload=json.dumps(event_payload))
    db.add(event)
    db.commit()
    db.refresh(event)

    events.publish_event("UserCreated", event_payload)

    # Actualizar la proyección
    projection = models.UserProjection(**event_payload)
    db.add(projection)
    db.commit()
    return projection

# def get_objeto(db: Session, ojtid: int):
#     return db.query(models.Objeto).filter(models.Objeto.ojtid == ojtid).first()

# def get_objetos(db: Session, skip: int = 0, limit: int = 10):
#     return db.query(models.Objeto).offset(skip).limit(limit).all()

# def get_detalles_titulos_deuda(db: Session, skip: int = 0, limit: int = 10):
#     return db.query(models.DetallesTitulosDeuda).offset(skip).limit(limit).all()

# def create_objeto(db: Session, objeto: schemas.ObjetoCreate):
#     db_objeto = models.Objeto(**objeto.dict())
#     db.add(db_objeto)
#     db.commit()
#     db.refresh(db_objeto)
#     return db_objeto

# def create_titulo_deuda(db: Session, titulo: schemas.TituloDeudaCreate):
#     db_titulo = models.TituloDeuda(**titulo.dict())
#     db.add(db_titulo)
#     db.commit()
#     db.refresh(db_titulo)
#     return db_titulo