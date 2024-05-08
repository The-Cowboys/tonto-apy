from fastapi import FastAPI


from apps.usuario import routers_usuario

api_router = FastAPI()

# Aca van todas las URLs que dirigen a las apps
app.include_router (routers_usuario.router, prefix = "/usuario", tags = ["usuario"])