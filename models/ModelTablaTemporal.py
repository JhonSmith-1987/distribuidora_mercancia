class ModelTablaTemporal:

    @classmethod
    def insertDatosTablaTemp(cls, db, dato_tabla_temp):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO tabla_temporal 
                            (cantidad, detalle, valor_unit, valor_total) 
                            VALUES (%s, %s, %s, %s)
                     """
            values = (
                dato_tabla_temp.cantidad,
                dato_tabla_temp.descripcion,
                dato_tabla_temp.valor_unit,
                dato_tabla_temp.valor_total
            )
            cursor.execute(sql, values)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def mostrarTablaTemporal(cls, db):
        try:
            cursor = db.connection.cursor()
            sql = 'SELECT * FROM tabla_temporal'
            cursor.execute(sql)
            data = cursor.fetchall()
            if data != None:
                return data
            else:
                return None
        except Exception as ex:
            raise Exception(ex)