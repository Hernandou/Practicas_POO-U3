from ClassMenu import Menu
from ObjectEnconder import ObjectEncoder
from ClassLista import Lista

if __name__ == '__main__':

    band = True
    mnu = Menu()

    jsonF = ObjectEncoder()
    lista = Lista()
    dct = jsonF.leerJSONArchivo('/Users/hernan/Desktop/UNSJ/Segundo Año/P O O/Practicas POO/U3/Ejercicio 8/Personal.json')
    lista = jsonF.decodificarDiccionario(dct)
    mnu = Menu()
    while(band):

        print('''
        ------- Menu -------
        1) Funcion A
        2) Funcion B
        3) Funcion C
        4) Funcion D
        5) Funcion E
        6) Funcion F
        7) Funcion G
        8) Funcion H
        9) Funcion I
        9) Funcion J
        5) Salir 
              ''')

        ans = str(input('> Ingrese una OPCION: '))

        if(ans != '5'):
            mnu.GestOpc(ans)

        elif(ans == '5'):
            band = False
