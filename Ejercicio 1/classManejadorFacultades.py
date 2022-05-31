from classFacultad import Facultad
import csv


class ListFacultades:

    __list = []
    facultad = []

    def __init__(self):

        self.__list = []
        band = True
        lista = []

        file = open('/Users/hernan/Desktop/UNSJ/Segundo Año/P O O/Practicas POO/U3/Ejercicio 1/facultades.csv')
        reader = csv.reader(file, delimiter=',')

        for fila in reader:
            
            if(band):
                facultad = fila
                band = False
            else:
                if(fila[0] == facultad[0]):
                    lista.append(fila)
                else:
                    obj = Facultad(int(facultad[0]),facultad[1],facultad[2],facultad[3],facultad[4],lista)
                    self.__list.append(obj)
                    lista.clear()
                    facultad = fila
        obj = Facultad(int(facultad[0]),facultad[1],facultad[2],facultad[3],facultad[4],lista)
        self.__list.append(obj)
            
    def MostrarDatos(self, codFac):
        print('\n')
        band = True
        i = 0
        while(i < len(self.__list) and band):    
            if(codFac == self.__list[i].getCodigo()):
                print('Nombre Facultad: {}'.format(self.__list[i].getNombre()))
                print('\n')
                self.__list[i].getCarreras()
                band = False
                i += 1
    
    def MostrarCarrera(self,nomb):
        i = 0
        band = True
        while(i < len(self.__list) and band):
            if(self.__list[i].getNombreCarrera(nomb) == nomb):
                print('Codigo de la Carrera {} es: {}'.format(nomb,self.__list[i].getCodigoCarrera(nomb)))
                band = True
            i += 1
            
    def Mostrar(self):
        for obj in self.__list:
            print(obj)
            print(obj.mostrarCarreras())
            
            