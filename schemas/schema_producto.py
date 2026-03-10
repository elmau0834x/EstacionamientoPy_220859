from datetime import datetime
from pydantic import BaseModel, ConfigDict

class ProductoBase(BaseModel):
    nombre: str
    descripcion: str
    categoria: str
    unidad_medida: str
    stock_actual: int
    stock_minimo: int
    precio_compra: float
    fecha_registro: datetime
    fecha_actualizacion: datetime
    estado: bool

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    pass

class Producto(ProductoBase):
    Id: int
    # Adiós al class Config viejo, hola a la nueva versión limpia:
    model_config = ConfigDict(from_attributes=True)