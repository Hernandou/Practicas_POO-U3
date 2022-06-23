from mod import db
class Usuario(db.Model):

    __tablename__ = 'usuario' 
    __id = 0
    __nombre = ''
    __correo = ''
    __clave = ''
    __Receta = []

    def __init__(self,ID,nombre,correo,clave):

        self.__ID = ID
        self.__nombre = nombre
        self.__correo = correo
        self.__clave = clave

    def getID(self):
        return(self.__ID)

    def getNombre(self):
        return(self.__nombre)
    
    def getCorreo(self):
        return(self.__correo)

    def getClave(self):
        return(self.__clave)
