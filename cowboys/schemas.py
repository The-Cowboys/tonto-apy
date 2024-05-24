from pydantic import BaseModel
from typing import List

from titulos.schemas import 

class CrearCowboy (BaseModel):
    name:str
    email:str
    tonto:int

    class Config:
        orm_mode = True

class CrearCowboyRespuesta (BaseModel):
    id:int
    name:str
    email:str
    tonto:int

    class Config:
        orm_mode = True

class CowoysRespuesta (BaseModel):
    id:int
    name:str
    tonto:int
    tonto:int
    titulos: List[TituloRespuesta] = []