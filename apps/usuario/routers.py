from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

app = FastAPI()

class UserCreate(BaseModel):
    email: str
    hash: str
    estado: str
    rol: str
    created: str

@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, email=user.email, hash=user.hash, estado=user.estado, rol=user.rol, created=user.created)
