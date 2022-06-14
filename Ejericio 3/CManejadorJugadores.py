from ClassJugadores import Jugadores
import csv
class ListJugadores:
    
    __list = []
    
    def __init__(self):
        
        self.__list = []
        file = open('/Users/hernan/Desktop/UNSJ/Segundo Año/P O O/Practicas POO/U3/Ejericio 3/Jugadores.csv')
        reader = csv.reader(file, delimiter= ',')
        next(reader)
        for fila in reader:
            
            obj = Jugadores(fila[0],int(fila[1]),fila[2],fila[3],fila[4])
            self.__list.append(obj)
        
    def BuscJugador(self,dni):
        i = 0
        band = True
        jug = None
        while(i < len(self.__list) and band):
            if(self.__list[i].getDNI() == dni):
                
                band = False
                jug = self.__list[i]
                
            i += 1
            
        return(jug)