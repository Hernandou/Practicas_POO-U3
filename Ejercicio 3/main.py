from CManejadorJugadores import ListJugadores
from CManejadorEquipos import ListEquipos
from CManejadorContrato import ListContrato

if __name__ == '__main__':
    a = ListJugadores()
    b = ListEquipos()
    cnt = ListContrato()    
    ans = int(input('>> -Ingrese DNI del jugador: '))
    jug = a.BuscJugador(ans)

    if(jug != None):
        equip = input('>> -Ingrese nombre de  Equipo: ')
        eqp = b.BuscEquip(equip)
        
        if(eqp != None):
            pago = int(input('>> -Ingrese SUELDO de jugador: $'))
            cnt.AgregarContrato(jug,eqp,pago)
        else:
            print('>>Equipo NO encontrado')
    else:
        print('>> Jugador NO enocntrado')
        
    dni = int(input('>> -Ingrese DNI de Jugador a consultar Contrato: '))
    cnt.ConsultarContratos(dni)
    nombEquip = input('>> -Ingrese Nombre del equipo: ')
    cnt.ConsultarVencimiento(nombEquip)
    nombE = input('>> -Ingrese Nombre del equipo: ') 
    sueld = cnt.ImporteSueldos(nombE)
    
    if(sueld != 0):
        print('>> El importe TOTAL sueldos del equipo {} es: ${}'.format(nombEquip,sueld))
    else:
        print('No se encontro equipo')
    
        
    
    
