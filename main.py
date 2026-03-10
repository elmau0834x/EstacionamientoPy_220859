from routes.routes_reporte import reporte
from routes.routes_ticket_producto import ticket_producto
from fastapi import FastAPI
from routes.routes_rol import rol
from routes.routes_usuario import usuario
from routes.routes_auto import auto
from routes.routes_servicios import servicio
from routes.routes_auto_servicio import auto_servicio
from routes.routes_producto import producto
from routes.routes_movimiento_inventario import movimiento

app = FastAPI(
    title="API Segura de Administracion de un autolavado",
    description="API creada por mi profesor y le copie el código"
)

app.include_router(ticket_producto)
app.include_router(usuario)
app.include_router(rol)
app.include_router(auto)
app.include_router(servicio)
app.include_router(auto_servicio)
app.include_router(producto)
app.include_router(movimiento)
app.include_router(reporte)
