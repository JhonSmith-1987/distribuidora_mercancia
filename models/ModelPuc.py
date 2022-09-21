class ModelPuc:

    @classmethod
    def insertarPuc(cls, db, cuenta, codigo):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO puc 
                                (cuenta, codigo) 
                                VALUES (%s, %s)
                         """
            values = (
                cuenta, codigo
            )
            cursor.execute(sql, values)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def crearTablasPuc(cls, db, cuenta):
        cursor = db.connection.cursor()
        sql = f"""CREATE TABLE `{cuenta}`(
                        id int(10) AUTO_INCREMENT PRIMARY KEY,
                        fecha VARCHAR(250),
                        detalle VARCHAR(250),
                        debe INT(250),
                        haber INT(250)
                    )"""
        cursor.execute(sql)
        db.connection.commit()

    @classmethod
    def mostrarPuc(cls, db):
        try:
            cursor = db.connection.cursor()
            sql = 'SELECT * FROM puc'
            cursor.execute(sql)
            data = cursor.fetchall()
            if data != None:
                return data
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def mostrarTablaPuc(cls, db, tabla):
        try:
            cursor = db.connection.cursor()
            sql = f'SELECT * FROM {tabla}'
            cursor.execute(sql)
            data = cursor.fetchall()
            if data != None:
                return data
            else:
                return None
        except Exception as ex:
            raise Exception(ex)