from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import config.db
import auth

import models.model_auto_servicio
import models.model_auto
import models.model_usuario
import models.model_services
import models.model_ticket_producto
import models.model_producto
import schemas.schema_reporte

reporte = APIRouter()

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@reporte.get("/reporte/ticket/{ticket_id}", tags=["Reportes"])
async def generar_reporte_ticket(ticket_id: int, db: Session = Depends(get_db)):
    # 1. Buscamos el ticket maestro
    venta = db.query(models.model_auto_servicio.VehiculoServicio).filter(models.model_auto_servicio.VehiculoServicio.Id == ticket_id).first()
    if not venta:
        raise HTTPException(status_code=404, detail="El ticket de venta no existe")

    # 2. Extraemos la información base
    vehiculo = db.query(models.model_auto.Vehiculo).filter(models.model_auto.Vehiculo.Id == venta.vehiculo_Id).first()
    cliente = db.query(models.model_usuario.Usuario).filter(models.model_usuario.Usuario.Id == vehiculo.usuario_Id).first()
    servicio = db.query(models.model_services.Servicios).filter(models.model_services.Servicios.Id == venta.servicio_Id).first()
    operativo = db.query(models.model_usuario.Usuario).filter(models.model_usuario.Usuario.Id == venta.operativo_Id).first()
    cajero = db.query(models.model_usuario.Usuario).filter(models.model_usuario.Usuario.Id == venta.cajero_Id).first()

    # 3. Matemáticas del Servicio (Lavado)
    subtotal_servicio = servicio.costo
    descuento_porcentaje = venta.descuento if venta.descuento else 0.0
    monto_descuento = subtotal_servicio * (descuento_porcentaje / 100)
    total_servicio = subtotal_servicio - monto_descuento

    # 4. Buscamos los Productos comprados en este ticket
    items_comprados = db.query(models.model_ticket_producto.TicketProducto).filter(models.model_ticket_producto.TicketProducto.ticket_Id == ticket_id).all()
    
    lista_productos_json = []
    total_productos = 0.0

    for item in items_comprados:
        prod_db = db.query(models.model_producto.Producto).filter(models.model_producto.Producto.Id == item.producto_Id).first()
        subtotal_item = item.cantidad * item.precio_unitario
        total_productos += subtotal_item
        
        lista_productos_json.append({
            "producto": prod_db.nombre,
            "cantidad": item.cantidad,
            "precio_unitario": item.precio_unitario,
            "subtotal": subtotal_item
        })

    # 5. Calculamos el Gran Total
    gran_total = total_servicio + total_productos

    # 6. Construimos la factura completa
    return {
        "ticket_id": venta.Id,
        "cliente": f"{cliente.nombre} {cliente.primer_apellido}",
        "vehiculo": f"{vehiculo.modelo} ({vehiculo.placa})",
        "cajero": cajero.nombre,
        "chalán": operativo.nombre,
        "detalle_servicio": {
            "lavado": servicio.nombre,
            "costo_base": subtotal_servicio,
            "descuento_aplicado": f"{descuento_porcentaje}%",
            "dinero_descontado": monto_descuento,
            "total_lavado": total_servicio
        },
        "detalle_productos": lista_productos_json,
        "resumen_cuenta": {
            "total_servicios": total_servicio,
            "total_tienda": total_productos,
            "GRAN_TOTAL": gran_total
        }
    }