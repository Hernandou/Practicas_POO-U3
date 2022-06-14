from ManejadorCalefactores import ListCalefactor
from ClassCalElectrico import CalefactorElectrico
from ClassCalGas import CalefactorGas

if __name__ == '__main__':
    
    menor = None
    ans = int(input('>> -Ingrese size del arreglo: '))
    a = ListCalefactor(ans)
    cost = float(input('>> Ingrese costo por m3: '))
    cantM3 = float(input('>> Ingrese la cantidad de m3: '))
    a.CalcularConsumoGas(cost,cantM3) #Calefactor Gas
    costW = float(input('>> Ingrese costo por KW/h: '))
    cantH = float(input('>> Ingrese la CANTIDAD estimada a consumir por hora: '))
    a.CalcularConsumoElectrico(costW,cantH)
    menor = a.CalcularMenorElectrico()
    print('> El Calefactor ELECTRICO con MENOR consumo es: {}'.format(menor))
    menorG = a.CalcularMenorGas()
    print('> El Calefactor a GAS con menor consumo es: {}'.format(menorG))
