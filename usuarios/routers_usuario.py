from fastapi import APIRouter, Depends, Body, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import bcrypt

from usuarios import crud, schemas
from settings import bd_coneccion

router = APIRouter()

@router.post ("/registrar", response_model = schemas.UsuarioRespuesta)
def crear_usuario (db: Session = Depends (bd_coneccion.get_db), usuario: schemas.CrearUsuario = Body(...)):
    # Valida que los campos no estén vacíos
    if not usuario.email:
        return JSONResponse(status_code = status.HTTP_400_BAD_REQUEST, content={"detail": "El campo 'email' no puede estar vacío"})
    if not usuario.password:
        return JSONResponse(status_code = status.HTTP_400_BAD_REQUEST, content={"detail": "El campo 'password' no puede estar vacío"})

    # busca si el usuario existe
    db_usuario = crud.usuario_por_mail (db, email = usuario.email)

    # si el usuario existe retorna un status 400 y un json con un mensaje
    if db_usuario:
        return JSONResponse(status_code = status.HTTP_400_BAD_REQUEST, content={"detail": "El usuario ya está registrado"})

    # Generar el hash de la contraseña
    # hashed_password = bcrypt.hashpw (usuario.password.encode ('utf-8'), bcrypt.gensalt())
    hash = bcrypt.hashpw (usuario.password.encode ('utf-8'), bcrypt.gensalt())
    hashed_password = hash.decode()

    # Guarda el usuario en la base de datos
    db_usuario = crud.crear_usuario (db = db, usuario = usuario, hashed_password = hashed_password)

    return db_usuario
