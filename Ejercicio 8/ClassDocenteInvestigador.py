from ClassDocente import Docente
from ClassInvestigador import Investigador


class DocenteInvestigador(Docente,Investigador):
    __categoria = ''
    __importExtra = ''

    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, categoria, importeextra, area, tipo, carrera, cargo, catedra):
        super().__init__(cuil, apellido, nombre, sueldobasico,
                         antiguedad, area, tipo, carrera, cargo, catedra)
        self.__categoria = categoria
        self.__importExtra = importeextra

    def getcategoria(self):
        return(self.__categoria)

    def getimporte(self):
        return self.__importExtra

    def calcularsueldo(self):
        return super().calcularsueldo()+self.__importExtra

    def __str__(self):
        return (super().__str__())

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self.getcuil(),
                apellido=self.getapellido(),
                nombre=self.getnombre(),
                sueldobasico=self.getsueldobasico(),
                antiguedad=self.getantiguedad(),
                categoria=self.__Categoria,
                importeextra=self.__importExtra,
                area=self.getarea(),
                tipo=self.gettipo(),
                carrera=self.getcarrera(),
                cargo=self.getcargo(),
                catedra=self.getcatedra()
            ))
        return d
