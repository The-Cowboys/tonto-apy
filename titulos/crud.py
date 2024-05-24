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
    # db.refresh (db_titulo)
    return db_titulo

# revisa si existe el cowboy con ese id
def cowboy_existente (db: Session, cowboy_id: int ):
    return db.query (Cowboy).filter (Cowboy.id == cowboy_id).one_or_none() is not None


# def actualizar_tonto():
#     Session = sessionmaker(bind=engine)
#     session = Session()

#     # Obtener el número de menciones de cada titulo y actualizar la columna 'tonto'
#     cowboys = session.query(Titulo)
#     for titulo in titulos:
#         titulo.tonto = session.query(func.count()).filter_by(id=titulo.id).scalar()

#     session.commit()
#     session.close()