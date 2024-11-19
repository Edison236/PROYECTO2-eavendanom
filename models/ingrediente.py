from database.db import db

class Ingrediente(db.Model):

    __tablename__ = 'ingredientes'    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    calorias_por_porcion = db.Column(db.Integer, nullable=False)
    inventario = db.Column(db.Integer, default=0)
    es_vegetariano = db.Column(db.Boolean, default=True)
    es_sano = db.Column(db.Boolean, default=True)

    def __init__(self, nombre:str, precio:float, calorias_por_porcion:int, inventario:int, es_vegetariano:bool, es_sano:bool):
        self.nombre = nombre
        self.precio = precio
        self.calorias_por_porcion = calorias_por_porcion
        self.inventario = inventario
        self.es_vegetariano = es_vegetariano
        self.es_sano = es_sano

    def reabastecer(self, cantidad):
        self.inventario += cantidad

    def bajar_inventario(self):
        self.inventario = 0

        