from ClassHeladera import Heladera
from ClassLavarropas import Lavarropas
from ClassTelevisor import Televisor
from ClassLista import Lista
from pathlib import Path
import json

class ObjectEncoder:

    def DecodeDict(self, dct):

        if('__class__' not in dct):

            return dct
        else:

            class_name = dct['__class__']
            class_name = eval(class_name)

            if(class_name == 'Lista'):

                Aparatos = dct['Aparatos']
                dctAparato = Aparatos[0]
                manejador = class__()

                for i in range(len(Aparatos)):
                    dctAparato = Aparatos[i]
                    class_name = dctAparato.pop('__class__')
                    class__ = eval(class_name)
                    atributos = dctAparato['__atributos__']
                    unAparato = class__(**atributos)
                    manejador.AgregarElemento(unAparato)
                return(manejador)

    def LeerJSON(self, file):

        with Path(file).open(encoding='UTF-8') as fuente:
            dic = json.load(fuente)
        fuente.close()
        return(dic)
        dest.close()
        
    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()
