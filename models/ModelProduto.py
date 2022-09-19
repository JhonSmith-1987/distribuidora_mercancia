class ModelProduto:

    @classmethod
    def insertProduct(cls, db, producto):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO producto 
                        (nombre, color, gama, precio_costo, precio_venta, imagen) 
                        VALUES (%s, %s, %s, %s, %s, %s)
                 """
            values = (
                      producto.nombre,
                      producto.color,
                      producto.gama,
                      producto.precio_costo,
                      producto.precio_venta,
                      producto.imagen
                      )
            cursor.execute(sql, values)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)