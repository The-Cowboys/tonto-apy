from sqlalchemy.orm import Session

import random
from datetime import datetime, timedelta, time

from tonto import models, schemas
from cowboys import crud

# al horario de uruguay se le tiene que sumar 3 hora
# al horario de europa se le tiene que descontar 2 hora
HORA_ESPECIFICA = time (21, 0)


def obtener_ultimo_tonto (db: Session):
    ahora = datetime.utcnow()
    fecha_hora_especifica = datetime.combine (ahora.date(), HORA_ESPECIFICA)

    if ahora < fecha_hora_especifica:
        fecha_hora_especifica -= timedelta (days=1)

    return db.query (models.Tonto).filter (models.Tonto.created >= fecha_hora_especifica).first()


def calcular_tiempo():
    ahora = datetime.utcnow()
    fecha_hora_especifica = datetime.combine (ahora.date(), HORA_ESPECIFICA)

    if ahora >= fecha_hora_especifica:
        fecha_hora_especifica += timedelta (days=1)

    diferencia_tiempo = fecha_hora_especifica - ahora
    return diferencia_tiempo


# veufuca si en las ultimas 24 horas se creo un tonto
# Crea un nuevo registro en la tabla tonto y le suma mas uno tonto al cowboy
def nuevo_tonto (db: Session, nuevo_tonto: schemas.NuevoTonto):
    # Verifica si ya existe un Tonto creado después de la hora específica del día
    tonto_creado = obtener_ultimo_tonto (db)

    if tonto_creado:
        tiempo_restante = calcular_tiempo()
        return None, tiempo_restante

    cowboy_existente = crud.cowboy_id (db, nuevo_tonto.cowboy_id)

    if not cowboy_existente:
        return None, None

    db_tonto = models.Tonto (cowboy_id = nuevo_tonto.cowboy_id)

    cowboy_existente.tonto += 1

    db.add (cowboy_existente)
    db.add (db_tonto)
    db.commit()

    return db_tonto, None


# Selecsiona un cowboy aleatoreo y le suma mas 1 al tonto y despues lo guarda
# Crea un nuevo registro en la tabla tontos
def tonto_random (db: Session):
    cowboys = crud.obtener_cowboys (db)

    if not cowboys:
        return None

    random.shuffle (cowboys)
    random_cowboy = random.choice (cowboys)

    nuevo_tonto (db, random_cowboy)

    return random_cowboy