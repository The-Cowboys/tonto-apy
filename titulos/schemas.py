from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# crear Titulo
class CrearTitulo (BaseModel):
    name: str
    cowboy_id: int

    class Config:
        orm_mode = True

# respuesta
class TituloRespuesta (BaseModel):
    id: int
    name: str
    created: datetime
    updated: datetime
    cowboy_id: int

    class Config:
        orm_mode = True

# actualizar
class ActualizarTitulo (BaseModel):
    name: Optional[str] = None
    cowboy_id: Optional[int] = None

    class Config:
        orm_mode = True
