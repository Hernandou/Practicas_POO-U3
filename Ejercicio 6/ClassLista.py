from ClassNodo import Nodo

class Lista:
    __cabeza = None
    __cant = 0
    __actual = None
    __index = 0

    def __init__(self):
        self.__cabeza = None
        self.__cant = 0
        self.__index = 0
        self.__actual = None

    def __iter__(self):
        return(self)

    def __next__(self):
        if(self.__cabeza == self.__cant):
            self.__actual = self.__cabeza
            self.__index = 0

            raise StopIteration
        else:

            self.__index += 1
            dat = self.__actual.getAparato()
            self.__actual = self.__actual.getSiguiente()
            return(dat)

    def AgregarAparato(self, aparato):
        # Crea la instancia de NODO con el argumento de la instancia a guardar
        node = Nodo(aparato)
        # Asigna lo que apunta la CABEZA al siguiente del nuevo nodo
        node.setSiguiente(self.__cabeza)
        self.__cabeza = node  # Actualiza/Cambia la cabeza
        self.__cant += 1

    def InsertarNodo(self, obj, posicion):
        self.__actual = self.__cabeza
        self.__index = 0

        if(posicion == 0):
            self.AgregarAparato(obj)

        else:
            while(self.__index != posicion and self.__actual != None):
                anterior = self.__actual
                self.__actual = self.__actual.getSiguiente()
                self.__index += 1

            if(self.__index == posicion):
                newNode = Nodo(obj)
                newNode.setSiguiente(self.__actual)
                anterior.setSiguiente(newNode)
                self.__cant += 1
                self.__index = 0
                self.__actual = self.__comienzo

            else:
                raise IndexError

        def MostrarElemento(self, posicion):
            self.__actual = self.__cabeza
            self.__index = 0
            
            while (self.__index != posicion and self.__index < self.__cant):
                self.__actual = self.__actual.getSiguiente()
                self.__index += 1
            
            if self.__index < self.__cant:
                print(type(self.__actual.getAparato()))
            else:
                raise IndexError