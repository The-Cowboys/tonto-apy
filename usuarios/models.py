from sqlalchemy import Column, Integer, String, DateTime
import datetime

from settings.bd_coneccion import Base

class Usuario (Base):
    # nombre de la tabla a la que apunta este modelo
    __tablename__ = "usuarios"

    id = Column (Integer, primary_key = True, index = True)
    email = Column (String, unique = True, index = True)
    hash = Column (String)
    estado = Column (String)
    rol = Column (String)
    created = Column (DateTime, default = datetime.datetime.utcnow)

