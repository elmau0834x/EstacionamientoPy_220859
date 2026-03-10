from sqlalchemy.orm import Session
import models.model_producto
import schemas.schema_producto

def get_productos(db: Session, skip: int = 0, limit: int = 100):
    # Bug del límite corregido:
    return db.query(models.model_producto.Producto).offset(skip).limit(limit).all()

def get_producto(db: Session, id: int):
    return db.query(models.model_producto.Producto).filter(models.model_producto.Producto.Id == id).first()

def create_producto(db: Session, producto: schemas.schema_producto.ProductoCreate):
    db_producto = models.model_producto.Producto(**vars(producto))
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

# --- Funciones nuevas para tener tu CRUD completo ---
def update_producto(db: Session, id: int, producto: schemas.schema_producto.ProductoUpdate):
    db_producto = db.query(models.model_producto.Producto).filter(models.model_producto.Producto.Id == id).first()
    if db_producto:
        for var, value in vars(producto).items():
            if value is not None:
                setattr(db_producto, var, value)
        db.add(db_producto)
        db.commit()
        db.refresh(db_producto)
    return db_producto

def delete_producto(db: Session, id: int):
    db_producto = db.query(models.model_producto.Producto).filter(models.model_producto.Producto.Id == id).first()
    if db_producto:
        db.delete(db_producto)
        db.commit()
    return db_producto