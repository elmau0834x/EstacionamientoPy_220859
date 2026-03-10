from sqlalchemy import Column, Integer, Float, ForeignKey
from config.db import Base

class TicketProducto(Base):
    '''Clase para la tabla detalle de productos en un ticket'''
    __tablename__ = "tbd_ticket_productos"
    
    Id = Column(Integer, primary_key=True, index=True)
    ticket_Id = Column(Integer, ForeignKey("tbd_usuario_vehiculo_servicio.Id"))
    producto_Id = Column(Integer, ForeignKey("tbb_productos.Id"))
    cantidad = Column(Integer)
    precio_unitario = Column(Float) # Guardamos el precio al momento de la venta