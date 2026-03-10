from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from config.db import Base

class Producto(Base):
    __tablename__ = "tbb_productos"
    Id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(25))
    descripcion = Column(String(100))
    categoria = Column(String(20))
    unidad_medida = Column(String(20))
    stock_actual = Column(Integer)
    stock_minimo = Column(Integer)
    precio_compra = Column(Float)
    fecha_registro = Column(DateTime)
    fecha_actualizacion = Column(DateTime)
    estado = Column(Boolean)