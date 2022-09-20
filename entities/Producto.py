class Producto:

    def __init__(self, nombre, color, gama, cantidad, precio_costo, precio_venta, imagen):

        self.nombre = nombre
        self.color = color
        self.gama = gama
        self.cantidad = cantidad
        self.precio_costo = precio_costo
        self.precio_venta = precio_venta
        self.imagen = imagen

    def __str__(self):
        return f"""

                nombre: {self.nombre}
                color: {self.color}
                gama: {self.gama}
                cantidad: {self.cantidad}
                precio de costo: {self.precio_costo}
                precio de venta: {self.precio_venta}
                imagen: {self.imagen}
            """

    # # getter
    #
    #
    #
    # @property
    # def nombre(self):
    #     return self.__nombre
    #
    # @property
    # def color(self):
    #     return self.color
    #
    # @property
    # def gama(self):
    #     return self.__gama
    #
    # @property
    # def precio_costo(self):
    #     return self.__precio_costo
    #
    # @property
    # def precio_venta(self):
    #     return self.__precio_venta
    #
    # @property
    # def imagen(self):
    #     return self.__imagen
    #
    # # setter
    #
    #
    #
    # @nombre.setter
    # def nombre(self, nombre):
    #     self.__nombre = nombre
    #
    # @color.setter
    # def color(self, color):
    #     self.__color = color
    #
    # @gama.setter
    # def gama(self, gama):
    #     self.__gama = gama
    #
    # @precio_costo.setter
    # def precio_costo(self, precio_costo):
    #     self.__precio_costo = precio_costo
    #
    # @precio_venta.setter
    # def precio_venta(self, precio_venta):
    #     self.__precio_venta = precio_venta
    #
    # @imagen.setter
    # def imagen(self, imagen):
    #     self.__imagen = imagen
