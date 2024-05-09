from pydantic import BaseModel

# para crear un nuevo usuario se tienen que proporsionar estos datos
class Crear_usuario (BaseModel):
    email: str
    password: str

# esto es lo que se devuelve despues de crrear un usuario
class Usuario_respuesta (BaseModel):
    email: str
    estado: str = "activacion_pendiente"
    rol: str = "usuario"
