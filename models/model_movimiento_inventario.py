from sqlalchemy import Column, Integer, DateTime, ForeignKey, Enum as SQLEnum
import enum
from config.db import Base

class TipoMovimiento(str, enum.Enum):
    '''Opciones permitidas para el tipo de movimiento'''
    Entrada = "Entrada"
    Salida = "Salida"

class MovimientoInventario(Base):
    '''Clase para la tabla de historial de movimientos de inventario'''
    __tablename__ = "tbd_movimiento_inventario"
    
    Id = Column(Integer, primary_key=True, index=True)
    producto_Id = Column(Integer, ForeignKey("tbb_productos.Id"))
    tipo_movimiento = Column(SQLEnum(TipoMovimiento))
    cantidad = Column(Integer)
    fecha_movimiento = Column(DateTime)
    usuario_Id = Column(Integer, ForeignKey("tbb_usuarios.Id"))