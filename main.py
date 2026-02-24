from fastapi import FastAPI
from routes.routes_rol import rol
from routes.routes_usuario import usuario
from routes.routes_auto import auto

app = FastAPI(
    title="API Segura de Administracion de un autolavado",
    description="API creada por mi profesor y le copie el código"
)

app.include_router(rol)
app.include_router(usuario)
app.include_router(auto)