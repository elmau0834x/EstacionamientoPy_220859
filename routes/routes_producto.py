from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import config.db
import crud.crud_producto
import schemas.schema_producto
import models.model_producto
import auth  # Tu archivo de seguridad

producto = APIRouter()
models.model_producto.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET - Todos los productos protegidos
@producto.get("/producto/", response_model=List[schemas.schema_producto.Producto], tags=["Productos"])
async def read_productos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.crud_producto.get_productos(db=db, skip=skip, limit=limit)

# POST - Ruta corregida y protegida
@producto.post("/producto/", response_model=schemas.schema_producto.Producto, tags=["Productos"])
def create_producto(producto_data: schemas.schema_producto.ProductoCreate, db: Session = Depends(get_db)):
    return crud.crud_producto.create_producto(db=db, producto=producto_data)

# PUT - Nuevo
@producto.put("/producto/{id}", response_model=schemas.schema_producto.Producto, tags=["Productos"])
async def update_producto(id: int, producto_data: schemas.schema_producto.ProductoUpdate, db: Session = Depends(get_db)):
    db_producto = crud.crud_producto.update_producto(db=db, id=id, producto=producto_data)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no existe")
    return db_producto

# DELETE - Nuevo
@producto.delete("/producto/{id}", response_model=schemas.schema_producto.Producto, tags=["Productos"])
async def delete_producto(id: int, db: Session = Depends(get_db), token: str = Depends(auth.oauth2_scheme)):
    db_producto = crud.crud_producto.delete_producto(db=db, id=id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no existe")
    return db_producto