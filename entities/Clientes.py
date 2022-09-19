class Clientes:

    def __init__(self, nombre, razon_social, nit, direccion, ciudad, email):
        self.nombre = nombre
        self.razon_social = razon_social
        self.nit = nit
        self.direccion = direccion
        self.ciudad = ciudad
        self.email = email

    def __str__(self):
        return f"""
                nombre: {self.nombre}
                razon social: {self.razon_social}
                nit: {self.nit}
                direccion: {self.direccion}
                ciudad: {self.ciudad}
                email: {self.email}
            """
