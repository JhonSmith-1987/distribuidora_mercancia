class ModelVentas:

    @classmethod
    def mostrardatosVenta(cls, db, id):
        try:
            cursor = db.connection.cursor()
            sql = 'SELECT * FROM clientes WHERE id_provedor = {}'.format(id)
            cursor.execute(sql)
            data = cursor.fetchone()
            if data != None:
                return data
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def seleccionarNombreProductos(cls, db):
        try:
            cursor = db.connection.cursor()
            sql = 'SELECT nombre FROM producto'
            cursor.execute(sql)
            data = cursor.fetchall()
            if data != None:
                return data
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def mostrardatosCompra(cls, db, id):
        try:
            cursor = db.connection.cursor()
            sql = 'SELECT * FROM provedores WHERE id_provedor = {}'.format(id)
            cursor.execute(sql)
            data = cursor.fetchone()
            if data != None:
                return data
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def mostrarSumaTotalCompra(cls, db):
        try:
            cursor = db.connection.cursor()
            sql = 'SELECT SUM(valor_total) FROM tabla_temporal'
            cursor.execute(sql)
            data = cursor.fetchone()
            if data != None:
                return data[0].to_integral_value()
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

