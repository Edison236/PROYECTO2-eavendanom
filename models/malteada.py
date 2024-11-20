from models.producto import Producto
from database.db import db

class Malteada(Producto):    
    __tablename__ = 'malteadas'
    id = id = db.Column(db.Integer, db.ForeignKey('productos.id'), primary_key=True)
    volumen_onzas = db.Column(db.Float)  # Volumen en onzas para malteadas
