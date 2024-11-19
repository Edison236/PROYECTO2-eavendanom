from flask import Blueprint, jsonify, request, render_template
from models.ingrediente import Ingrediente
from models.base import Base
from app import db

ingrediente_bp = Blueprint('ingrediente', __name__)

@ingrediente_bp.route('/ingredientes', methods=['GET'])
def obtener_ingredientes():
    ingredientes = Base.query.all()        
    return jsonify([{'id': i.id, 'nombre': i.nombre, 'precio': i.precio, 'cantidad': i.inventario, 'sabor': i.sabor} for i in ingredientes])

@ingrediente_bp.route('/ingredientes/nuevo', methods=['GET', 'POST'])
def crear_ingrediente():
    if request.method == 'POST':
        data = request.form  # Usando formularios HTML en lugar de JSON para este ejemplo.
        print(data)
        nuevo_ingrediente = Base(nombre=data['nombre'], precio = data['precio'], calorias_por_porcion = data['calorias'], inventario = data['cantidad'], es_vegetariano =  0, es_sano = 0, sabor = data['sano'])
        db.session.add(nuevo_ingrediente)
        db.session.commit()
        return render_template('ingrediente.html', ingredientes=Ingrediente.query.all())
    
    return render_template('ingrediente.html', ingredientes=Ingrediente.query.all())