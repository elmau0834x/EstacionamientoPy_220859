from fastapi import FastAPI
from routes.router_rol import rol
from routes.router_usuario import usuario

app = FastAPI(
    title="API Segura de Administracion de un autolavado",
    description="API creada por mi profesor y le copie el código"
)

app.include_router(rol)
app.include_router(usuario)