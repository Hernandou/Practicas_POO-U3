import json
from pathlib import Path
from ClassInvestigador import Investigador
from ClassDocente import Docente
from ClassPersonalApoyo import PersonaldeApoyo
from ClassDocenteInvestigador import DocenteInvestigador


class ObjectEncoder:

    def cargaJson(self, jsonF):
        obj1 = Docente(cuil='20-3454506-8', apellido='Perez', nombre='Nicolas', sueldo=89000,anti=3, carrera='LCC', cargo='JTP', catedra='Sistemas de Informacion')
        obj2 = Investigador(cuil='15-324235-5', apellido='Dominguez', nombre='Juan',sueldo=120000, anti=2, area='Computacional', tipo='Cientifica')
        obj3 = PersonaldeApoyo(cuil='12-456543-4', apellido='Castro',nombre='Maria', sueldo=140000, anti=2, categoria='12')
        obj4 = DocenteInvestigador(programa='I', importe=25000, cuil='18-3446706-8', apellido='Lopez', nombre='Marcos',sueldo=89000, anti=3, catedra='EyFCI', carrera='LCC', cargo='Simple', area='Estructuras', tipo='Teorica')

        d1 = obj2.toJson()
        d2 = obj2.toJson()
        d3 = obj3.toJson()
        d4 = obj4.toJson()
        lista = [d1, d2, d3, d4]
        self.guardarJSONArchivo(lista,'/Users/hernan/Desktop/UNSJ/Segundo Año/P O O/Practicas POO/U3/Ejercicio 7/Personal.json')

    def guardarJSON(self, lista, archivo):
        with Path(archivo).open('w', encoding='UTF-8') as destino:
            json.dump(lista, destino, indent=4)
            destino.close()


    def LeerJSON(self, archivo):
        with Path(archivo).open(encoding='UTF-8') as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario

    def cargarobjeto(self, claselista):
        listadicc = self.leerJSON('personal.json')
        print(len(listadicc))
        for elem in listadicc:
            if '__class__' not in elem:
                print('No se encuentra la clase')
            else:
                class_name = elem['__class__']
                class_ = eval(class_name)
                print(class_name)

                if class_name == 'Docente':
                    atributos = elem['__atributos__']
                    Doc = class_(**atributos)
                    claselista.agregarPersona(Doc)
                    
                elif class_name == 'Investigador':
                    atributos = elem['__atributos__']
                    Inv = class_(**atributos)
                    claselista.agregarPersona(Inv)
                    
                elif class_name == 'PersonaldeApoyo':
                    atributos = elem['__atributos__']
                    Pers = class_(**atributos)
                    claselista.agregarPersona(Pers)
                    
                elif class_name == 'DocenteInvestigador':
                    atributos = elem['__atributos__']
                    Doc_I = class_(**atributos)
                    claselista.agregarPersona(Doc_I)

    def retornarobjeto(self, tipo):
        if tipo == 'Docente':
            objeto = Docente(cuil='15-1823791-2', apellido='Ortiz', nombre='Juan', sueldo=50000,anti=10, carrera='LSI', cargo='JTP', catedra='Programacion Orientada a Objetos')
        elif tipo == 'Investigador':
            objeto = Investigador(cuil='20-1923192-3', apellido='Dominguez', nombre='Carlos',sueldo=120000, anti=2, area='Computacional', tipo='Cientifica')
        elif tipo == 'Personal Apoyo':
            objeto = PersonaldeApoyo(cuil='12-456543-4', apellido='Pereyra',nombre='Maria', sueldo=70000, anti=1, categoria='I')
        elif tipo == 'Docente Investigador':
            objeto = DocenteInvestigador(programa='I', importe=25000, cuil='18-3446706-8', apellido='Lopez', nombre='Juan Cruz',sueldo=90000, anti=4, catedra='EyFCI', carrera='LCC', cargo='Jefe de Catedra', area='Estructuras', tipo='Teorica')
        else:
            objeto = None

        return objeto
