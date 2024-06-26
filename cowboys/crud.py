from sqlalchemy.orm import Session
from sqlalchemy import func

from . import models, schemas

def crear_cowboy (db: Session, cowboy: schemas.CrearCowboy):
    db_cowboy = models.Cowboy (     name = cowboy.name,
                                    email = cowboy.email,
                                    tonto = cowboy.tonto if cowboy.tonto is not None else 0
                                    )
    db.add (db_cowboy)
    # guarda la nueva instansia de cowboy
    db.commit()
    # Actualiza el objeto db_cowboy con los valores de la base de datos
    # db.refresh (db_cowboy)
    return db_cowboy


# obtiene un cowboy por mail
def cowboy_existente (db: Session, cowboy ):
    return db.query (models.Cowboy).filter (models.Cowboy.email == cowboy.email).one_or_none() is not None

# obtiene todo los cowboys
def obtener_cowboys (db: Session):
    return db.query (models.Cowboy).all()


# obtiene un cowboy por id
def cowboy_id (db: Session, id):
    return db.query (models.Cowboy).filter (models.Cowboy.id == id).first()


# edita un cowboy
def editar_cowboy (db: Session, cowboy_id: int, cowboy_editar: schemas.CowboyEditar):
    cowboy = db.query (models.Cowboy).filter (models.Cowboy.id == cowboy_id).first()

    if not cowboy:
        return None

    for key, value in cowboy_editar.dict().items():
        # si el campo es igual a None no lo atualiza
        if value is not None:
            setattr (cowboy, key, value)

    db.commit()

    return cowboy


# borrar un cowboy
def borrar_cowboy (db: Session, id):
    cowboy = db.query (models.Cowboy).filter (models.Cowboy.id == id).first()

    if cowboy :
        db.delete (cowboy)
        db.commit()

        return True

    return None
