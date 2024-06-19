from sqlalchemy import Column, Integer, DateTime, ForeignKey, Date
from sqlalchemy.orm import relationship
import datetime

from settings.bd_coneccion import Base
from cowboys.models import Cowboy

class Tonto (Base):
    __tablename__ = "tonto"

    id = Column (Integer, primary_key = True, index = True)
    cowboy_id = Column (Integer, ForeignKey ('cowboys.id'))
    created = Column (DateTime, default = datetime.datetime.utcnow)
    dia = Column(Date, default = datetime.date.today)

    cowboy = relationship ("Cowboy", back_populates = "tontos")
