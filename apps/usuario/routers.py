from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import bcrypt

from . import crud, schemas, models, bd_coneccion

router = APIRouter()

@router.post("/registrar", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(bd_coneccion.get_db)):
    # busca si el usuario existe
    db_user = crud.get_user_by_email(db, email=user.email)

    # si el usuario existe retorna un status 400
    if db_user:
        raise HTTPException(status_code=400, detail="El usuario ya está registrado")


    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = crud.create_user(db=db, user=user, hashed_password=hashed_password)
    return db_user
