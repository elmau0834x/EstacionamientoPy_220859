from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import config.db
import crud.crud_movimiento_inventario
import schemas.schema_movimiento_inventario
import models.model_movimiento_inventario
import auth

movimiento = APIRouter()
models.model_movimiento_inventario.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@movimiento.get("/movimiento-inventario/", response_model=List[schemas.schema_movimiento_inventario.MovimientoInventario], tags=["Movimientos de Inventario"])
async def read_movimientos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.crud_movimiento_inventario.get_movimientos(db=db, skip=skip, limit=limit)

@movimiento.post("/movimiento-inventario/", response_model=schemas.schema_movimiento_inventario.MovimientoInventario, tags=["Movimientos de Inventario"])
def create_movimiento(movimiento_data: schemas.schema_movimiento_inventario.MovimientoInventarioCreate, db: Session = Depends(get_db)):
    return crud.crud_movimiento_inventario.create_movimiento(db=db, movimiento=movimiento_data)

@movimiento.put("/movimiento-inventario/{id}", response_model=schemas.schema_movimiento_inventario.MovimientoInventario, tags=["Movimientos de Inventario"])
async def update_movimiento(id: int, movimiento_data: schemas.schema_movimiento_inventario.MovimientoInventarioUpdate, db: Session = Depends(get_db)):
    db_movimiento = crud.crud_movimiento_inventario.update_movimiento(db=db, id=id, movimiento=movimiento_data)
    if db_movimiento is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return db_movimiento

@movimiento.delete("/movimiento-inventario/{id}", response_model=schemas.schema_movimiento_inventario.MovimientoInventario, tags=["Movimientos de Inventario"])
async def delete_movimiento(id: int, db: Session = Depends(get_db), token: str = Depends(auth.oauth2_scheme)):
    db_movimiento = crud.crud_movimiento_inventario.delete_movimiento(db=db, id=id)
    if db_movimiento is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return db_movimiento