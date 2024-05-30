from fastapi import APIRouter, Depends, Body, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from titulos import crud, schemas
from settings import bd_coneccion

router = APIRouter()

@router.post ("/titulos", response_model = schemas.TituloRespuesta)
def crear_titulo (db: Session = Depends (bd_coneccion.get_db), titulo: schemas.CrearTitulo = Body(...)):
    # Valida que los campos no estén vacíos
    for campo in ["name", "cowboy_id",]:
        if getattr (titulo, campo) in (None, "", []):
            return JSONResponse (status_code = status.HTTP_400_BAD_REQUEST, content = {"detail": f"El campo {campo} está vacío"})

    # # busca si el titulo existe
    cowboy_existente = crud.cowboy_existente (db, titulo.cowboy_id)

    # Si el cowboy no existe retorna un status 404 y un json con un mensaje
    if not cowboy_existente:
        raise HTTPException (status_code = status.HTTP_404_NOT_FOUND, detail = f"El cowboy con el id {titulo.cowboy_id} no existe")

    # Guarda el titulo en la base de datos
    db_titulo = crud.crear_titulo (db = db, titulo = titulo,)

    return db_titulo


@router.get ("/titulos", response_model = list [schemas.Tirulos])
def obtener_titulos (db: Session = Depends (bd_coneccion.get_db)):
    titulos = crud.obtener_titulos (db = db)

    return titulos