from fastapi import FastAPI

# esto es para evitar errores de importacion circular
from init_schemas import init_schemas
init_schemas ()

from usuarios import routers_usuario
from titulos import routers_titulos
from cowboys import routers_cowboys
from titulos import routers_titulos
# from tonto import routers_tonto


app = FastAPI()

# Aca van todas las URLs que dirigen a las apps
app.include_router (routers_usuario.router, prefix = "/api", tags = ["api"])

app.include_router (routers_titulos.router, prefix = "/api")

app.include_router (routers_cowboys.router, prefix = "/api")

# app.include_router (routers_tonto.router, prefix = "/api")
