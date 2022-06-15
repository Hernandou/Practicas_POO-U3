from ClassAparato import Aparato

class Lavarropas(Aparato):
    
    __capacidadLavado = 0
    __velocidadCentrif = 0
    __cantidadProgrmas = 0
    __TipCarga = ''
    
    def __init__(self,marca,modelo,color,paisFab,precioBase,capacidadLavado,velocidadCentrif,cantidadProgramas,TipCarga):
        super().__init__(marca,modelo,color,paisFab,precioBase)
        
        self.__capacidadLavado = capacidadLavado
        self.__velocidadCentrif = velocidadCentrif
        self.__cantidadProgrmas = cantidadProgramas
        self.__TipCarga = TipCarga
        
    def __str__(self):
        return('{}\n> Capacidad: {}\n> Velocidad Centrif: {}\n> Cantidad Programas: {}\n> Tipo Carga: {]'.format(self.__capacidadLavado,self.__velocidadCentrif,self.__cantidadProgrmas,self.__TipCarga))
        