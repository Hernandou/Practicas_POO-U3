from ClassMenu import Menu
from ClassAparato import Aparato
import ObjectEncoder
from ClassHeladera import Heladera
from ClassLavarropas import Lavarropas
from ClassTelevisor import Televisor
from ClassLista import Lista

if __name__ == '__main__':
    band = False
    mnu = Menu()
    
    lista = Lista()
    jsF = ObjectEncoder.ObjectEncoder()
    dct = jsF.LeerJSON('/Users/hernan/Desktop/UNSJ/Segundo Año/P O O/Practicas POO/U3/Ejercicio 6/Aparatos.json')
    lista = jsF.DecodeDict(dct)
    
    while(not band):
        
        print('''
         -------- Menu ---------
         
            1) Funcion A
            2) Funcion B
            3) Funcion C
            4) Funcion D
            5) Salir     
              ''')
        
        ans = str(input('>> -Ingrese Opcion: '))
        
        if(ans != '5'):
            mnu.GestOpc(ans,lista)
        elif(ans == '5'):
            band = True