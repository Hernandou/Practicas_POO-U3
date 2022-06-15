from ClassAparato import Aparato

class Heladera(Aparato):
    
    __CapLitr = 0
    __Freezer = None
    __cicl = None
    
    def __init__(self,marca,modelo,color,paisFab,precioBase,CapLit,Freezer,cicl):
        super.__init__(marca,modelo,color,paisFab,precioBase)
        
        self.__CapLitr = CapLit
        self.__Freezer = Freezer
        self.__cicl = cicl



    def __str__(self):
        return('{} \n> Capacidad Litros: {}\n> Freezer: {}\n> Ciclica: {}'.format(super().__str__,self.__CapLitr,self.__Freezer,self.__cicl))