from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
import os

from datetime import date
from config import config

# Models:
from models.ModelProduto import ModelProduto


# Entities:
from entities.Producto import Producto


app = Flask(__name__)
db = MySQL(app)


@app.route('/')
def index():
    return render_template('administracion.html')


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


def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return "<h1>Página no encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
