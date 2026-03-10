from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List
import config.db
import auth

import schemas.schema_ticket_producto
import models.model_ticket_producto
import models.model_producto
import models.model_movimiento_inventario

ticket_producto = APIRouter()
models.model_ticket_producto.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@ticket_producto.post("/ticket-producto/", response_model=schemas.schema_ticket_producto.TicketProducto, tags=["Ventas y Asignaciones"])
def agregar_producto_al_ticket(
    item_data: schemas.schema_ticket_producto.TicketProductoCreate, 
    usuario_id_cajero: int, 
    db: Session = Depends(get_db), 
):
    # 1. Verificamos que el producto exista en el catálogo
    producto_db = db.query(models.model_producto.Producto).filter(models.model_producto.Producto.Id == item_data.producto_Id).first()
    if not producto_db:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    if producto_db.stock_actual < item_data.cantidad:
        raise HTTPException(status_code=400, detail=f"Stock insuficiente. Solo quedan {producto_db.stock_actual} en inventario.")

    # 2. CREAMOS EL ITEM MANUALMENTE PARA INYECTARLE EL PRECIO AUTOMÁTICAMENTE
    # Nota: Tomamos 'precio_compra' del catálogo de productos.
    nuevo_item = models.model_ticket_producto.TicketProducto(
        ticket_Id=item_data.ticket_Id,
        producto_Id=item_data.producto_Id,
        cantidad=item_data.cantidad,
        precio_unitario=producto_db.precio_compra  # <--- MAGIA: El sistema pone el precio solo
    )
    db.add(nuevo_item)

    # 3. Restamos el stock del catálogo principal
    producto_db.stock_actual -= item_data.cantidad
    db.add(producto_db)

    # 4. Creamos el registro automático de "Salida" en el inventario
    nuevo_movimiento = models.model_movimiento_inventario.MovimientoInventario(
        producto_Id=producto_db.Id,
        tipo_movimiento="Salida",
        cantidad=item_data.cantidad,
        fecha_movimiento=datetime.now(),
        usuario_Id=usuario_id_cajero
    )
    db.add(nuevo_movimiento)
    
    # Guardamos todos los cambios al mismo tiempo
    db.commit()
    db.refresh(nuevo_item) # Actualizamos para que FastAPI pueda leer el ID que le dio MySQL

    return nuevo_item

@ticket_producto.get("/ticket-producto/{ticket_id}", response_model=List[schemas.schema_ticket_producto.TicketProducto], tags=["Ventas y Asignaciones"])
def ver_productos_del_ticket(ticket_id: int, db: Session = Depends(get_db)):
    # Esta parte se queda igual (puedes copiar el import de crud_ticket_producto si lo tenías)
    return db.query(models.model_ticket_producto.TicketProducto).filter(models.model_ticket_producto.TicketProducto.ticket_Id == ticket_id).all()