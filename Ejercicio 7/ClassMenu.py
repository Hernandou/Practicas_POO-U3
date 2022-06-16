from ClassDocente import Docente
from ClassInvestigador import Investigador
from ClassDocenteInvestigador import DocenteInvestigador
from ClassPersonalApoyo import PersonaldeApoyo
from ClassPersonal import Personal
from ObjectEnconder import ObjectEncoder


class Menu:

    __switch = None

    def __init__(self):
        self.__switch = {
            '1': self.opc1,
            '2': self.opc2,
            '3': self.opc3,
            '4': self.opc4,
            '5': self.opc5,
            '6': self.opc6,
            '7': self.opc7,
            '8': self.opc8
        }

    def getop(self, op, lista):
        func = self.__switch.get(op, lambda: print('>> Opcion Invalida'))
        func(lista)


    def crearelemento(self):
        op = input('>> -Ingrese un miembro del Personal\n1_ Docente\n2_ Investigador\n3_Docente Investigador\n4_ Personal de Apoyo\n')
        cuil = input('>> -Ingrese cuil\n')
        nombre = input('>> -Ingrese nombre\n')
        apellido = input('>> -Ingrese apellido\n')
        sueldo = float(input('>> -Ingrese sueldo basico\n'))
        antiguedad = int(input('>> -Ingrese antiguedad\n'))
        bandera = True
        
        while(bandera):
            if (op == '1'):
                carrera = input('>> -Ingrese carrera\n')
                catedra = input('>> -Ingrese catedra\n')
                cargo = input('>> -Ingrese cargo\n')
                area = tipo = ''
                
                elemento = Docente.Docente(cuil, apellido, nombre, sueldo, antiguedad, area, tipo, carrera, cargo, catedra)
                bandera = False
                
            elif (op == '2'):
                
                area = input('>> -Ingrese area\n')
                tipo = input('>> -Ingrese tipo de investigacion\n')
                carrera = cargo = catedra = ''
                elemento = Investigador.Investigador(cuil, apellido, nombre, sueldo, antiguedad, area, tipo, carrera, cargo, catedra)
                bandera = False
                
            elif (op == '3'):
                
                area = input('>> -Ingrese area\n')
                tipo = input('>> -Ingrese tipo de investigacion\n')
                carrera = input('>> -Ingrese carrera\n')
                catedra = input('>> -Ingrese catedra\n')
                cargo = input('>> -Ingrese cargo\n')
                Categoria = input('>> -Ingrese categoria\n')
                importe = float(input('>> -Ingrese importe\n'))
                elemento = DocenteInvestigador.DocenteInvestigador(cuil, apellido, nombre, sueldo, antiguedad, Categoria, importe, area, tipo, carrera, cargo, catedra)
                bandera = False
                
            elif (op == '4'):
                
                categoria = int(input('>> -Ingrese una categoría\n'))
                elemento = PersonaldeApoyo.PersonaldeApoyo(cuil, apellido, nombre, sueldo, antiguedad, categoria)
                bandera = False
                
            else:
                print('opc no válida')
                op = input(
                    '>> -Ingrese un miembro del Personal\n1_ Docente\n2_ Investigador\n3_Docente Investigador\n4_ Personal de Apoyo\n')
        return(elemento)

    def opc1(self, lista):
        elemento = self.crearelemento()
        bandera = True
        
        while (bandera):
            try:
                posicion = int(input('>> -Ingrese una posicion \n'))
                lista.InsertarElemento(elemento, posicion-1)
                bandera = not bandera
            except IndexError:
                
                print('Error: Indice inválido')

    def opc2(self, lista):
        elemento = self.crearelemento()
        lista.AgregarElemento(elemento)

    def opc3(self, lista):
        bandera = True
        
        while (bandera):
            try:
                posicion = int(input('>> -Ingrese una posicion \n'))
                print(lista.MostrarElemento(posicion-1))
                bandera = not bandera
            except IndexError:
                
                print('Error: Indice inválido')

    def opc4(self, lista):
        listado = []
        i = 0
        
        for agente in lista:
            if type(agente) == DocenteInvestigador:
                listado.append(agente)
        listado.sort()
        
        for agente in listado:
            print(agente)

    def opc5(self, lista):
        area = input('>> -Ingrese un area de investigacion\n')
        continv = 0
        contdocinv = 0
        
        for agente in lista:
            if type(agente) == Investigador and agente.getarea() == area:
                continv += 1
            if type(agente) == DocenteInvestigador and agente.getarea() == area:
                contdocinv += 1
        print('La cantidad de investigadores en el area es de {}\nLa cantidad de docentes investigadores en el area es de {}\n'.format(
            continv, contdocinv))

    def opc6(self, lista):
        listado = []
        
        for agente in lista:
            listado.append(agente)
        listado.sort()
        for elemento in listado:
            print(elemento)

    def opc7(self, lista):
        
        cat = input('>> -Ingrese una categoria (I,II,III,IV)\n')
        total = 0
        for agente in lista:
            if type(agente) == DocenteInvestigador and agente.getcategoria() == cat:
                print(agente)
                total += agente.getimporte()
        print('El importe total es {}'.format(total))

    def opc8(self, lista):
        jsonF = ObjectEncoder()
        d = lista.toJSON()
        jsonF.guardarJSONArchivo(d, 'Personal.json')

    def salir(self):
        print('Usted ha salido del programa')
