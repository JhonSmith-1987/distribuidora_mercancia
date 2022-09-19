class Clientes:

    def __init__(self, id_cliente, nombre, razon_social, nit, direccion, ciudad, email):
        self.__id_cliente = id_cliente
        self.__nombre = nombre
        self.__razon_social = razon_social
        self.__nit = nit
        self.__direccion = direccion
        self.__ciudad = ciudad
        self.__email = email

    def __str__(self):
        return f"""
                id: {self.__id_cliente}
                nombre: {self.__nombre}
                razon social: {self.__razon_social}
                nit: {self.__nit}
                direccion: {self.__direccion}
                ciudad: {self.__ciudad}
                email: {self.__email}
            """

    # getter

    @property
    def id_cliente(self):
        return self.__id_cliente

    @property
    def nombre(self):
        return self.__nombre

    @property
    def razon_social(self):
        return self.__razon_social

    @property
    def nit(self):
        return self.__nit

    @property
    def direccion(self):
        return self.__direccion

    @property
    def ciudad(self):
        return self.__ciudad

    @property
    def email(self):
        return self.__email

    # setter

    @id_cliente.setter
    def id(self, id):
        self.__id_cliente = id

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @razon_social.setter
    def razon_social(self, razon_social):
        self.__razon_social = razon_social

    @nit.setter
    def nit(self, nit):
        self.__nit = nit

    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion

    @ciudad.setter
    def ciudad(self, ciudad):
        self.__ciudad = ciudad

    @email.setter
    def email(self, email):
        self.__email = email