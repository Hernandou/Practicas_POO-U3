class Nodo:
    __Aparato = None
    __siguiente = None
    
    def  __init__(self,Aparato):
        self.__Aparato = Aparato
        self.__siguiente = None
    
    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente
        
    def getSiguiente(self):
        return(self.__siguiente)
    
    def getInst(self):
        return(self.__Aparato)