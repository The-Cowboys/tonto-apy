from pydantic import BaseModel

class CrearCowboy (BaseModel):
    id:int
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