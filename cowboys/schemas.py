from pydantic import BaseModel
from typing import List, Optional


# crear un cowboy
class CrearCowboy (BaseModel):
    name:str
    email:str
    tonto:int

    class Config:
        from_attributes = True


# respuesta al crear un cowboy
class CrearCowboyRespuesta (BaseModel):
    id:int
    name:str
    email:str
    tonto:int

    class Config:
        from_attributes = True


# respuesta al optener todos los cowboys
class CowboysRespuesta (BaseModel):
    id:int
    name:str

    class Config:
        from_attributes = True



# Respuesta al optener los titulos de un cowboy
class CowboyTituloRespuesta (BaseModel):
    name: str
    id: int

    class Config:
        from_attributes = True


# editar cowboy
class CowboyEditar (BaseModel):
    name: Optional [str] = None
    email: Optional [str] = None
    tonto: Optional [int] = None

    class Config:
        from_attributes = True


# esta importacion va ultima para evitar error de importacion circular
# Respuesta al optener un cowboy
from titulos.schemas import TitulosCowboyRespuesta
class CowboyRespuesta (BaseModel):
    id:int
    name:str
    email:str
    tonto:int
    # esta entre comillas "" para evitar un error de importacion circular de normal va sin comillas ""
    titulos: List["TitulosCowboyRespuesta"] = []

    class Config:
        from_attributes = True
