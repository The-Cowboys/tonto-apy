from fastapi import APIRouter, Depends, Body, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from urls import CREAR_COWBOY, OPTENER_COWBOYS
from cowboys import crud, schemas
from settings import bd_coneccion

router = APIRouter()

@router.post (CREAR_COWBOY, response_model = schemas.CrearCowboyRespuesta)
def crear_cowboy (db: Session = Depends (bd_coneccion.get_db), cowboy: schemas.CrearCowboy = Body(...)):
    # Valida que los campos no estén vacíos
    for campo in ["name", "email", "tonto"]:
        if getattr (cowboy, campo) in (None, "", []):
            return JSONResponse (status_code = status.HTTP_400_BAD_REQUEST, content = {"detail": f"El campo {campo} está vacío"})

    # busca si el cowboy existe
    cowboy_existente = crud.cowboy_existente (db, cowboy)

    # si el cowboy existe retorna un status 400 y un json con un mensaje
    if cowboy_existente :
        return JSONResponse (status_code = status.HTTP_400_BAD_REQUEST, content = {"detail": "Ya existe un Cowboy con ese email"})

    # Guarda el cowboy en la base de datos
    db_cowboy = crud.crear_cowboy (db = db, cowboy = cowboy,)

    return db_cowboy

@router.post (OPTENER_COWBOYS, response_model = schemas.CowoysRespuesta)
def optener_cowboy (db: Session = Depends (bd_coneccion.get_db), ):
    pass