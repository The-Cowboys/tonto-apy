from sqlalchemy.orm import Session
from . import models, schemas

def crear_cowboy (db: Session, cowboy: schemas.CrearCowboy):
    db_cowboy = models.Usuario ( id = cowboy.id ,name = cowboy.name, email = cowboy.email, tonto = cowboy.tonto)
    db.add (db_cowboy)
    # guarda la nueva instansia de cowboy
    db.commit()
    # Actualiza el objeto db_cowboy con los valores de la base de datos
    # db.refresh (db_cowboy)
    return db_cowboy


def actualizar_tonto():
    Session = sessionmaker(bind=engine)
    session = Session()

    # Obtener el número de menciones de cada cowboy y actualizar la columna 'tonto'
    cowboys = session.query(Cowboy)
    for cowboy in cowboys:
        cowboy.tonto = session.query(func.count()).filter_by(id=cowboy.id).scalar()
    
    session.commit()
    session.close()