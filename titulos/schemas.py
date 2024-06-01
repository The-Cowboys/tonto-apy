from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

from cowboys.schemas import CowboyTituloRespuesta

# crear Titulo
class CrearTitulo (BaseModel):
    name: str
    cowboy_id: int

    class Config:
        orm_mode = True


# respuesta al crear un titulo
class TituloRespuesta (BaseModel):
    id: int
    name: str
    cowboy: CowboyTituloRespuesta
    created: datetime
    updated: datetime

    class Config:
        orm_mode = True


# devuelve todo los titulos
class Tirulos (BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


# actualizar
class ActualizarTitulo (BaseModel):
    name: Optional[str] = None
    cowboy_id: Optional[int] = None

    class Config:
        orm_mode = True


# respuesta titulos del cowboy
class TitulosCowboyRespuesta (BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True