class ModelCliente:

    @classmethod
    def insertarClinete(cls, db, cliente):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO clientes 
                            (nombre, razon_social, nit, direccion, ciudad, email) 
                            VALUES (%s, %s, %s, %s, %s, %s)
                     """
            values = (
                cliente.nombre,
                cliente.razon_social,
                cliente.nit,
                cliente.direccion,
                cliente.ciudad,
                cliente.email,
            )
            cursor.execute(sql, values)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def mostrarClientes(cls, db):
        try:
            cursor = db.connection.cursor()
            sql = 'SELECT * FROM clientes'
            cursor.execute(sql)
            data = cursor.fetchall()
            if data != None:
                return data
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def eliminarCliente(cls, db, id):
        try:
            cursor = db.connection.cursor()
            sql = 'DELETE FROM clientes WHERE id_cliente={}'.format(id)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)