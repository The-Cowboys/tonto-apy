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

# optiene un cowboy por mail
def cowboy_existente (db: Session, cowboy ):
    return db.query (models.Cowboy).filter (models.Cowboy.email == cowboy.email).one_or_none() is not None


def obtener_cowboys(db: Session):
    return db.query(models.Cowboy).all()


# def actualizar_tonto():
#     Session = sessionmaker(bind=engine)
#     session = Session()

#     # Obtener el número de menciones de cada cowboy y actualizar la columna 'tonto'
#     cowboys = session.query(Cowboy)
#     for cowboy in cowboys:
#         cowboy.tonto = session.query(func.count()).filter_by(id=cowboy.id).scalar()

#     session.commit()
#     session.close()