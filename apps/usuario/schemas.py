from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    email: str
    estado: str = "activacion_pendiente"
    rol: str = "usuario"
