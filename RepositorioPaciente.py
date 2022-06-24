from ManejadorPaciente import ManejadorPaciente
from ObjectEncoder import ObjectEncoder
from Paciente import Paciente
class RespositorioPaciente(object):
    __conn=None
    __manejador=None
    def __init__(self, conn):
        self.__conn = conn
        diccionario=self.__conn.leerJSONArchivo()
        generarManejador=False
        if diccionario!=-1:
            resultado=self.__conn.decodificarDiccionario(diccionario)
            if isinstance(resultado,ManejadorPaciente):
                self.__manejador=resultado
            else:
                generarManejador=True
        else:
            generarManejador=True
        if generarManejador:
            self.__manejador=ManejadorPaciente()
    def obtenerListaPacientes(self):
        return self.__manejador.getListaPacientes()
    def agregarPaciente(self, paciente):
        self.__manejador.agregarPaciente(paciente)
        return paciente
    def modificarPaciente(self, paciente):
        self.__manejador.updatePaciente(paciente)
        return paciente
    def borrarPaciente(self, paciente):
        self.__manejador.deletePaciente(paciente)
    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())