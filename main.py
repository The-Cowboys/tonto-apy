from fastapi import FastAPI

from usuarios import routers_usuario
from titulos import routers_titulos
from cowboys import routers_cowboys


app = FastAPI()

# Aca van todas las URLs que dirigen a las apps
app.include_router (routers_usuario.router, prefix = "/api", tags = ["api"])

app.include_router (routers_titulos.router, prefix = "/api", tags = ["api"])

app.include_router (routers_cowboys.router, prefix = "/api")

