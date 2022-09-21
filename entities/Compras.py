class Compras:

    def __init__(self, id_provedor, fecha, sub_total, iva, total):
        self.id_provedor = id_provedor
        self.fecha = fecha
        self.sub_total = sub_total
        self.iva = iva
        self.total = total

    def __str__(self):
        return f"""
                id_cliente: {self.id_provedor}
                fecha: {self.fecha}
                bub_total: {self.sub_total}
                iva: {self.iva}
                total: {self.total}
            """
