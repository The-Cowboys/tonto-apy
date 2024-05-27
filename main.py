from fastapi import FastAPI

from usuarios import routers_usuario
from cowboys import routers_cowboys
from titulos import routers_titulos

app = FastAPI()

# Aca van todas las URLs que dirigen a las apps
app.include_router (routers_usuario.router, prefix = "/api", tags = ["api"])

app.include_router (routers_titulos.router, prefix = "/api")

app.include_router (routers_cowboys.router, prefix = "/api")