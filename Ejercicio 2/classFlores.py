
class Flores:
    
    __numero = 0
    __nombre = ''
    __size = 0
    __color = ''
    __descripc = ''
    __vent = 0
    
    def __init__(self,numero,nombre,color,descripc):
        
        self.__numero = numero
        self.__nombre = nombre
        self.__color = color
        self.__descripc = descripc
        self.__vent = 0
        
    def getCodigo(self):
        return(self.__numero)
    
    def setVent(self):
        self.__vent += 1
        
            
    
    def __str__(self):
        return('\n>> Numero Flor: {}\n>> Nombre: {}\n>> Color: {}\n>> Descripcion: {}'.format(self.__numero,self.__nombre,self.__color,self.__descripc))