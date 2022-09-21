class ModelCompras:

    @classmethod
    def insertarCompra(cls, db, compra):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO compras 
                        (id_provedor, fecha, sub_total, iva, total) 
                        VALUES (%s, %s, %s, %s, %s)
                    """
            values = (
                compra.id_provedor,
                compra.fecha,
                compra.sub_total,
                compra.iva,
                compra.total
            )
            cursor.execute(sql, values)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)