from sqlalchemy.orm import Session

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


# obtiene un titulo por id
def titulo_id (db: Session, id):
    return db.query (models.Titulo).filter (models.Titulo.id == id).first()


# edita un titulo
def editar_titulo (db: Session, titulo_id: int, titulo_editar: schemas.ActualizarTitulo):
    titulo = db.query (models.Titulo).filter (models.Titulo.id == titulo_id).first()

    if not titulo:
        return False

    for key, value in titulo_editar.dict().items():
        # si el campo es igual a None no lo atualiza
        if value is not None:
            setattr (titulo, key, value)

    db.commit()

    return titulo

# borrar un titulo
def borrar_titulo (db: Session, id):
    titulo = db.query (models.Titulo).filter (models.Titulo.id == id).first()

    if titulo :
        db.delete (titulo)
        db.commit()

        return False

    return True
