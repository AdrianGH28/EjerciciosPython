import tkinter as tk
from suman import SumaN

class SumaNApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Suma de los primeros N números")

        tk.Label(root, text="Ingrese un número:").pack()
        self.n_entry = tk.Entry(root)
        self.n_entry.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        tk.Button(root, text="Calcular", command=self.calcular_suma).pack()

    def calcular_suma(self):
        n = int(self.n_entry.get())
        suma_n = SumaN(n)
        self.result_label.config(text=f"Suma total: {suma_n.calcular_suma()}")
