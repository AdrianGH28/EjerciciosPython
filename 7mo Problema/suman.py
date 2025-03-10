class SumaN:
    def __init__(self, n):
        self.n = n

    def calcular_suma(self):
        return sum(range(1, self.n + 1))