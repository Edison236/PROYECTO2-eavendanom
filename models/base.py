from models.ingrediente import Ingrediente
from database.db import db

class Base(Ingrediente):
    __tablename__ = 'bases'
    id = id = db.Column(db.Integer, db.ForeignKey('ingredientes.id'), primary_key=True)
    sabor = db.Column(db.String(50), nullable=False) 

    def __init__(self, nombre, precio, calorias_por_porcion, inventario, es_vegetariano, es_sano, sabor:str):
        super().__init__(nombre, precio, calorias_por_porcion, inventario, es_vegetariano, es_sano)
        self.sabor = sabor