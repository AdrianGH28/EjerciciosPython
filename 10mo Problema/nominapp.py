import tkinter as tk
from nomina import Nomina

class NominaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculo de Nómina")

        tk.Label(root, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.pack()

        tk.Label(root, text="Horas Normales:").pack()
        self.horas_normales_entry = tk.Entry(root)
        self.horas_normales_entry.pack()

        tk.Label(root, text="Horas Extras:").pack()
        self.horas_extras_entry = tk.Entry(root)
        self.horas_extras_entry.pack()

        tk.Label(root, text="Cantidad de Hijos:").pack()
        self.hijos_entry = tk.Entry(root)
        self.hijos_entry.pack()

        tk.Label(root, text="Pago por Hora:").pack()
        self.pago_hora_entry = tk.Entry(root)
        self.pago_hora_entry.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        tk.Button(root, text="Calcular", command=self.calcular_nomina).pack()

    def calcular_nomina(self):
        nombre = self.nombre_entry.get()
        horas_normales = int(self.horas_normales_entry.get())
        horas_extras = int(self.horas_extras_entry.get())
        hijos = int(self.hijos_entry.get())
        pago_hora = float(self.pago_hora_entry.get())

        nomina = Nomina(nombre, horas_normales, horas_extras, hijos, pago_hora)
        total_pago = nomina.calcular_pago_total()

        self.result_label.config(
            text=f"Pago Total para {nombre}: {total_pago:.2f}"
        )
