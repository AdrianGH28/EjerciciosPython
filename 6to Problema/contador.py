class Contador:
    def __init__(self):
        self.contador = 0
    def incrementar(self):
        self.contador += 1
    def obtener_contador(self):
        return self.contador