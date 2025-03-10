import tkinter as tk
from sumahasta0 import SumaHastaCero

class SumaHastaCeroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Suma hasta 0")

        tk.Label(root, text="Ingrese un número (0 para detenerse):").pack()
        self.num_entry = tk.Entry(root)
        self.num_entry.pack()

        self.result_label = tk.Label(root, text="Suma: 0")
        self.result_label.pack()

        self.suma = SumaHastaCero()
        tk.Button(root, text="Agregar", command=self.agregar_numero).pack()

    def agregar_numero(self):
        numero = int(self.num_entry.get())
        suma_total = self.suma.agregar_numero(numero)
        self.result_label.config(text=f"Suma: {suma_total}")

        if numero == 0:
            self.num_entry.config(state="disabled")
