from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
import os
from datetime import date

from datetime import date
from config import config

# Models:
from models.ModelProduto import ModelProduto
from models.ModelCliente import ModelCliente
from models.ModelProvedor import ModelProvedor
from models.ModelVentas import ModelVentas
from models.ModelCompras import ModelCompras
from models.ModelTablaTemporal import ModelTablaTemporal
from models.ModelPuc import ModelPuc

# Entities:
from entities.Producto import Producto
from entities.Clientes import Clientes
from entities.Provedores import Provedores
from entities.Compras import Compras
from entities.Ventas import Ventas
from entities.TablaTemporal import TablaTemporal

app = Flask(__name__)
db = MySQL(app)
fecha = date.today()


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
        cantidad = request.form['cantidad']
        precio_costo = request.form['precio_costo']
        precio_venta = request.form['precio_venta']
        file = request.files['file']
        basepath = os.path.dirname(__file__)
        filename = secure_filename(file.filename)
        extension = os.path.splitext(filename)[1]
        nuevo_nombre_file = nombre + extension
        upload_path = os.path.join(basepath, 'static/img_productos', nuevo_nombre_file)
        file.save(upload_path)
        producto = Producto(nombre, color, gama, cantidad, precio_costo, precio_venta, imagen=nuevo_nombre_file)
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


# ******************************** VENTAS *****************************
@app.route('/ventas')
def ventas():
    datos = ModelCliente.mostrarClientes(db)
    return render_template('ventas.html', datos=datos)


@app.route('/ventas1/<id>')
def ventasUno(id):
    datos = ModelVentas.mostrardatosVenta(db, id)
    nombre_productos = ModelVentas.seleccionarNombreProductos(db)
    fecha = date.today()
    return render_template('ventas1.html', datos=datos, fecha=fecha, nombre_productos=nombre_productos)


@app.route('/ingresar_venta', methods=['POST'])
def ingresarVenta():
    if request.method == 'POST':
        cantidad = request.form['cantidad']
        descripcion = request.form['descripcion']
        valor = request.form['valor']
        tipo_de_pago = request.form['tipo_de_pago']
        print(f"""
            cantidad: {cantidad}
            descripcion: {descripcion}
            valor: {valor}
            tipo de pago: {tipo_de_pago}
            
""")
        return 'si funciona'


# ******************************** COMPRAS *****************************
@app.route('/compras')
def Compras():
    provedores = ModelProvedor.mostrarProvedor(db)
    nombre_productos = ModelVentas.seleccionarNombreProductos(db)
    suma_total = int(ModelVentas.mostrarSumaTotalCompra(db))
    iva = round(suma_total * 0.19)
    total = suma_total + iva
    print(provedores)
    return render_template('compras1.html', provedores=provedores, total=total, iva=iva,
                           nombre_productos=nombre_productos, suma_total=suma_total)


@app.route('/ingresar_compra', methods=['POST'])
def ingresarCompra():
    if request.method == 'POST':
        cantidad = int(request.form['cantidad'])
        descripcion = request.form['descripcion']
        valor = int(request.form['valor_unit'])
        valor_total = valor * cantidad
        dato_tabla_temp = TablaTemporal(cantidad, descripcion, valor_unit=valor, valor_total=valor_total)
        ModelTablaTemporal.insertDatosTablaTemp(db, dato_tabla_temp)
        flash('compra agregada correctamente')
        return redirect(url_for('Compras'))


@app.route('/ver_guardar_compras/<id>')
def verGuardarCompras(id):
    datos_prov = ModelVentas.mostrardatosCompra(db, id)
    datos_compra = ModelTablaTemporal.mostrarTablaTemporal(db)
    suma_total = int(ModelVentas.mostrarSumaTotalCompra(db))
    iva = round(suma_total * 0.19)
    total = suma_total + iva
    id_provedor = int(datos_prov[0])
    compra = Compras(id_provedor, fecha, sub_total=suma_total, iva=iva, total=total)
    ModelCompras.insertarCompra(db, compra)
    print(datos_prov)
    return render_template('compras.html', suma_total=suma_total, iva=iva, total=total, datos_prov=datos_prov, fecha=fecha, datos_compra=datos_compra)


# ******************************** PUC *****************************
@app.route('/crear_puc')
def crearPuc():
    return render_template('crear_puc.html')


@app.route('/guardar_puc', methods=['POST'])
def guardarPuc():
    if request.method == 'POST':
        cuenta = request.form['cuenta']
        codigo = request.form['codigo']
        ModelPuc.insertarPuc(db, cuenta, codigo)
        ModelPuc.crearTablasPuc(db, cuenta)
        flash('dato guardado en el puc y cuenta creada')
        return redirect(url_for('crearPuc'))
    else:
        flash('no guardo, revisar')
        return redirect(url_for('crearPuc'))


@app.route('/mostrar_puc')
def mostrarPuc():
    datos = ModelPuc.mostrarPuc(db)
    return render_template('mostrar_puc.html', datos=datos)


@app.route('/mostrar_tabla_puc/<tabla>')
def mostrarTablaPuc(tabla):
    datos = ModelPuc.mostrarTablaPuc(db, tabla)
    return render_template('mostrar_tabla_puc.html', tabla=tabla, datos=datos)


# ******************************** MANEJO DE ERRORES *****************************
def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return "<h1>P??gina no encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
