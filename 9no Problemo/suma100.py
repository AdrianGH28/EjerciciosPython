class SumaHasta100:
    def __init__(self):
        self.total = 0

    def agregar_numero(self, numero):
        if self.total <= 100:
            self.total += numero
        return self.total
