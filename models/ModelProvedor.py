class ModelProvedor:

    @classmethod
    def insertarProvedor(cls, db, provedor):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO provedores 
                            (nombre, razon_social, nit, direccion, ciudad, email) 
                            VALUES (%s, %s, %s, %s, %s, %s)
                     """
            values = (
                provedor.nombre,
                provedor.razon_social,
                provedor.nit,
                provedor.direccion,
                provedor.ciudad,
                provedor.email,
            )
            cursor.execute(sql, values)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def mostrarProvedor(cls, db):
        try:
            cursor = db.connection.cursor()
            sql = 'SELECT * FROM provedores'
            cursor.execute(sql)
            data = cursor.fetchall()
            if data != None:
                return data
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def eliminarProvedor(cls, db, id):
        try:
            cursor = db.connection.cursor()
            sql = 'DELETE FROM provedores WHERE id_provedor={}'.format(id)
            cursor.execute(sql)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)