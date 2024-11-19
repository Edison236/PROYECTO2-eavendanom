from models.producto import Producto
from database.db import db

class Malteada(Producto):
    volumen_onzas = db.Column(db.Float)  # Volumen en onzas para malteadas
