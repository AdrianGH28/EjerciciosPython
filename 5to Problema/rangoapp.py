import tkinter as tk
from rango import Rango

class RangoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Verificar Rango")
        
        tk.Label(root, text="Ingrese un número:").pack()
        self.numero_entry = tk.Entry(root)
        self.numero_entry.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        tk.Button(root, text="Verificar", command=self.verificar_rango).pack()

    def verificar_rango(self):
        numero = int(self.numero_entry.get())
        rango = Rango(numero)
        if rango.es_valido():
            self.result_label.config(text="Número dentro del rango")
        else:
            self.result_label.config(text="Número fuera del rango")
