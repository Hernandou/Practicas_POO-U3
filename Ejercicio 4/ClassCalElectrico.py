from ClassCalefactor import Calefactor


class CalefactorElectrico(Calefactor):
    
    __potencia = 0
    __consumo = 0
    def __init__(self,marca,modelo,watts):
        super().__init__(marca,modelo)
        self.__potencia = watts
        
    def getConsumo(self):
        return(self.__consumo)
        
    def CalcularConsumo(self,costW,cantH):
        self.__consumo = costW * cantH * self.__potencia
    
    def __lt__(self,other):
        val = False
        
        if(self.__consumo < other.__consumo):
            val = True
    
        return(val)
        

    def __str__(self):
        return('>>{}\n> Consumo: {}\n > Potencia: {}'.format(super().__str__,self.__consumo,self.__potencia))
    
        
        
        