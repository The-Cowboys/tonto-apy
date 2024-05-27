from pydantic import BaseModel
from typing import List

from titulos.schemas import TitulosCowboyRespuesta

# crear un cowboy
class CrearCowboy (BaseModel):
    name:str
    email:str
    tonto:int

    class Config:
        orm_mode = True

# respuesta al crear un cowboy
class CrearCowboyRespuesta (BaseModel):
    id:int
    name:str
    email:str
    tonto:int

    class Config:
        orm_mode = True

# respuesta al optener todos los cowboys
class CowoysRespuesta (BaseModel):
    id:int
    name:str

    class Config:
        orm_mode = True

# Respuesta al optener un cowboy
class CowoyRespuesta (BaseModel):
    id:int
    name:str
    tonto:int
    titulos: List[TitulosCowboyRespuesta] = []

    class Config:
        orm_mode = True