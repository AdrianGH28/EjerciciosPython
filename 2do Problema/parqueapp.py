import tkinter as tk
from parque import Parque

class ParqueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Precio del Juego")

        tk.Label(root, text="Edad:").pack()
        self.edad_entry = tk.Entry(root)
        self.edad_entry.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        tk.Button(root, text="Calcular", command=self.calcular_precio).pack()

    def calcular_precio(self):
        edad = int(self.edad_entry.get())
        parque = Parque(edad)
        self.result_label.config(text=f"Precio a pagar: {parque.calcular_precio():.2f}")
