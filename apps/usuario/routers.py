from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import bcrypt

from . import crud, schemas, models, bd_coneccion

router = APIRouter()

@router.post("/registrar", response_model=schemas.Usuario_respuesta)
def crear_usuario(usuario: schemas.Crear_usuario, db: Session = Depends(bd_coneccion.SessionLocal)):
    # busca si el usuario existe
    db_usuario = crud.usuario_por_mail(db, email=usuario.email)

    # si el usuario existe retorna un status 400
    if db_usuario:
        raise HTTPException(status_code=400, detail="El usuario ya está registrado")


    hashed_password = bcrypt.hashpw(usuario.password.encode('utf-8'), bcrypt.gensalt())
    db_usuario = crud.crear_usuario(db=db, usuario=usuario, hashed_password=hashed_password)
    return db_usuario
