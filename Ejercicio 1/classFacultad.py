from classCarrera import Carrera
class Facultad:
    
    __codigo = 0
    __nombre = ''
    __direccion = ''
    __localidad = ''
    __telefono = ''
    __carreras = []
    
    def __init__(self,codigo,nombre,direccion,localidad,telefono,carreras):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono
        self.__carreras = []
        
        for carrera in carreras:
            obj = Carrera(carrera[0],carrera[1],carrera[2],carrera[3],carrera[4],carrera[5])
            self.__carreras.append(obj)

        
    def getCodigo(self):
        return(self.__codigo)
    
    def getNombre(self):
        return(self.__nombre)
    
    def getCarreras(self):
    
        for i in range(len(self.__carreras)):
        
            print('>> Carrera {}    -   Duracion: {}'.format(self.__carreras[i].getNombre(),self.__carreras[i].getDuracion()))        
        
    def mostrarCarreras(self):
        for obj in self.__carreras:
            print(obj)
    def __str__(self):
        return('\n>> Codigo: {}\n>>Nombre: {}\n>> Direccion: {}\n>> Localidad: {}\n>> Telefono: {}'.format(self.__codigo,self.__nombre,self.__direccion,self.__localidad,self.__telefono))