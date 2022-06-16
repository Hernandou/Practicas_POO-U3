from ClassMenu import Menu
from ObjectEnconder import ObjectEncoder
from ClassLista import Lista

if __name__ == '__main__':

    band = True
    mnu = Menu()

    jsonF = ObjectEncoder()
    lista = Lista()
    dct = jsonF.LeerJSON("Personal.json")
    lista = jsonF.decodificarDiccionario(dct)
    mnu = Menu()
    while(band):

        print('''
        ------- Menu -------
        1) Funcion A
        2) Funcion B
        3) Funcion C
        4) Funcion D
        5) Salir 
              ''')

        ans = str(input('> Ingrese una OPCION: '))

        if(ans != '5'):
            mnu.GestOpc(ans)

        elif(ans == '5'):
            band = False
