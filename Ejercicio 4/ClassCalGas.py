from ClassCalefactor import Calefactor

class CalefactorGas(Calefactor):
    
    __matricula = ''
    __calorias = 0
    __consumo = 0
    
    def __init__(self,marca,modelo,matricula,calorias,consumo = 0):
        
        super().__init__(marca,modelo)
        self.__matricula = matricula
        self.__calorias = calorias
        self.__consumo = consumo
        
    def getConsumo(self):
        return(self.__consumo)
    
    def __lt__(self,other):
        val = False
        
        if(self.__consumo < other.__consumo):
            val = True
    
        return(val)
    
    def CalcularConsumoGas(self,costo,cantM3):
        
        cost = (self.__calorias/1000)*costo *cantM3
        self.__consumo = cost
        
        
    def __str__(self):
        return('\n{}\n > Calorias: {}\n> Consumo: {}'.format(super().__str__,self.__calorias,self.__consumo))