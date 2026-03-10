from pydantic import BaseModel, ConfigDict

# 1. Esto es lo único que el cajero mandará en Swagger (¡Sin precio!)
class TicketProductoCreate(BaseModel):
    ticket_Id: int
    producto_Id: int
    cantidad: int

# 2. Esto es lo que devuelve la API (Ya incluye el ID autogenerado y el precio que el sistema calculó)
class TicketProducto(TicketProductoCreate):
    Id: int
    precio_unitario: float
    model_config = ConfigDict(from_attributes=True)