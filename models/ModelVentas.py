class ModelVentas:

    @classmethod
    def mostrardatosVenta(cls, db, id):
        try:
            cursor = db.connection.cursor()
            sql = 'SELECT * FROM clientes WHERE id_cliente = {}'.format(id)
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