import csv
from ClaseViajeros import Viajero

from os import path

class manejador:
    __lista: list[Viajero] #atributo de la clase manejador que almacena la lista que voy a manipular

    def __init__(self):
        self.__lista=self.cargarObjeto()
    
    def cargarObjeto(self):
        listaViajero = []
        archivo = open(path.dirname(__file__) + '/ArchViajeros.csv')
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            v = Viajero(int(fila[0]), int(fila[1]), str(fila[2]), str(fila[3]), int(fila[4]))
            listaViajero.append(v)
        
        return(listaViajero)
        archivo.close()


    #apartado 1
    def comparar(self):
        viajMAX = self.__lista[0]
        for vj in self.__lista:
            if vj > viajMAX:
                viajMAX=vj
        print("Viajeros con mayor cantidad de millas acumuladas")
        for vj in self.__lista:
            if(viajMAX.cantidadTotalMillas()==vj.cantidadTotalMillas()):
                print("Viajero: {} - Nombre: {} - Millas: {}".format(vj.getNumViajero(), vj.getNombre(), vj.cantidadTotalMillas()))

    #apartado 2
    def acumular(self):
        for vj in self.__lista:
            num = int(input("Millas actuales: {} --- Ingrese millas a acumular: ".format(vj.cantidadTotalMillas())))
            vj+=num
            print("Nueva cantidad de millas acumuladas: {}".format(vj.cantidadTotalMillas()))
            print("\n")
    
    #apartado 3
    def canjear(self):
        for vj in self.__lista:
            num=int(input("Millas actuales: {} --- Ingrese millas a canjear: ".format(vj.cantidadTotalMillas())))
            vj-=num
            print("Nueva cantidad de millas: {}".format(vj.cantidadTotalMillas()))
            print("\n")
    