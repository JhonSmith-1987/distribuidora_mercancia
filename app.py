from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
import os

from datetime import date
from config import config

# Models:
from models.ModelProduto import ModelProduto
from models.ModelCliente import ModelCliente
from models.ModelProvedor import ModelProvedor


# Entities:
from entities.Producto import Producto
from entities.Clientes import Clientes
from entities.Provedores import Provedores


app = Flask(__name__)
db = MySQL(app)


@app.route('/')
def index():
    return render_template('administracion.html')


# ******************************* CLIENTES **********************************
@app.route('/nuevo_cliente')
def nuevoCliente():
    return render_template('nuevo_cliente.html')


@app.route('/insertar_cliente', methods=['POST'])
def crear_cliente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        razon_social = request.form['razon_social']
        nit = request.form['nit']
        direccion = request.form['direccion']
        ciudad = request.form['ciudad']
        email = request.form['email']
        cliente = Clientes(nombre, razon_social, nit, direccion, ciudad, email)
        ModelCliente.insertarClinete(db, cliente)
        flash('Cliente creado con exito')
        return redirect(url_for('index'))
    else:
        flash('hubo un error con la creacion del cliente')
        return redirect(url_for('index'))


@app.route('/mostrar_clientes')
def mostrarClientes():
    datos = ModelCliente.mostrarClientes(db)
    return render_template('mostrar_clientes.html', datos=datos)


@app.route('/eliminar_cliente/<id>')
def eliminarCliente(id):
    ModelCliente.eliminarCliente(db, id)
    return redirect(url_for('mostrarClientes'))


# ******************************* PROVEDORES **********************************
@app.route('/nuevo_provedor')
def nuevoProvedor():
    return render_template('nuevo_provedor.html')


@app.route('/insertar_provedor', methods=['POST'])
def crearProvedor():
    if request.method == 'POST':
        nombre = request.form['nombre']
        razon_social = request.form['razon_social']
        nit = request.form['nit']
        direccion = request.form['direccion']
        ciudad = request.form['ciudad']
        email = request.form['email']
        provedor = Provedores(nombre, razon_social, nit, direccion, ciudad, email)
        ModelProvedor.insertarProvedor(db, provedor)
        flash('Provedor creado con exito')
        return redirect(url_for('index'))
    else:
        flash('hubo un error con la creacion del provedor')
        return redirect(url_for('index'))


@app.route('/mostrar_provedor')
def mostrarProvedor():
    datos = ModelProvedor.mostrarProvedor(db)
    return render_template('mostrar_provedor.html', datos=datos)


@app.route('/eliminar_provedor/<id>')
def eliminarProvedor(id):
    ModelProvedor.eliminarProvedor(db, id)
    return redirect(url_for('mostrarProvedor'))


# ******************************** PRODUCTOS *****************************
@app.route('/nuevo_producto')
def nuevoProducto():
    return render_template('nuevo_producto.html')


@app.route('/insertar_producto', methods=['POST'])
def createProduct():
    if request.method == 'POST':
        nombre = request.form['nombre']
        color = request.form['color']
        gama = request.form['gama']
        precio_costo = request.form['precio_costo']
        precio_venta = request.form['precio_venta']
        file = request.files['file']
        basepath = os.path.dirname(__file__)
        filename = secure_filename(file.filename)
        extension = os.path.splitext(filename)[1]
        nuevo_nombre_file = nombre + extension
        upload_path = os.path.join(basepath, 'static/img_productos', nuevo_nombre_file)
        file.save(upload_path)
        producto = Producto(nombre, color, gama, precio_costo, precio_venta, imagen=nuevo_nombre_file)
        ModelProduto.insertProduct(db, producto)
        flash('Producto creado con exito')
        return redirect(url_for('index'))
    else:
        flash('hubo un error con la creacion del producto')
        return redirect(url_for('index'))


@app.route('/mostrar_productos')
def mostrarProductos():
    datos = ModelProduto.mostrarProductos(db)
    return render_template('mostrar_productos.html', datos=datos)


@app.route('/eliminar_producto/<id>')
def eliminarProducto(id):
    ModelProduto.eliminarProducto(db, id)
    return redirect(url_for('mostrarProductos'))


def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return "<h1>Página no encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
