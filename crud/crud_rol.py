import models.rol as model_rol
from sqlalchemy.orm import Session

def get_rol(db: Session, skip: int = 0, limit: int = 100):
    '''Función para obtener los roles'''
    return db.query(models.model_rol.Rol).offset(skip).limit(limit).all()

def get_rol_py_nombre(db: Session,skip: int = 0, limit: int = 100):
    return db.query(models.model_rol.rol).filter(models.model_rol.Rol.nombre_rol == nombre_rol).first()

def create_rol(db:Session, rol: schemas.schema_rol.RolCreate):
    return db_rol

def update_rol(db:Session, id: int, rol: schemas.model_rol.RolUpdate):

    db_rol = db.query(models.model_rol.Rol.filter)