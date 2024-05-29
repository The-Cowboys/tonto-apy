from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


from settings.bd_coneccion import Base

class Cowboy (Base):
    # nombre de la tabla a la que apunta este modelo
    __tablename__ = "cowboys"

    id = Column (Integer, primary_key = True, index = True)
    name = Column (String, index = True)
    email = Column (String, unique = True, index = True)
    tonto = Column (Integer)

    titulos = relationship("Titulo", back_populates="cowboy")
