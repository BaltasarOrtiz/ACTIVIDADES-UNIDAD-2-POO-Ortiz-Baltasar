import csv
from ClaseViajeros import Viajero
from menu import llamarMenu


def test():
    print("Test Realizado")
    v = Viajero(134, 23897122, "Oscar", "Guevara", 4000)
    print(v)



if __name__== '__main__':
    test()
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
