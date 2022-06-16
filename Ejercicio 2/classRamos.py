
class Ramos:
    
    __size = ''
    __list = []
    
    def __init__(self,size = 0):
        
        if(size == 1):
            self.__size = 'Chico'
            
        elif(size == 3):
            self.__size = 'Mediano'
            
        elif(size == 6):
            self.__size = 'Grande'
            
    def AgregarFlores(self,flor):
        
        self.__list.append(flor)
        
    def cargarRamo(self):
        return(self.__list)