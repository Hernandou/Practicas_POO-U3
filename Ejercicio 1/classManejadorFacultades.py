from classFacultad import Facultad
import csv


class ListFacultades:

    __list = []
    facultad = []

    def __init__(self):

        self.__list = []
        band = True
        lista = []

        file = open(
            '/Users/hernan/Desktop/UNSJ/Segundo Año/P O O/Practicas POO/U3/Ejercicio 1/facultades.csv')
        reader = csv.reader(file, delimiter=',')
        bandera = True
        lista = []

        for fila in reader:
            if('Facultad' in fila[1]):
                obj = Facultad(int(fila[0]), fila[1],fila[2], fila[3], fila[4], lista)
                self.__list.append(obj)
                band = False
                
            else:
                if(band == False):
                    if('Licenciatura' in fila[2]):
                        lista.append(fila)

    def MostrarDatos(self, codFac):

        for i in range(len(self.__list)):
            print(self.__list[i])
            print(self.__list[i].mostrarCarreras())
