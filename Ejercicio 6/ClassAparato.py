class Aparato(object):
    
    __marca = ''
    __modelo = ''
    __color = ''
    __paisFab = ''
    __precioBase = 0
    
    def __init__(self,marca,modelo,color,paisFab,precioBase):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__paisFab = paisFab
        self.__precioBase = precioBase
    
    def getMarca(self):
        return(self.__marca)
    
    def getmodelo(self):
        return (self.__modelo)
    
    def getpais(self):
        return (self.__pais)
    
    def getcolor(self):
        return (self.__color)
    
    def getprecio(self):
        return (self.__preciobase)
    
    def setimporte(self, importe):
        self.__importe=importe
        
    def getimporte(self):
        return(self.__importe)
    
    def __str__(self):
        return('>> Marca: {}\n>>Modelo: {}\n>> Color: {}\n>>Pais Fabricacion: {}\n>> Precio Base:{}\n'.format(self.__marca,self.__modelo,self.__color,self.__paisFab,self.__precioBase))