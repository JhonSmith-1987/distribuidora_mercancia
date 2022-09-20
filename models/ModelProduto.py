class ModelProduto:

    @classmethod
    def insertProduct(cls, db, producto):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO producto 
                        (nombre, color, gama, cantidad, precio_costo, precio_venta, imagen) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                 """
            values = (
                      producto.nombre,
                      producto.color,
                      producto.gama,
                      producto.cantidad,
                      producto.precio_costo,
                      producto.precio_venta,
                      producto.imagen
                      )
            cursor.execute(sql, values)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def mostrarProductos(cls, db):
        try:
            cursor = db.connection.cursor()
            sql = 'SELECT * FROM producto'
            cursor.execute(sql)
            data = cursor.fetchall()
            if data != None:
                return data
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def eliminarProducto(cls, db, id):
        try:
            cursor = db.connection.cursor()
            sql = 'DELETE FROM producto WHERE id_producto={}'.format(id)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

