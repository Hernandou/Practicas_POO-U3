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
            obj = Carrera(carrera[0],carrera[1],carrera[2],carrera[3],carrera[4],carrera[-1])
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
    
    def getNombreCarrera(self,nomb):
        
        i = 0
        band = True
        
        while(i < len(self.__carreras) and band):
            if(self.__carreras[i].getNombre() == nomb):
                band = False
            i += 1
                
        if(band):
            print('>> No se encontro la Carrera especificada')            
            
    def getCodigoCarrera(self,nomb):
        i = 0
        band = True
        
        while(i<len(self.__carreras) and band):
            if(self.__carreras[i].getNombre() == nomb):
                cod = self.__carreras[i].getCodigo()
                band = True
            i+=1
            
        return(cod)        
        

            
    def __str__(self):
        return('\n>> Codigo: {}\n>>Nombre: {}\n>> Direccion: {}\n>> Localidad: {}\n>> Telefono: {}'.format(self.__codigo,self.__nombre,self.__direccion,self.__localidad,self.__telefono))