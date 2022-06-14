from ClassContrato import Contrato
import numpy as np
from datetime import datetime
import random

class ListContrato:

    def __init__(self):

        self.__list = np.empty(0, dtype=Contrato)

    def AgregarContrato(self,jugador,equip,PagoMens):
        fechaInicio = datetime.now()
        fechaInicio = datetime.strftime(fechaInicio, '%d / %m / %y')
        aux = fechaInicio
        FechaFin = aux.split('/')
        mes_rand = random.randint(1, 12)
        FechaFin[1] = mes_rand
        FechaFin[2] = 23
        FechaFin = ' / '.join(map(str, FechaFin))
        obj = Contrato(fechaInicio,FechaFin,PagoMens,jugador,equip)
        self.__list = np.append(self.__list,obj)
    
    def ConsultarContratos(self,dni):
        i = 0
        band = False
        
        while(i < len(self.__list) and band == False):
            jug = self.__list[i].getJugador()
            
            if(jug.getDNI() == dni):
                print('\n')
                equip = self.__list[i].getEquipo()
                band = True
                print('''Jugador {} 
                      Contratado en el equipo {} 
                      Su contrato finaliza el dia: {}'''.format(jug.getNombre(), equip.getNombre(),self.__list[i].getFechaFin()))
            i += 1
            
    def ConsultarVencimiento(self,nomb):
        i = 0
        band = False
        while(i < len(self.__list) and band == False):
            equip = self.__list[i].getEquipo()
            if(equip.getNombre() == nomb):
                jug = self.__list[i].getJugador()
                print('\n')
                band = True
                
                if(self.__list[i].getMes() == 6):
                    print('El jugador {} vencera su contrato dentro de 6 meses'.format(jug.getNombre()))
            i += 1            
                
                
    def ImporteSueldos(self,nomb):
        acum = 0
        i = 0
        band = False
        
        while(i < len(self.__list) and band == False):
            eqp = self.__list[i].getEquipo()
            
            if(eqp.getNombre() == nomb):
                print('yi')
                band = True
                acum += self.__list[i].getSueldo()
            i += 1
            
        return(acum)
            