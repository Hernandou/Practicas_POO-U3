from ClassEquipos import Equipos
import numpy as np
import csv

class ListEquipos:
    
    def __init__(self):
        self.__list = np.empty(0,dtype = Equipos)
        file = open('/Users/hernan/Desktop/UNSJ/Segundo Año/P O O/Practicas POO/U3/Ejericio 3/Equipos.csv')
        reader = csv.reader(file,delimiter = ',')
        i = 0
        
        for fila in reader:
            if(len(fila) == 1):
                num = int(fila[0])
                self.__list.resize(num)
            else:   
                obj = Equipos(fila[0],fila[1])
                self.__list[i] = obj
                i += 1
                
    def MostrarEquipos(self):
        
        for i in range(len(self.__list)):
            print('\n')
            print(self.__list[i])
            
    def BuscEquip(self,nomb):
        i = 0
        band = False
        equip = None
        while(i < len(self.__list) and band == False):
            
            if(self.__list[i].getNombre() == nomb):
                band = True
                equip = self.__list[i]
                
            i += 1
        return(equip)    
    