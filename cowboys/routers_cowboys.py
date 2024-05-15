from fastapi import APIRouter, Depends, Body, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import bcrypt

from cowboys import crud, schemas
from settings import bd_coneccion

router = APIRouter()

@router.post ("/CrearCowboys", response_model = schemas.CrearCowboyRespuesta)
def crear_cowboy (db: Session = Depends (bd_coneccion.get_db), cowboy: schemas.CrearCowboy = Body(...)):

    # Valida que los campos no estén vacíos
    for campo in ["name", "email", "tonto"]:
        if getattr (cowboy, campo) in (None, "", []):
            return JSONResponse (status_code=status.HTTP_400_BAD_REQUEST, content = {"detail": f"El campo {campo} está vacío"})

    # busca si el cowboy existe
    db_cowboy = crud.cowboy_por_id (db, id = cowboy.id)

    # si el cowboy existe retorna un status 400 y un json con un mensaje
    if db_cowboy:
        return JSONResponse (status_code = status.HTTP_400_BAD_REQUEST, content={"detail": "El cowboy ya está registrado"})

    # Guarda el cowboy en la base de datos
    db_cowboy = crud.crear_cowboy (db = db, cowboy = cowboy,)

    return db_cowboy