class Ventas:

    def __init__(self, id_venta, id_cliente, fecha, forma_pago, bub_total, iva, total):
        self.__id_venta = id_venta
        self.__id_cliente = id_cliente
        self.__fecha = fecha
        self.__forma_pago = forma_pago
        self.__sub_total = bub_total
        self.__iva = iva
        self.__total = total

    def __str__(self):
        return f"""
                id_venta: {self.__id_venta}
                id_cliente: {self.__id_cliente}
                fecha: {self.__fecha}
                forma_pago: {self.__forma_pago}
                bub_total: {self.__sub_total}
                iva: {self.__iva}
                total: {self.__total}
            """

    # getter

    @property
    def id_venta(self):
        return self.__id_venta

    @property
    def id_cliente(self):
        return self.__id_cliente

    @property
    def fecha(self):
        return self.__fecha

    @property
    def forma_pago(self):
        return self.__forma_pago

    @property
    def bub_total(self):
        return self.__sub_total

    @property
    def iva(self):
        return self.__iva

    @property
    def total(self):
        return self.__total

    # setter

    @id_venta.setter
    def id_venta(self, id_venta):
        self.__id_venta = id_venta

    @id_cliente.setter
    def id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente

    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha

    @forma_pago.setter
    def forma_pago(self, forma_pago):
        self.__forma_pago = forma_pago

    @bub_total.setter
    def bub_total(self, bub_total):
        self.__sub_total = bub_total

    @iva.setter
    def iva(self, iva):
        self.__iva = iva

    @total.setter
    def total(self, total):
        self.__total = total