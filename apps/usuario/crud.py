from sqlalchemy.orm import Session
from . import models, schemas

# optiene un usuario por mail
def usuario_por_mail(db: Session, email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()

# crea una nueva instancioa de usuario
def crear_usuario(db: Session, usuario: schemas.Crear_usuario, hashed_password: str):
    db_usuario = models.Usuario(email=usuario.email, hash=hashed_password, estado="activacion_pendiente", rol="usuario")
    db.add(db_usuario)
    # guarda la nueva instansia de usuario
    db.commit()
    # Actualiza el objeto db_usuario con los valores de la base de datos
    db.refresh(db_usuario)
    return db_usuario