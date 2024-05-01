from sqlalchemy.orm import Session
from . import models, schemas

# optiene un usuario por mail
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# crea una nueva instancioa de usuario
def create_user(db: Session, user: schemas.UserCreate, hashed_password: str):
    db_user = models.User(email=user.email, hash=hashed_password, estado="activacion_pendiente", rol="usuario")
    db.add(db_user)
    # guarda la nueva instansia de usuario
    db.commit()
    # Actualiza el objeto db_user con los valores de la base de datos
    db.refresh(db_user)
    return db_user