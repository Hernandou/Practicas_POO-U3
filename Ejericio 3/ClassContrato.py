import csv
from datetime import date, datetime

class Contrato:
    
    __fechInicio = ''
    __fechaFin = ''
    __PagoMens = 0
    __Jugador = None
    __Equipo = None
    
    def __init__(self,fechaInicio,fechaFin,PagoMens,Jugador,Equipo):
        self.__fechInicio = fechaInicio
        self.__fechaFin = fechaFin
        self.__PagoMens = PagoMens
        self.__Jugador = Jugador
        self.__Equipo = Equipo
        
    def getJugador(self):
        return(self.__Jugador)
    
    def getEquipo(self):
        return(self.__Equipo)
    
    def getFechaFin(self):
        return(self.__fechaFin)
    
    def getMes(self):
        dia = datetime.today()
        mesHoy = datetime.strftime(dia,'%m')
        mesFin = self.__fechaFin.split(' /')
        mesF = int(mesFin[1])
        mes = mesF-int(mesHoy)
        return(mes)
        
    def getSueldo(self):
        return(self.__PagoMens)

    def __str__(self):
        return('\t\t\tContrato\n-Fecha Inicio {}              Fecha Fin: {}'.format(self.__fechInicio,self.__fechaFin))
        
        