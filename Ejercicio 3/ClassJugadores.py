

class Jugadores:
    
    def __init__(self,nombre,dni,ciudad,pais,fechaNac):
        
        self.__nombre = nombre
        self.__dni = dni
        self.__ciudad = ciudad
        self.__pais = pais
        self.__fechaNac = fechaNac
        
    def getDNI(self):
        return(self.__dni)
    
    def getNombre(self):
        return(self.__nombre)

        
        
    def __str__(self):
        return('- Nombre: {}\n-DNI: {}\n-Ciudad: {}\n-Pais: {}\n-Fecha Nacimiento: {}'.format(self.__nombre,self.__dni,self.__ciudad,self.__pais,self.__fechaNac))