from sqlalchemy.orm import Session
import models.model_ticket_producto
import schemas.schema_ticket_producto

def get_productos_por_ticket(db: Session, ticket_id: int):
    # Busca todos los productos que pertenecen a un ticket específico
    return db.query(models.model_ticket_producto.TicketProducto).filter(models.model_ticket_producto.TicketProducto.ticket_Id == ticket_id).all()

def add_producto_a_ticket(db: Session, item: schemas.schema_ticket_producto.TicketProductoCreate):
    db_item = models.model_ticket_producto.TicketProducto(**vars(item))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item