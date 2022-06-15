import ObjectEncoder
from ClassNodo import Nodo
from ClassLavarropas import Lavarropas
from ClassHeladera import Heladera
from ClassTelevisor import Televisor
from ClassLista import Lista


class Menu:

    __Switch = None

    def __init__(self):
        self.__Switch = {

            '1': self.opc1,
            '2': self.opc2,
            '3': self.opc3,
            '4': self.opc4,
            '5': self.opc5,
            '6': self.opc6
        }

    def GestOpc(self, opc, lista):
        func = self.__Switch.get(opc, lambda: print('>> Opcion Invalida'))
        func(lista)

    def opc1(self, lista):
        band = True
        ans = str(input('''>> Ingrese aparato que desea crear
                        
                        A) Lavarropas       B) Televisor    C) Heladera
                        : '''))

        marc = input('  -Ingrese Marca: ')
        modelo = input(' -Ingrese Modelo: ')
        color = input(' -Ingrese Color: ')
        pais = input('  -Ingrese Pais: ')
        precio = int(input(' -Ingrese Precio: '))

        if(ans == 'A'):

            capCarga = int(input('  -Ingrese capacidad de carga: '))
            veloC = int(input(' -Ingrese Velocidad del Lavarropas: '))
            cantProg = int('    -Ingrese La cantidad de programas: ')
            tipCarga = str(input('  -Ingrese Tipo de carga: '))
            obj = Lavarropas(marc, modelo, color, pais, precio,capCarga, veloC, cantProg, tipCarga)
            pos =  input('-  Ingrese la POSICION que desea insertar el APARATO: ')
            lista.InsertarNodo(obj, pos)
            
        elif(ans == 'B'):
            tipPant = input('   -Ingrese tipo de pantalla: ')
            pulgadas = int(input('  -Ingrese cant de pulgadas: '))
            definicion = input('    -Ingrese tipo de definicion: ')
            conex = input('Ingrese si posee conexion a internet ''SI''/ ''NO'': ')
        
            if(conex == 'SI'):
                conex = True
            elif(conex == 'NO'):
                conex = False
            
            obj = Televisor(marc,modelo,color,pais,precio,tipPant,pulgadas,definicion,conex)
            pos =  input('-  Ingrese la POSICION que desea insertar el APARATO: ')
            lista.InsertarNodo(obj,pos)
        
        elif(ans == 'C'):
            capac = int(input(' -Ingrese Capacidad en LITROS: '))
            Freezer = input('   -Ingrese si tiene Freezer ''SI''/ ''NO'': ')
            
            if(Freezer == 'SI'):
                Freezer = True
            elif(Freezer == 'NO'):
                Freezer = False
            cicl = str(input('  -Ingrese si es Ciclica Ingrese ''SI''/ ''NO'''))
            
            if(cicl == 'SI'):
                cicl = True
            else:
                cicl = False
            obj = Heladera(marc,modelo,color,pais,precio,capac,Freezer,cicl)
            pos =  input('-  Ingrese la POSICION que desea insertar el APARATO: ')
            lista.InsertarNodo(obj,pos)

    def opc2(self, lista):
        band = True
        
        while(band):
            try:
                posicion = int(input(' -Ingrese posicion:'))
                lista.MostrarElemento(posicion - 1)
                band = False
                
            except IndexError:
                print(' ERROR: Indice ingresado supera la lista')

    def opc3(self, lista):
        cont=0
        for aparato in lista:
            if aparato.getMarca()=="philips":
                cont+=1
        print("-Cantidad de aparatos marca PHILIPS: {}".format(cont))

    def opc4(self, lista):
        
        for aparato in lista:
            if type(aparato)==Lavarropas and aparato.getcarga()=="superior":
                print(aparato)
                
    def opc5(self,lista):
        for aparato in lista:
            aparato.calcularimporte()
            print("-Aparato:{}    {}".format(str(type(aparato)), aparato))
    
    def opc6(self,lista):
        jsF=ObjectEncoder()
        dct=lista.toJSON()
        jsF.guardarJSONArchivo(dct,'/Users/hernan/Desktop/UNSJ/Segundo Año/P O O/Practicas POO/U3/Ejercicio 6/Aparatos.json')
        
