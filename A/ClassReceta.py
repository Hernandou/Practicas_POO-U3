from mod import db
class Receta(db.Model):
    __tablename__ = 'receta'
    __id = 0
    __nombre = ''
    __tiempo = ''
    __elab = ''
    __cantidMegusta = 0
    __fecha = ''
    __ingredientes = []

    def __init__(self,ID,nombre,tiempo,elab,cantidMegusta,fecha):
        self.__id = 0
        self.__nombre = nombre
        self.__elab = elab
        self.__cantidMegusta = cantidMegusta
        self.__fecha = fecha

    def getID(self):
        return(self.__ID)
    
    def getNombre(self):
        return(self.__nombre)

    def getTiempo(self):
        return(self.__tiempo)

    def getElab(self):
        return(self.__elab)

    def getCantMegusta(self):
        return(self.__cantidMegusta)

    def getFecha(self):
        return(self.__fecha)
