class Carrera:
    
    __fac = 0
    __codigo = 0
    __nombre = ''
    __fechaInic = ''
    __duracion = 0
    __titulo = ''
    
    def __init__(self,fac,codigo,nombre,fechaInicio,duracion,titulo):
        self.__fac = fac
        self.__codigo = codigo
        self.__nombre = nombre
        self.__fechaInic = fechaInicio
        self.__duracion = duracion
        self.__titulo = titulo
        
    def getNombre(self):
        return(self.__nombre)
    
    def getDuracion(self):
        return(self.__duracion)
    
    
    def __str__(self):
        return('\nCodigo: {}\nNombre: {}'.format(self.__codigo,self.__nombre))