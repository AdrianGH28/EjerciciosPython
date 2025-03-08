import tkinter as tk
from validacion import Validacion

class ValidacionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Validar Número")
        self.validacion = Validacion()

        tk.Label(root, text="Ingrese un número:").pack()
        self.numero_entry = tk.Entry(root)
        self.numero_entry.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        tk.Button(root, text="Validar", command=self.validar).pack()

    def validar(self):
        try:
            numero = int(self.numero_entry.get())
            while not self.validacion.validar_numero(numero):
                self.result_label.config(text="Inválido, ingrese otro número")
                return
            self.result_label.config(text=f"Número válido: {numero}")
        except ValueError:
            self.result_label.config(text="Ingrese un número válido")