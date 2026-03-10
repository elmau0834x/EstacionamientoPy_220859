from sqlalchemy import Column, Integer, Boolean, DateTime, Date, Time, ForeignKey, Enum as SQLEnum, Float
import enum
from config.db import Base

class Solicitud(str, enum.Enum):
    Programada = "Programada"
    Proceso = "Proceso"
    Realizada = "Realizada"
    Cancelada = "Cancelada"

class VehiculoServicio(Base):
    __tablename__ = "tbd_usuario_vehiculo_servicio"
    Id = Column(Integer, primary_key=True, index=True)
    vehiculo_Id = Column(Integer, ForeignKey("tbb_vehiculos.Id"))
    cajero_Id = Column(Integer, ForeignKey("tbb_usuarios.Id"))
    operativo_Id = Column(Integer, ForeignKey("tbb_usuarios.Id"))
    servicio_Id = Column(Integer, ForeignKey("tbc_servicios.Id"))
    fecha = Column(Date)
    hora = Column(Time)
    estatus = Column(SQLEnum(Solicitud))
    descuento = Column(Float, default=0.0) # <--- Nuevo campo para la venta
    estado = Column(Boolean)
    fecha_registro = Column(DateTime)
    fecha_actualizacion = Column(DateTime)