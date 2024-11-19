from database.db import db

class Producto(db.Model):
    __tablename__ = 'productos'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio_publico = db.Column(db.Float, nullable=False)
    
    ingredientes = db.relationship('Ingrediente', secondary='producto_ingredientes')
    
    def calcular_calorias(self):
        return sum(ingrediente.calorias_por_porcion for ingrediente in self.ingredientes)

    def calcular_costo(self):
        return sum(ingrediente.precio for ingrediente in self.ingredientes)

producto_ingredientes = db.Table('producto_ingredientes',
    db.Column('producto_id', db.Integer, db.ForeignKey('productos.id')),
    db.Column('ingrediente_id', db.Integer, db.ForeignKey('ingredientes.id'))
)