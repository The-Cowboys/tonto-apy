from sqlalchemy.orm import Session

import random

from . import models, schemas
from cowboys import crud
from cowboys.models import Cowboy


#   selecsiona un cowboy aleatoreo
def tonto_random (db: Session):
    cowboys = crud.obtener_cowboys (db)

    cowboys_id = []
    for cowboy in cowboys:
        cowboys_id.append (cowboy.id)

    random.shuffle (cowboys_id)
    cowboy_id = random.choice (cowboys_id)

    return cowboy_id


def seleccionar_tonto (db: Session):
    cowboy_id = tonto_random (db)

    cowboy = crud.cowboy_id (db, cowboy_id)

    return cowboy



