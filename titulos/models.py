from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, event
from sqlalchemy.orm import relationship
import datetime

from settings.bd_coneccion import Base
from cowboys.models import Cowboy

class Titulo (Base):
    __tablename__ = "titulos"

    id = Column (Integer, primary_key = True, index = True)
    name = Column (String, index = True)
    created = Column (DateTime, default = datetime.datetime.utcnow)
    updated = Column (DateTime, default = datetime.datetime.utcnow, onupdate = datetime.datetime.utcnow)
    cowboy_id = Column (Integer, ForeignKey ('cowboys.id'))

    cowboy = relationship ("Cowboy", back_populates = "titulos")

# Para actualizar automáticamente el campo updated
@event.listens_for (Titulo, 'before_update')
def receive_before_update (mapper, connection, target):
    target.updated = datetime.datetime.utcnow()

# agregar esto al modelo cowboy
# titulos = relationship("Titulo", back_populates="cowboy")
