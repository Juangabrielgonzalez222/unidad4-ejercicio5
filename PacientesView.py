import tkinter as tk
from PacienteList import PacienteList
from UpdatePacienteForm import UpdatePacienteForm
class PacientesView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Pacientes")
        self.list = PacienteList(self, height=15)
        self.form = UpdatePacienteForm(self)
        self.btn_new = tk.Button(self, text="Agregar Paciente")
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)
    def setControlador(self, ctrl):
        #vincula la vista con el controlador
        self.btn_new.config(command=ctrl.crearPaciente)
        self.list.bind_doble_click(ctrl.seleccionarPaciente)
        self.form.bind_save(ctrl.modificarPaciente)
        self.form.bind_delete(ctrl.borrarPaciente)
        self.form.bind_imc(ctrl.mostrarImc)
    def agregarPaciente(self, paciente):
        self.list.insertar(paciente)
    def modificarPaciente(self, paciente, index):
        self.list.modificar(paciente, index)
    def borrarPaciente(self, index):
        self.form.limpiar()
        self.list.borrar(index)
    #obtiene los valores del formulario y crea un nuevo paciente
    def obtenerDetalles(self):
        return self.form.crearPacienteDesdeFormulario()
    #Ver estado de Paciente en formulario de pacientes
    def verPacienteEnForm(self, paciente):
        self.form.mostrarEstadoPacienteEnFormulario(paciente)