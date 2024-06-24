from sqlalchemy.orm import Session

import random

from tonto import models, schemas
from cowboys import crud


#   selecsiona un cowboy aleatoreo y le suma mas 1 al tonto y despues lo guarda
def tonto_random (db: Session):
    cowboys = crud.obtener_cowboys (db)

    if not cowboys:
        return None

    random.shuffle (cowboys)
    random_cowboy = random.choice (cowboys)
    random_cowboy.tonto += 1

    db.commit()

    return random_cowboy


# Crea un nuevo registro en la tabla tonto y le suma mas uno tonto al cowboy
def nuevo_tonto (db: Session, nuevo_tonto: schemas.NuevoTonto):
    cowboy_existente = crud.cowboy_id (db, nuevo_tonto.cowboy_id)

    if not cowboy_existente:
        return None

    db_tonto = models.Tonto (cowboy_id = nuevo_tonto.cowboy_id)

    cowboy_existente.tonto += 1

    db.add (cowboy_existente)
    db.add (db_tonto)
    db.commit()

    return db_tonto