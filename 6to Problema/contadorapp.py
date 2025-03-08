import tkinter as tk
from contador import Contador

class ContadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador de Entradas")
        self.contador = Contador()
        
        tk.Label(root, text="Ingrese un número:").pack()
        self.numero_entry = tk.Entry(root)
        self.numero_entry.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        tk.Button(root, text="Contar", command=self.contar_entrada).pack()

    def contar_entrada(self):
        _ = self.numero_entry.get()
        self.contador.incrementar()
        self.result_label.config(text=f"Entradas registradas: {self.contador.obtener_contador()}")
