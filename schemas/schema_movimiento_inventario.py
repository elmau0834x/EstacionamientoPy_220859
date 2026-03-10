from datetime import datetime
from pydantic import BaseModel, ConfigDict
from enum import Enum

# Creamos el Enum para Pydantic y Swagger
class TipoMovimientoEnum(str, Enum):
    Entrada = "Entrada"
    Salida = "Salida"

class MovimientoInventarioBase(BaseModel):
    producto_Id: int
    tipo_movimiento: TipoMovimientoEnum  # <--- ¡Magia! Swagger ahora mostrará una lista desplegable
    cantidad: int
    fecha_movimiento: datetime
    usuario_Id: int

class MovimientoInventarioCreate(MovimientoInventarioBase):
    pass

class MovimientoInventarioUpdate(MovimientoInventarioBase):
    pass

class MovimientoInventario(MovimientoInventarioBase):
    Id: int
    model_config = ConfigDict(from_attributes=True)