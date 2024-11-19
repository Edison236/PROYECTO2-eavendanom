from flask import Blueprint, jsonify, request, render_template
from models.producto import Producto
from app import db

producto_bp = Blueprint('producto', __name__)

@producto_bp.route('/productos', methods=['GET'])
def obtener_productos():
    productos = Producto.query.all()
    return jsonify([{'id': p.id, 'nombre': p.nombre, 'precio': p.precio_publico} for p in productos])

@producto_bp.route('/productos/nuevo', methods=['GET', 'POST'])
def crear_producto():
    if request.method == 'POST':
        data = request.form  # Usando formularios HTML en lugar de JSON para este ejemplo.
        nuevo_producto = Producto(nombre=data['nombre'], precio_publico=data['precio'])
        db.session.add(nuevo_producto)
        db.session.commit()
        return render_template('producto.html', productos=Producto.query.all())
    
    return render_template('producto.html', productos=Producto.query.all())