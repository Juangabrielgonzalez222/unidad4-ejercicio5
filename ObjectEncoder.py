import json
from msilib.schema import File
from pathlib import Path
from ManejadorPaciente import ManejadorPaciente
from Paciente import Paciente
class ObjectEncoder(object):
    __pathArchivo=None
    def __init__(self, pathArchivo):
        self.__pathArchivo=pathArchivo
    def decodificarDiccionario(self, d):
        resultado=None
        if '__class__' not in d:
            resultado=-1
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='ManejadorPaciente':
                pacientes=d['pacientes']
                manejador=class_()
                for i in range(len(pacientes)):
                    dPaciente=pacientes[i]
                    class_name=dPaciente.pop('__class__')
                    class_=eval(class_name)
                    atributos=dPaciente['__atributos__']
                    unPaciente=class_(**atributos)
                    manejador.agregarPaciente(unPaciente)
            resultado=manejador
        return resultado
    def guardarJSONArchivo(self, diccionario):
        with Path(self.__pathArchivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()
    def leerJSONArchivo(self):
        diccionario=None
        try:
            with Path(self.__pathArchivo).open(encoding="UTF-8") as fuente:
                diccionario=json.load(fuente)
                fuente.close()
        except FileNotFoundError:
            diccionario=-1
        return diccionario