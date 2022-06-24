import tkinter as tk
from PacienteForm import PacienteForm
class VerImc(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.paciente = None
        self.title('IMC')
        self.config(padx=15,pady=10)
        self.label1=tk.Label(self,text='IMC')
        self.entry1=tk.Entry(self,width=25)
        self.label2=tk.Label(self,text='Composición Corporal')
        self.entry2=tk.Entry(self,width=25)
        self.btn_close = tk.Button(self, text="Volver", command=self.destroy)
        self.label1.grid(column=0,row=0)
        self.entry1.grid(pady=5,column=1,row=0,columnspan=2)
        self.label2.grid(column=0,row=1)
        self.entry2.grid(pady=8,column=1,row=1,columnspan=2)
        self.btn_close.grid(pady=15,columnspan=3)
    def mostrarImcPaciente(self,paciente):
        self.entry1.insert(0,str(paciente.calcularImc()))
        self.entry2.insert(0,paciente.tipoDeImc())