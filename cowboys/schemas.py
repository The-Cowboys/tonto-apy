from pydantic import BaseModel

class CrearCowboy (BaseModel):
    id = int
    name = str
    email = str
    tonto = int