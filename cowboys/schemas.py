from pydantic import BaseModel

class CrearCowboy (BaseModel):
    name:str
    email:str
    tonto:int

    class Config:
        orm_mode = True

class CrearCowboyRespuesta (BaseModel):
    name:str
    email:str
    tonto:int

    class Config:
        orm_mode = True

class CowboyTituloRespuesta (BaseModel):
    name: str
    id: int