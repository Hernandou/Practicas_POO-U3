from ClassNodo import Nodo
from ClassInvestigador import Investigador
from ClassDocente import Docente
from ClassDocenteInvestigador import DocenteInvestigador


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
