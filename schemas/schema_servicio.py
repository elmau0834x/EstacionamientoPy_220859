from datetime import datetime
from pydantic import BaseModel, ConfigDict

class ServicioBase(BaseModel):
    nombre: str
    descripcion: str
    costo: float
    descuento: float  # <--- Nuevo campo
    duracion_minutos: int
    estado: bool
    fecha_registro: datetime
    fecha_actualizacion: datetime

class ServicioCreate(ServicioBase):
    pass

class ServicioUpdate(ServicioBase):
    pass

class Servicio(ServicioBase):
    Id: int
    model_config = ConfigDict(from_attributes=True)