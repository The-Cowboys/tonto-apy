from fastapi import APIRouter, Depends, Body, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

import cowboys
from tonto import crud
from settings import bd_coneccion

router = APIRouter()

@router.get ("/tonto", response_model = cowboys.schemas.CrearCowboyRespuesta)
def seleccionar_tonto (db: Session = Depends (bd_coneccion.get_db)):
    cowboy  = crud.tonto_random (db)
    if cowboy is None:
        raise HTTPException (status_code = 404, detail = "No hay cowboys disponibles")

    return cowboy