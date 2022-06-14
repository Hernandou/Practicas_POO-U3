from zope.interface import Interface
from zope.interface import implementer

class Inter(Interface):
    
    def InsertarElemento(elem,posicion):
        pass
    
    def AgregarElemento(elem):
        pass
    
    def MostrarElemento(posicion):
        pass