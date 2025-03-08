import tkinter as tk
from suma100 import SumaHasta100

class SumaHasta100App:
    def __init__(self, root):
        self.root = root
        self.root.title("Suma hasta 100")

        tk.Label(root, text="Ingrese un número:").pack()
        self.num_entry = tk.Entry(root)
        self.num_entry.pack()

        self.result_label = tk.Label(root, text="Suma: 0")
        self.result_label.pack()

        self.suma = SumaHasta100()
        tk.Button(root, text="Agregar", command=self.agregar_numero).pack()

    def agregar_numero(self):
        numero = int(self.num_entry.get())
        suma_total = self.suma.agregar_numero(numero)
        self.result_label.config(text=f"Suma: {suma_total}")

        if suma_total > 100:
            self.num_entry.config(state="disabled")
