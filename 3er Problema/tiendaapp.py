import tkinter as tk
from tienda import Tienda

class TiendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Descuento en Tienda")

        tk.Label(root, text="Mes:").pack()
        self.mes_entry = tk.Entry(root)
        self.mes_entry.pack()

        tk.Label(root, text="Importe:").pack()
        self.importe_entry = tk.Entry(root)
        self.importe_entry.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        tk.Button(root, text="Calcular", command=self.calcular_total).pack()

    def calcular_total(self):
        mes = self.mes_entry.get()
        importe = float(self.importe_entry.get())
        tienda = Tienda(mes, importe)
        self.result_label.config(text=f"Total a pagar: {tienda.calcular_total():.2f}")
