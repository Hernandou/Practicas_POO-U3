class Menu:
    __switch = None

    def __init__(self):

        self.__switch = {

            '1': self.opc1,
            '2': self.opc2,
            '3': self.opc3,
        }

    def GestOpc(self, opc, obj, Lram, ram):

        func = self.__switch.get(opc, lambda: print('Opcion Invalida'))
        func(obj, Lram, ram)

    def opc1(self, obj, Lram, ram):
        i = 0
        num = int(input('>> -Ingrese la cantidad de flores (Ramo): '))

        while(i < num):

            cod = int(input('>> -Ingrese el codigo de flor a agregar: '))
            flr = obj.BuscarFlor(cod)

            if(flr == None):
                print('La flor NO se encontro')
            else:
                ram.AgregarFlores(flr)
                i += 1

        Lram.AgregarRamos(ram.cargarRamo())

    def opc2(self, obj, Lram, ram):
        Lram.FloresMasVendidas(obj)

    def opc3(self, obj, Lram, ram):
        size = input("Ingrese un tamaño de ramo (pequeño, mediano, grande)\n")
        Lram.MostrarFloresPorTamanio(size,obj)
