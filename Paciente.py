import re
class Paciente(object):
    __telefonoRegex = re.compile(r"\([0-9]{3}\)[0-9]{7}")
    __apellido=None
    __nombre=None
    __telefono=None
    __altura=None
    __peso=None
    def __init__(self, apellido,nombre,telefono,altura,peso):
        self.__apellido=self.requerido(apellido, 'Apellido es un valor requerido')
        self.__nombre = self.requerido(nombre, 'Nombre es un valor requerido')
        self.__telefono = self.formatoValido(telefono, self.__telefonoRegex, 'Teléfono no tiene formato correcto')
        self.__altura = self.tipoValido(altura, 'Altura no tiene un valor numérico correcto.')
        self.__peso = self.tipoValido(peso, 'Peso no tiene un valor numérico correcto.')
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getTelefono(self):
        return self.__telefono
    def getAltura(self):
        return self.__altura
    def getPeso(self):
        return self.__peso
    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor
    def formatoValido(self, valor, regex, mensaje):
        if not valor or not regex.match(valor):
            raise ValueError(mensaje)
        return valor
    def tipoValido(self,valor,mensaje):
        try:
            valor=int(valor)
        except ValueError:
            raise ValueError(mensaje)
        return valor
    def calcularImc(self):
        resultado=0
        metros=self.__altura/100
        resultado=round(self.__peso/(metros*metros),2)
        return resultado
    def tipoDeImc(self):
        tipo=''
        imc=self.calcularImc()
        if imc <18.5:
            tipo='Peso inferior al normal'
        elif imc >=18.5 and imc< 25:
            tipo='Peso normal'
        elif imc>= 25.0 and imc< 30:
            tipo='Peso superior al normal'
        else:
            tipo='Obesidad'    
        return tipo
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
            apellido=self.__apellido,
            nombre=self.__nombre,
            telefono=self.__telefono,
            altura=self.__altura,
            peso=self.__peso
            ))
        return d