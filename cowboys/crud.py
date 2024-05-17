from sqlalchemy.orm import Session
from sqlalchemy import func

from . import models, schemas

def crear_cowboy (db: Session, cowboy: schemas.CrearCowboy):
    if cowboy.id == 0 :
        id_mas_alto = db.query(func.max(models.Cowboy.id)).scalar()

        if id_mas_alto is None:
            id_mas_alto = 1

        else:
            id_mas_alto += 1

    else:
        id_mas_alto = cowboy.id

    db_cowboy = models.Cowboy (    id = id_mas_alto,
                                    name = cowboy.name,
                                    email = cowboy.email,
                                    tonto = cowboy.tonto if cowboy.tonto is not None else 0
                                    )
    db.add (db_cowboy)
    # guarda la nueva instansia de cowboy
    db.commit()
    # Actualiza el objeto db_cowboy con los valores de la base de datos
    # db.refresh (db_cowboy)
    return db_cowboy

# optiene un usuario por mail
def cowboy_existente (db: Session, cowboy ):
    if db.query (models.Cowboy).filter (models.Cowboy.id == cowboy.id).first():
        resultado = "id"
        return resultado

    if db.query (models.Cowboy).filter (models.Cowboy.email == cowboy.email).first():
        resultado = "email"
        return resultado

    resultado = "adelante"
    return True

# def actualizar_tonto():
#     Session = sessionmaker(bind=engine)
#     session = Session()

#     # Obtener el número de menciones de cada cowboy y actualizar la columna 'tonto'
#     cowboys = session.query(Cowboy)
#     for cowboy in cowboys:
#         cowboy.tonto = session.query(func.count()).filter_by(id=cowboy.id).scalar()
    
#     session.commit()
#     session.close()