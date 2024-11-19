from models.producto import Producto
from database.db import db

class Copa(Producto):
    tipo_vaso = db.Column(db.String(50))  # Tipo de vaso específico para copas
