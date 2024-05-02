# from fastapi import APIRouter
from fastapi import FastAPI

from apps.usuario import routers

app = FastAPI()

# Aca van todas las URLs que dirigen a las apps

# app.include_router(  archivo  . objeto APIRouter , prefix="/ruta", tags=["apodo"])
app.include_router (routers.router, prefix="/usuario", tags=["usuario"])