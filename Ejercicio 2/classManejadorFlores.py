from classFlores import Flores
import numpy as np
import csv
class ListFlores:
    
    __cantidad = 0

    def __init__(self):
        
        self.__list = np.empty(0,dtype=Flores)
        file = open('/Users/hernan/Desktop/UNSJ/Segundo Año/P O O/Practicas POO/U3/Ejercicio 2/flores.csv')
        reader = csv.reader(file,delimiter= ';')
        i = 0
        for fila in reader:
            obj = Flores(int(fila[0]),fila[1],fila[2],fila[3])
            self.__list = np.append(self.__list,obj)
            i += i
            
    def mostrarCatalogo(self):
        
        for obj in self.__list:
            print(obj)
            
    def getLong(self):
        return(len(self.__list))
    
    def getcantidad(self):
        return(self.__cantidad)
            
    def BuscarFlor(self, cod):
        flr = None
        band = True
        i = 0
        
        while(i < len(self.__list) and band == True):
            
            if(cod == self.__list[i].getCodigo()):
                band = False
                flr = self.__list[i]
                self.__list[i].setVent()

            i += 1
        return(flr)
    
    

            
            
            
        
        
        
        
        
        

    
    