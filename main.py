from ControladorPacientes import ControladorPacientes
from ObjectEncoder import ObjectEncoder
from PacientesView import PacientesView
from RepositorioPaciente import RespositorioPaciente

if __name__ == "__main__":
    conn=ObjectEncoder('pacientes.json')
    repo=RespositorioPaciente(conn)
    vista=PacientesView()
    ctrl=ControladorPacientes(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()