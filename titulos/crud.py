from sqlalchemy.orm import Session
from sqlalchemy import func

from . import models, schemas
from cowboys.models import Cowboy

def crear_titulo (db: Session, titulo: schemas.CrearTitulo):
    db_titulo = models.Titulo (     name = titulo.name,
                                    cowboy_id = titulo.cowboy_id,
                                    )
    db.add (db_titulo)
    # guarda la nueva instansia de titulo
    db.commit()
    # Actualiza el objeto db_titulo con los valores de la base de datos
    return db_titulo

# revisa si existe el cowboy con ese id
def cowboy_existente (db: Session, cowboy_id: int ):
    return db.query (Cowboy).filter (Cowboy.id == cowboy_id).one_or_none() is not None

# obtiene todo los titulos
def obtener_titulos (db: Session):
    return db.query (models.Titulo).all()