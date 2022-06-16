from classManejadorFlores import ListFlores
from classManejadorRamos import ListRamo
from classMenu import Menu
from classRamos import Ramos

if __name__ == '__main__':
    
    obj = ListFlores()
    obj.mostrarCatalogo()
    Lram = ListRamo()
    mnu = Menu()
    ram = Ramos()
    band = False
    
    while(not band):
        
        print(''' 
              
    -------- Menu ---------
    1) Cargar Ramo
    2) Mostrar nombre flores mas vendidas
    3) Funcion C
    4) Salir    
              ''')
        
        ans = str(input('>> Ingrese una opcion: '))
        
        if(ans != '4'):
            mnu.GestOpc(ans,obj,Lram,ram)
            
        else:
            
            band = True
    
    
    