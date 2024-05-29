from fastapi import APIRouter, Depends, Body, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from urls import CREAR_COWBOY, OBTENER_COWBOYS, OBTENER_COWBOY_ID, EDITAR_COWBOY, BORRAR_COWBOY
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


@router.get (OBTENER_COWBOYS, response_model = list [schemas.CowboysRespuesta])
def obtener_cowboys (db: Session = Depends (bd_coneccion.get_db)):
    cowboys = crud.obtener_cowboys (db = db)

    return cowboys


@router.get (OBTENER_COWBOY_ID, response_model = schemas.CowboyRespuesta)
def obtener_cowboy (id: int, db: Session = Depends (bd_coneccion.get_db)):
    cowboy = crud.cowboy_id (db, id)

    if cowboy is None:
        raise HTTPException (status_code = 404, detail = "Cowboy no encontrado")

    return cowboy


@router.put (EDITAR_COWBOY, response_model = schemas.CrearCowboyRespuesta)
def editar_cowboy (id: int, cowboy_editar: schemas.CowboyEditar, db: Session = Depends(bd_coneccion.get_db)):
    for campo in ["name", "email", "tonto"]:
        if getattr (cowboy_editar, campo) in (0, "", []):
            setattr (cowboy_editar, campo, None)

    cowboy_existente = crud.cowboy_existente (db, cowboy_editar)

    if cowboy_existente :
        return JSONResponse (status_code = status.HTTP_400_BAD_REQUEST, content = {"detail": "Ya existe un Cowboy con ese email"})

    cowboy = crud.editar_cowboy (db, id, cowboy_editar)

    if cowboy is None:
        raise HTTPException (status_code = 404, detail = "Cowboy no encontrado")

    return cowboy

@router.delete (BORRAR_COWBOY)
def obtener_cowboy(id: int, db: Session = Depends (bd_coneccion.get_db)):
    cowboy = crud.borrar_cowboy (db, id)

    if cowboy is None:
        raise HTTPException (status_code = 404, detail = "Cowboy no encontrado")

    return JSONResponse (status_code = status.HTTP_200_OK, content = {"detail": "El cowboy fue borrado con exito"})
