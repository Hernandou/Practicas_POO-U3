
class Calefactor(object):
    
    __marca = ''
    __modelo = ''
    def __init__(self,marca,modelo):
        self.__marca = marca
        self.__modelo = modelo
        
    def getNombre(self):
        return(self.__marca)
        
        
    def __str__(self):
        return('> Marca: {}         > Modelo: {}\n'.format(self.__marca,self.__modelo))
        
        
