import csv
from ClaseViajeros import Viajero
from menu import llamarMenu

if __name__== '__main__':
    listaViajero = []
    archivo = open("ArchViajeros.csv")
    reader = csv.reader(archivo, delimiter=";")
    next(reader)
    for fila in reader:
        v = Viajero(fila[0], fila[1], fila[2], fila[3], fila[4])
        listaViajero.append(v)
    archivo.close()
    #print(len(listaViajero))
    llamarMenu(listaViajero)