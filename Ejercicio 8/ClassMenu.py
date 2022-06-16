from ClassDocente import Docente
from ClassInvestigador import Investigador
from ClassDocenteInvestigador import DocenteInvestigador
from ClassPersonalApoyo import PersonaldeApoyo
from ClassPersonal import Personal
from ObjectEnconder import ObjectEncoder
from InterfaceTesorero import ITesorero
from InterfaceDirector import IDirector


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
        op = input(
            '>> -Ingrese un miembro del Personal\n1_ Docente\n2_ Investigador\n3_Docente Investigador\n4_ Personal de Apoyo\n')
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

                elemento = Docente.Docente(
                    cuil, apellido, nombre, sueldo, antiguedad, area, tipo, carrera, cargo, catedra)
                bandera = False

            elif (op == '2'):

                area = input('>> -Ingrese area\n')
                tipo = input('>> -Ingrese tipo de investigacion\n')
                carrera = cargo = catedra = ''
                elemento = Investigador.Investigador(
                    cuil, apellido, nombre, sueldo, antiguedad, area, tipo, carrera, cargo, catedra)
                bandera = False

            elif (op == '3'):

                area = input('>> -Ingrese area\n')
                tipo = input('>> -Ingrese tipo de investigacion\n')
                carrera = input('>> -Ingrese carrera\n')
                catedra = input('>> -Ingrese catedra\n')
                cargo = input('>> -Ingrese cargo\n')
                Categoria = input('>> -Ingrese categoria\n')
                importe = float(input('>> -Ingrese importe\n'))
                elemento = DocenteInvestigador.DocenteInvestigador(
                    cuil, apellido, nombre, sueldo, antiguedad, Categoria, importe, area, tipo, carrera, cargo, catedra)
                bandera = False

            elif (op == '4'):

                categoria = int(input('>> -Ingrese una categoría\n'))
                elemento = PersonaldeApoyo.PersonaldeApoyo(
                    cuil, apellido, nombre, sueldo, antiguedad, categoria)
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

    def opc9(self, lista):
        usuario = input('>>Ingrese usuario\n')
        contraseña = input('>>Ingrese contraseña\n')
        
        if (usuario == 'uTesorero' and contraseña == 'ag@74ck'):
            tesorero = ITesorero(lista)
            control = input('>>Ingrese dni del empleado a buscar (Ingrese T para terminar)\n')
        
        while control != 'T':
            tesorero.gastosSueldoPorEmpleado(control)
            control = input(
                '>>Ingrese dni del empleado a buscar (Ingrese T para terminar)\n')
        else:
            print('Usuario y/o contraseña incorrectos\n')

    def opc10(self, lista):
        usuario = input('>>Ingrese usuario\n')
        contraseña = input('>>Ingrese contraseña\n')
        
        if (usuario == 'uDirector' and contraseña == 'ufC77#!1'):
            director = IDirector(lista)
            control = input('>>Ingrese una OPCION:\n1_ Modificar Sueldo Basico de un empleado\n2_ Modificar porcentaje por cargo de un empleado\n3_ Modificar porcentaje por categoria de un empleado\n4_ Modificar importe Extra de un empleado\n0_ Salir\n')
            
            while contr != '0':
                if contr == '1':
                    dni = input('>>Ingrese un DNI\n')
                    basico = float(input('>>Ingrese nuevo sueldo básico\n'))
                    director.modificarBasico(dni, basico)
                    
                elif contr == '2':
                    dni = input('>>Ingrese un DNI\n')
                    porcentaje = int(input('>>Ingrese un nuevo porcentaje (%)\n'))
                    porcentaje = 1+porcentaje/100
                    director.modificarPorcentajeporcargo(dni, porcentaje)
                    
                elif contr == '3':
                    dni = input('>>Ingrese un DNI\n')
                    porcentaje = int(input('>>Ingrese un nuevo porcentaje (%)\n'))
                    porcentaje = 1+porcentaje/100
                    director.modificarPorcentajeporcategoria(dni, porcentaje)
                    
                elif contr == '4':
                    dni = input('>>Ingrese un DNI\n')
                    Importe = float(input('>>Ingrese NUEVO importe extra: \n'))
                    director.modificarImporteExtra(dni, Importe)
                    
                else:
                    print('Opcion invalida')
                contr = input('>>Ingrese una opcion:\n1_ Modificar Sueldo Basico de un empleado\n2_ Modificar porcentaje por cargo de un empleado\n3_ Modificar porcentaje por categoria de un empleado\n4_ Modificar importe Extra de un empleado\n0_ Salir\n')
        else:
            print('Usuario y/o contraseña incorrectos\n')
