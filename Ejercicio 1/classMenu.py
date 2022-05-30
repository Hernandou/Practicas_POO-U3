
class Menu:
    
    __Switch = None
    
    def __init__(self):
        
        self.__Switch = {
            
            '1' : self.opc1,
            '2' : self.opc2,
            '3' : self.opc3
        }
        
        
    def GestOpc(self,opc,obj):
        
        func = self.__Switch.get(opc, lambda : print('Opcion NO valida'))
        func(obj)

    def opc1(self,obj):
        cod = 2
        #cod = int(input('>> -Ingrese codigo de facultad: '))     
        obj.MostrarDatos(cod)   
        
    def opc2(self,obj):
        print('Opc 2')
        
    def opc3(self,obj):
        print('Opc 3')