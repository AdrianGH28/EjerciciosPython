class Parque:
    PRECIO = 50

    def __init__(self, edad):
        self.edad = edad

    def calcular_precio(self):
        return self.PRECIO * 0.75 if self.edad < 10 else self.PRECIO
