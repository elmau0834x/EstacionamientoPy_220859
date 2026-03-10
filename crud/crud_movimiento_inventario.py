from sqlalchemy.orm import Session
import models.model_movimiento_inventario
import schemas.schema_movimiento_inventario

def get_movimientos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.model_movimiento_inventario.MovimientoInventario).offset(skip).limit(limit).all()

def get_movimiento(db: Session, id: int):
    return db.query(models.model_movimiento_inventario.MovimientoInventario).filter(models.model_movimiento_inventario.MovimientoInventario.Id == id).first()

def create_movimiento(db: Session, movimiento: schemas.schema_movimiento_inventario.MovimientoInventarioCreate):
    db_movimiento = models.model_movimiento_inventario.MovimientoInventario(**vars(movimiento))
    db.add(db_movimiento)
    db.commit()
    db.refresh(db_movimiento)
    return db_movimiento

def update_movimiento(db: Session, id: int, movimiento: schemas.schema_movimiento_inventario.MovimientoInventarioUpdate):
    db_movimiento = db.query(models.model_movimiento_inventario.MovimientoInventario).filter(models.model_movimiento_inventario.MovimientoInventario.Id == id).first()
    if db_movimiento:
        for var, value in vars(movimiento).items():
            if value is not None:
                setattr(db_movimiento, var, value)
        db.add(db_movimiento)
        db.commit()
        db.refresh(db_movimiento)
    return db_movimiento

def delete_movimiento(db: Session, id: int):
    db_movimiento = db.query(models.model_movimiento_inventario.MovimientoInventario).filter(models.model_movimiento_inventario.MovimientoInventario.Id == id).first()
    if db_movimiento:
        db.delete(db_movimiento)
        db.commit()
    return db_movimiento