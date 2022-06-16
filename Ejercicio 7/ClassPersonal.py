class Personal:
    __cuil = ''
    __apellido = ''
    __nombre = ''
    __sueldobasico = ''
    __antiguedad = ''

    def __init__(self, cuil, apellido, nombre, sueldo, antiguedad='', area='', tipo='', carrera='', cargo='', catedra=''):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldobasico = sueldo
        self.__antiguedad = antiguedad

    def getsueldobasico(self):
        return self.__sueldobasico

    def getantiguedad(self):
        return self.__antiguedad

    def getnombre(self):
        return self.__nombre

    def getcuil(self):
        return self.__cuil

    def getapellido(self):
        return self.__apellido

    def calcularsueldo(self):
        return self.getsueldobasico()*(1+self.getantiguedad()/100)

    def __lt__(self, other):
        val = None
        if (isinstance(self, Personal) and isinstance(other, Personal)):
            
            valor = (self.getapellido() < other.getapellido())
        else:
            print("Error: No son del mismo tipo")
        return val

    def __str__(self):
        return ("{}, {}    -Sueldo: {}\n    -Tipo de Investigacion:".format(self.getapellido(), self.getnombre(), self.calcularsueldo()))

    def toJSON(self):
        pass
