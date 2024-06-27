from fastapi import APIRouter, Depends, Body, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

import cowboys
from tonto import crud, schemas
from settings import bd_coneccion

router = APIRouter()

@router.get ("/tonto", response_model = cowboys.schemas.CrearCowboyRespuesta)
def seleccionar_tonto (db: Session = Depends (bd_coneccion.get_db)):
    cowboy  = crud.tonto_random (db)

    if cowboy is None:
        raise HTTPException (status_code = 404, detail = "No existe ese cowboy")

    return cowboy


@router.post ("/tonto", response_model = schemas.TontoRespuesta)
def guardar_tonto (nuevo_tonto: schemas.NuevoTonto, db: Session = Depends (bd_coneccion.get_db)):
    tonto_creado, tiempo_restante = crud.nuevo_tonto (db, nuevo_tonto)

    if tonto_creado is None:
        if tiempo_restante:
            horas, minutos = divmod (tiempo_restante.seconds // 60, 60)
            raise HTTPException(
                status_code=400,
                detail=f"El Tonto de hoy ya fue creado. Faltan {horas} horas y {minutos} minutos para que se pueda crear un nuevo Tonto."
            )
        else:
            raise HTTPException(status_code=404, detail="No existe ese cowboy")

    return tonto_creado