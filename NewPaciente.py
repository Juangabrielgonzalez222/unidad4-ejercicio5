import tkinter as tk
from PacienteForm import PacienteForm
class NewPaciente(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.paciente = None
        self.title('Nuevo Paciente')
        self.form = PacienteForm(self)
        self.btn_add = tk.Button(self, text="Confirmar", command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)
    def confirmar(self):
        self.paciente = self.form.crearPacienteDesdeFormulario()
        if self.paciente:
            self.destroy()
    def show(self):
        self.grab_set()
        self.wait_window()
        return self.paciente