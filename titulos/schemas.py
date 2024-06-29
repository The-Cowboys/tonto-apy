from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# crear Titulo
class CrearTitulo (BaseModel):
    name: str
    cowboy_id: int

    class Config:
        from_attributes = True


# devuelve todo los titulos
class Titulos (BaseModel):

    id: int
    name: str

    class Config:
        from_attributes = True


# actualizar
class ActualizarTitulo (BaseModel):
    name: Optional[str] = None
    cowboy_id: Optional[int] = None

    class Config:
        from_attributes = True


# respuesta titulos del cowboy
class TitulosCowboyRespuesta (BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


# esta importacion va ultima para evitar error de importacion circular
# respuesta al crear un titulo
from cowboys.schemas import CowboyTituloRespuesta
class TituloRespuesta (BaseModel):
    id: int
    name: str
    # esta entre comillas "" para evitar un error de importacion circular de normal va sin comillas ""
    cowboy: "CowboyTituloRespuesta"
    created: datetime
    updated: datetime

    class Config:
        from_attributes = True
