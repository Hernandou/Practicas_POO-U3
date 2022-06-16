from classRamos import Ramos
from classManejadorFlores import ListFlores


class ListRamo:

    __list = []

    def __init__(self):
        self.__list = []

    def AgregarRamos(self, listRam):
        self.__list.append(listRam)

    def MostrarRamos(self):

        for obj in self.__list:
            print(obj)

    def FloresMasVendidas(self, ListFlores):

        lista = []
        for i in range(ListFlores.getLong()):
            listaaux = []
            aux = 0
            for ramos in self.__lista:
                aux += ramos.buscarflores(ListFlores.getflor(i).getnumero())
            listaaux.append(aux)
            listaaux.append('{} {}'.format(ListFlores.getflor(
                i).getnombre(), ListFlores.getflor(i).getcolor()))
            lista.append(listaaux)
        lista.sort(reverse=True)
        print('> -Los nombres de las flores mas vendidas son:')
        i = 0

    def MostrarFloresPorTamanio(self, size, ListFlores):
        
        Lista = []
        for i in range(ListFlores.getcantidad()):
            j=0
            bandera=False
            while (j<len(self.__lista) and bandera==False):
                if (self.__lista[j].gettamano()==size and self.__lista[j].encontrarflor(ListFlores.getflor(i).getnumero())):
                    bandera = not bandera
                j+=1
            if bandera:
                Lista.append(ListFlores.getflor(i).getnombre()+' '+ListFlores.getflor(i).getcolor())
        print('> -Las flores en los ramos de tamaño {}:'.format(size))
        for flor in Lista:
            print(flor)
     
