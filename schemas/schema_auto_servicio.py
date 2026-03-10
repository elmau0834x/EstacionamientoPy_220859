from datetime import datetime, date, time
from pydantic import BaseModel, ConfigDict

class UsuarioVehiculoServicioBase(BaseModel):
    vehiculo_Id: int
    cajero_Id: int
    operativo_Id: int
    servicio_Id: int
    fecha: date
    hora: time
    estatus: str
    descuento: float # <--- Nuevo campo
    estado: bool
    fecha_registro: datetime
    fecha_actualizacion: datetime

class UsuarioVehiculoServicioCreate(UsuarioVehiculoServicioBase):
    pass

class UsuarioVehiculoServicioUpdate(UsuarioVehiculoServicioBase):
    pass

class UsuarioVehiculoServicio(UsuarioVehiculoServicioBase):
    Id: int
    model_config = ConfigDict(from_attributes=True)