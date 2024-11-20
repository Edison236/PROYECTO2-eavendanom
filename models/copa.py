from models.producto import Producto
from database.db import db

class Copa(Producto):

    __tablename__ = 'copa'
    id = id = db.Column(db.Integer, db.ForeignKey('productos.id'), primary_key=True)
    tipo_vaso = db.Column(db.String(50))  # Tipo de vaso específico para copas
