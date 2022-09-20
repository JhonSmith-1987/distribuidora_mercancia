class TablaTemporal:

    def __init__(self, cantidad, descripcion, valor_unit, valor_total):
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.valor_unit = valor_unit
        self.valor_total = valor_total

    def __str__(self):
        return f"""
                cantidad: {self.cantidad}
                descripcion: {self.descripcion}
                valor unidad: {self.valor_unit}
                valor total: {self.valor_total}
            """