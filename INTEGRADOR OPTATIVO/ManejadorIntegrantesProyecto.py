from ClaseIntegrantes import Integrantes
import numpy as np
from numpy import ndarray
import csv

class ManejIntegrante:
    __arreIntegrante = ndarray

    def __init__(self):
        self.__arreIntegrante = self.cargarobjetos()

    def cargarobjetos(self):
        listatemp = []
        archivo = open("integrantesProyecto.csv")
        reader = csv.reader(archivo, delimiter = ";")
        next(reader)
        for fila in reader:
            integ = Integrantes(str(fila[0]), str(fila[1]), int(fila[2]), str(fila[3]), str(fila[4]))
            listatemp.append(integ)

        arre = np.array(listatemp)
        archivo.close()
        return arre


    def contarintegrantes(self, idp):
        acum=0
        for elem in self.__arreIntegrante:
            if idp == elem.getId() and elem.getRol() == "integrante":
                acum+=1
        return acum

    def calcularpuntaje(self, listaIdsProyec):
        puntajetotal = 0
        print("Iniciando Calculo de puntaje del proyecto: {}".format(listaIdsProyec))

        #Apartado a) Contar integrantes.
        if self.contarintegrantes(listaIdsProyec) >= 3:
            puntajetotal+=10
        else:
            puntajetotal-=20

        #Para directores y codirectores.
        for elem in self.__arreIntegrante:
            if listaIdsProyec == elem.getId():
                #Excluyo los integrantes.
                if elem.getRol() != "integrante":

                    if elem.getRol() != "codirector": #Aqui entra solo cuando es director.
                        if elem.getRol() == "director":
                            if elem.getCateg() == "I" or elem.getCateg() == "II":
                                puntajetotal+=10
                            else:
                                puntajetotal-=5
                                print("El proyecto debe tener director de categoria I o II")
                        else:
                            puntajetotal-=10
                            print("El proyecto debe tener un director")


                    else: #Aqui entra solo si es codirector.

                        if elem.getRol() == "codirector":
                            if elem.getCateg() == "I" or elem.getCateg() == "II" or elem.getCateg() == "III" :
                                puntajetotal+=10
                            else:
                                puntajetotal-=5
                                print("El proyecto debe tener codirector de categoria I o II o III")
                        else:
                            puntajetotal-=10
                            print("El proyecto debe tener un codirector")

        return puntajetotal


