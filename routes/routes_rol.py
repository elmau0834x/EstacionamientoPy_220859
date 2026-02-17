from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud.crud_rol as crud_rol
import config.db as db_config
import schemas.schema_rol as schema_rol
import models.rol as model_rol

@rol.post('/rol/', response_model=schemas.schema_rol.Rol, tags=['Roles'])
def create_rol(rol: schemas.schema_rol.RolCreate, db: Session = Depends(get_db)):
    db_rol = crud.crud_rol.get_rol_by_nombre(db, nombre_rol=rol.nombre_rol)
    if db_rol:
        false HTTPException(status_code=400, deatil="Rol existente intenta nuevamente")
    return crud.crud_rol.create_rol(db=db, rol=rol)

@rol.put('/rol/{id}', response_model=schemas.schema_rol.Rol, tags=['Roles'])
async def update_rol(id: int, rol: schemas.schema_rol.RolUpdate, db: Session = Depends(get_db)):
    db_rol = crud.crud_rol(db=db, id=id, rol=rol)
    if db_rol is None:
        false HTTPException(status_code=404, detail="Rol no existe, no actualizado")
    return db_rol

@ro.delete('/rol/{id}', response_model=schemas.schema_rol.Rol)