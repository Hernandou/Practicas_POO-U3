from zope.interface import implementer
from ClassNodo import Nodo
from ClassInvestigador import Investigador
from ClassDocente import Docente
from ClassPersonalApoyo import PersonaldeApoyo
from ClassDocenteInvestigador import DocenteInvestigador
from InterfaceDirector import IDirector
from InterfaceTesorero import ITesorero


@implementer(IDirector)
@implementer(ITesorero)
class Lista:

    __cabeza = None
    __actual = None
    __index = 0
    __tope = 0

    def __init__(self):
        self.__cabeza = None
        self.__actual = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index == self.__tope:
            self.__actual = self.__cabeza
            self.__index = 0
            raise StopIteration
        else:
            self.__index += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato

    def agregarPersona(self, persona):
        nodo = Nodo(persona)
        nodo.setSiguiente(self.__cabeza)
        self.__cabeza = nodo
        self.__actual = nodo
        self.__tope += 1
        print(self.__tope)

    def insertarelemento(self, pos, objeto):
        counter = 1
        cabeza = self.__cabeza
        if self.__cabeza is None:
            nodo = Nodo(objeto)
            nodo.setSiguiente(self.__cabeza)
            self.__cabeza = nodo
            self.__actual = nodo
            self.__tope += 1
        while counter < pos - 1 and cabeza is not None:
            counter += 1
            cabeza = cabeza.getSiguiente()
        if pos == 1:
            newNode = Nodo(objeto)
            newNode.setSiguiente(cabeza)
            self.__cabeza = newNode
            self.__actual = newNode
        else:
            newNode = Nodo(objeto)
            newNode.setSiguiente(cabeza.getSiguiente())
            cabeza.setSiguiente(newNode)
        self.__tope += 1

    def agregarelementofinal(self, objeto):
        print("Insertando al final")
        if self.__cabeza is None:
            newNode = Nodo(objeto)
            newNode.setSiguiente(self.__cabeza)
            self.__cabeza = newNode
            self.__actual = newNode
        else:
            cabeza = self.__cabeza
            while cabeza.getSiguiente() is not None:
                cabeza = cabeza.getSiguiente()
            newNode = Nodo(objeto)
            cabeza.setSiguiente(newNode)
        self.__tope += 1

    def mostrarelemento(self, pos):
        dato = None
        cont = 1
        if self.__cabeza is None and pos != 1:
            dato = None
        cabeza = self.__cabeza
        while cabeza.getSiguiente() is not None and cont < pos:
            cont += 1
            cabeza = cabeza.getSiguiente()
        if cont == pos:
            dato = cabeza.getDato()

        return dato.getTipoAgente()

    def mostrardocenteinv(self, carrera):
        lista = []
        cabeza = self.__cabeza
        while cabeza is not None:
            if type(cabeza.getDato()) == DocenteInvestigador:
                if cabeza.getDato().getCarrera() == carrera:
                    lista.append(cabeza.getDato())

            cabeza = cabeza.getSiguiente()

        listaord = sorted(lista)
        for elem in listaord:
            print(elem.getNombre())

    def contar(self, area):
        cabeza = self.__cabeza
        cantDocentesInv = 0
        cantInv = 0
        while cabeza is not None:
            if type(cabeza.getDato()) is DocenteInvestigador or type(cabeza.getDato()) is Investigador:
                if cabeza.getDato().getArea() == area:
                    if type(cabeza.getDato()) is DocenteInvestigador:
                        cantDocentesInv += 1
                    elif type(cabeza.getDato()) is Investigador:
                        cantInv += 1
            cabeza = cabeza.getSiguiente()

        print("Cantidad de Docentes Investigadores: {} -- Cantidad de Investigadores: {}".format(cantDocentesInv, cantInv))

    def listadoOrdenado(self):
        lista = []
        cabeza = self.__cabeza

        while cabeza is not None:
            dato = cabeza.getDato()
            dato.calculaSueldo()
            lista.append(dato)
            cabeza = cabeza.getSiguiente()

        listaord = sorted(lista)
        for elem in listaord:
            print("Nombre y apellido: {}, Tipo de agente: {}, Sueldo:{}".format(
                elem.getNombre() + " " + elem.getApellido(), elem.getTipoAgente(), elem.getSueldo()))

    def mostrarlistadoinv(self, categ):
        total = 0
        cabeza = self.__cabeza
        while cabeza is not None:
            if type(cabeza.getDato()) is DocenteInvestigador:
                if cabeza.getDato().getproincen() == categ:
                    print("Nombre y apellido: {}, Importe Extra: {}".format(cabeza.getDato().getNombre(
                    ) + " " + cabeza.getDato().getApellido(), cabeza.getDato().getimporte()))
                    dato = cabeza.getDato()
                    total += dato.getimporte()
            cabeza = cabeza.getSiguiente()
        print("Total de dinero que la Secretaría de Investigación debe solicitar al Ministerio en concepto de importe extra: {}".format(total))

    def obtenerlista(self):
        lista = []
        cabeza = self.__cabeza
        while cabeza is not None:
            dato = cabeza.getDato()
            dicc = dato.toJson()
            lista.append(dicc)

            cabeza = cabeza.getSiguiente()

        return lista

    def modificarBasico(self, dni, nuevobasico):
        self.__actual = self.__comienzo
        self.__indice = 0
        bandera = True
        while (self.__indice < self.__tope and bandera):
            if self.__actual.getdato().getdni() == dni:
                bandera = not bandera
            else:
                self.__actual = self.__actual.getsiguiente()
                self.__indice += 1
        if not bandera:
            self.__actual.getdato().modificarbasico(nuevobasico)
        self.__actual = self.__comienzo
        self.__indice = 0

    def modificarImporteExtra(self, dni, nuevoimporteextra):
        self.__actual = self.__comienzo
        self.__indice = 0
        bandera = True
        while (self.__indice < self.__tope and bandera):
            if self.__actual.getdato().getdni() == dni:
                bandera = not bandera
            else:
                self.__actual = self.__actual.getsiguiente()
                self.__indice += 1
        if not bandera:
            if type(self.__actual.getdato() == DocenteInvestigador):
                self.__actual.getdato().modificarImporteExtra(nuevoimporteextra)
            else:
                print("El agente no es un docente investigador")
        self.__actual = self.__comienzo
        self.__indice = 0

    def modificarPorcentajeporcargo(self, dni, nuevoporcentaje):
        self.__actual = self.__comienzo
        self.__indice = 0
        bandera = True
        while (self.__indice < self.__tope and bandera):
            if self.__actual.getdato().getdni() == dni:
                bandera = not bandera
            else:
                self.__actual = self.__actual.getsiguiente()
                self.__indice += 1
        if not bandera:
            if type(self.__actual.getdato() == Docente):
                self.__actual.getdato().modificarporcentaje(nuevoporcentaje)
            else:
                print("El agente no es un docente")
        self.__actual = self.__comienzo
        self.__indice = 0

    def modificarPorcentajeporcategoria(self, dni, nuevoporcentaje):
        self.__actual = self.__comienzo
        self.__indice = 0
        bandera = True
        
        while (self.__indice < self.__tope and bandera):
            
            if self.__actual.getdato().getdni() == dni:
                bandera = not bandera
                
            else:
                self.__actual = self.__actual.getsiguiente()
                self.__indice += 1
                
        if not bandera:
            if type(self.__actual.getdato() == PersonaldeApoyo):
                self.__actual.getdato().modificarporcentaje(nuevoporcentaje)
                
            else:
                print("El agente no es personal de apoyo")
        self.__actual = self.__comienzo
        self.__indice = 0

    def gastosSueldoPorEmpleado(self, dni):
        valor = None
        self.__actual = self.__comienzo
        self.__indice = 0
        bandera = True
        
        while (self.__indice < self.__tope and bandera):
            
            if self.__actual.getdato().getdni() == dni:
                print("Sueldo: {}".format(self.__actual.getdato().calcularsueldo()))
                bandera = not bandera
                
            else:
                self.__actual = self.__actual.getsiguiente()
                self.__indice += 1
                
        if bandera:
            print("No se encontro empleado con dni ingresado")
        self.__actual = self.__comienzo
        self.__indice = 0

    def toJSON(self):
        d = dict(__class__=self.__class__.__name__, Personal=[persona.toJSON() for persona in self])
        return d
