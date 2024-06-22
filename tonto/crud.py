from sqlalchemy.orm import Session

import json
import random

# from . import models, schemas
from cowboys import crud
from cowboys.models import Cowboy
from cowboys.routers_cowboys import editar_cowboy


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




