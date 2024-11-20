from flask import Blueprint, jsonify, request, render_template
from models.producto import Producto
from app import db

producto_bp = Blueprint('producto', __name__)

@producto_bp.route('/productos', methods=['GET'])
def obtener_productos():
    productos = Producto.query.all()
    return jsonify([{'id': p.id, 'nombre': p.nombre, 'precio': p.precio_publico} for p in productos])

@producto_bp.route('/productos/nuevo', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST':
        data = request.form  # Usando formularios HTML en lugar de JSON para este ejemplo.
        nuevo_producto = Producto(nombre=data['nombre'], precio_publico=data['precio'])
        db.session.add(nuevo_producto)
        db.session.commit()
        return render_template('producto.html', productos=Producto.query.all())
    
    return render_template('producto.html', productos=Producto.query.all())

@producto_bp.route('/productos/vender', methods=['GET', 'POST'])
def vender_producto():
    return render_template('vender.html',productos=Producto.query.all())

def producto_rentable(dic_productouno: dict, dic_productodos: dict, dic_productotres: dict, dic_productocuatro: dict) -> str:
    producto_rentable = None
    producto_mas_rentable = 0.0    
    productos = [dic_productouno,dic_productodos,dic_productotres,dic_productocuatro]
    for producto in productos:
         if producto['rentabilidad'] > producto_mas_rentable:
              producto_mas_rentable = producto['rentabilidad']
              producto_rentable = producto['nombre']
    return producto_rentable

def producto_mas_rentable(self):
    mejor_rentabilidad = 0.0
    producto_rentable = None

    for producto in self.productos:
        precio_venta = producto.precio_publico
        rentabilidad = producto.calcular_rentabilidad(precio_venta)
        if rentabilidad > mejor_rentabilidad:
            mejor_rentabilidad = rentabilidad
            producto_rentable = producto
    return producto_rentable