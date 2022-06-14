
class Equipos:
    __nombre = ''
    __ciudad = ''
    def __init__(self,nombre,ciudad):
        
        self.__nombre = nombre
        self.__ciudad = ciudad
        
    def getNombre(self):
        return(self.__nombre)
        
    def __str__(self):
        return('>> Equipo: {}      - Ciudad: {}'.format(self.__nombre,self.__ciudad))
    