from pydantic import BaseModel

class ReporteTicket(BaseModel):
    '''Molde para el JSON del reporte de venta con porcentaje'''
    ticket_id: int
    cliente_nombre: str
    vehiculo_info: str
    servicio_realizado: str
    nombre_operativo: str
    nombre_cajero: str
    subtotal: float
    porcentaje_descuento: float  # <--- Aquí diremos "15" (que será 15%)
    monto_descuento: float       # <--- Aquí diremos a cuánto dinero equivale ese 15%
    total_a_pagar: float