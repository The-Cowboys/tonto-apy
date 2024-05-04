from fastapi import APIRouter, HTTPException, Depends, Body
from sqlalchemy.orm import Session
import bcrypt

from . import crud, schemas, models, bd_coneccion

router = APIRouter()

def get_db():
    print ("8")
    db = bd_coneccion.SessionLocal()
    print ("9")

    try:
        print ("10")
        yield db
        print ("11")

    finally:
        print ("12")
        db.close()
        print ("13")

# def crear_usuario(usuario: schemas.Crear_usuario, db: Session = Depends(bd_coneccion.SessionLocal)):
# def crear_usuario(usuario: schemas.Crear_usuario = Body(...), db: Session = Depends(bd_coneccion.SessionLocal)):
@router.post("/registrar", response_model=schemas.Usuario_respuesta)
def crear_usuario(db: Session = Depends(get_db), usuario: schemas.Crear_usuario = Body(...)):
    print ("3")
    # busca si el usuario existe
    db_usuario = crud.usuario_por_mail(db, email=usuario.email)
    print ("4")


    # si el usuario existe retorna un status 400
    if db_usuario:
        print ("5")

        raise HTTPException(status_code=400, detail="El usuario ya está registrado")

    # Generar el hash de la contraseña
    hashed_password = bcrypt.hashpw(usuario.password.encode('utf-8'), bcrypt.gensalt())
    print ("6")

    # Crear el usuario en la base de datos
    db_usuario = crud.crear_usuario(db=db, usuario=usuario, hashed_password=hashed_password)
    print ("7")

    return db_usuario
