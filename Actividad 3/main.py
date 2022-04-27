
import csv
from ClaseRegistro import registro
from menu import llamarMenu
from os import path #visual

if __name__== '__main__': 
    
    dia = 30
    hora = 24
    lista = []
    
    for i in range(dia):
        lista.append([0]*hora)
    
    archivo = open(path.dirname(__file__) + '/temperaturas.csv') #visual
    reader = csv.reader(archivo, delimiter=",")
    next(reader)
    for line in reader:
        dia = int(line[0])
        hora = int(line[1])
        temp = line[2]
        hum = line[3]
        pres = line[4]
        lista[dia-1][hora-1] = registro(float(temp), float(hum), float(pres))
    archivo.close()
    
    llamarMenu(lista)
    
