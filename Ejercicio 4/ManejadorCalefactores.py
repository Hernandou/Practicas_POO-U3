from ClassCalefactor import Calefactor
from ClassCalElectrico import CalefactorElectrico
from ClassCalGas import CalefactorGas
import numpy as np
import csv


class ListCalefactor:

    __dimension = 0

    def __init__(self, dimension):
        self.__dimension = dimension
        self.__list = np.empty(self.__dimension, dtype=Calefactor)

        file = open(
            '/Users/hernan/Desktop/UNSJ/Segundo Año/P O O/Practicas POO/U3/Ejercicio 4/CalefactorElectrico.csv')
        reader = csv.reader(file, delimiter=',')
        i = 0
        for fila in reader:
            obj = CalefactorElectrico(fila[0], fila[1], int(fila[2]))
            self.__list = np.append(self.__list, obj)

        file.close()

        file = open(
            '/Users/hernan/Desktop/UNSJ/Segundo Año/P O O/Practicas POO/U3/Ejercicio 4/CalefactorGas.csv')
        reader = csv.reader(file, delimiter=',')

        for fila in reader:
            obj = CalefactorGas(fila[0], fila[1], fila[2], int(fila[3]))
            self.__list = np.append(self.__list, obj)

        file.close()

    def mostrar(self):

        for i in range(len(self.__list)):
            print(type(self.__list[i]))

    def CalcularConsumoGas(self, costo, cantM3):

        for i in range(len(self.__list)):
            if(isinstance(self.__list[i], CalefactorGas)):

                self.__list[i].CalcularConsumoGas(costo, cantM3)
                print('Consumo del calefactor {}  es: {}'.format(
                    self.__list[i].getNombre(), self.__list[i].getConsumo()))

    def CalcularConsumoElectrico(self, costW, cantH):

        for i in range(len(self.__list)):

            if(isinstance(self.__list[i], CalefactorElectrico)):

                self.__list[i].CalcularConsumo(costW, cantH)
                print('Calefactor Electrico {} - tiene un consumo de: {}'.format(
                    self.__list[i].getNombre(), self.__list[i].getConsumo()))

    def CalcularMenorElectrico(self):
        band = True
        for i in range(len(self.__list)):

            if(isinstance(self.__list[i], CalefactorElectrico)):

                if(band):
                    band = False
                    calef = self.__list[i]

                else:

                    if(self.__list[i] < calef):
                        calef = self.__list[i]
        return(calef)

    def CalcularMenorGas(self):
        band = True
        
        for i in range(len(self.__list)):
            if(isinstance(self.__list[i], CalefactorGas)):

                if(band):
                    band = False
                    calef = self.__list[i]

                else:
                        
                    if(self.__list[i] < calef):          
                        calef = self.__list[i]
                            
        return(calef)
                
                