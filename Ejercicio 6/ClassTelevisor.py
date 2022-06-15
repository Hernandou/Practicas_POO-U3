from ClassAparato import Aparato

class Televisor(Aparato):    
    __TipPantalla = ''
    __pulgadas = 0
    __TipDefinicion = ''
    __conexion = None
    
    def __init__(self,marca,modelo,color,paisFab,precioBase,TipPantalla,pulgadas,tipDefinicion,ConexInternet):
        super().__init__(marca,modelo,color,paisFab,precioBase)
        self.__TipPantalla = TipPantalla
        self.__pulgadas = pulgadas
        self.__TipDefinicion = tipDefinicion
        self.__conexion = ConexInternet
        
        
    def __str__(self):
        return('{}\n> Tipo Pantalla: {}\n> Pulgadas: {}\n> Tipo Definicion: {}\n > Conexion: {}'.format(super().__str__,self.__TipPantalla,self.__pulgadas,self.__TipDefinicion,self.__conexion))
