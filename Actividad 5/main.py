
import csv
from ClasePlan import PlanAhorro
from menu import llamarMenu
from os import path #visual

if __name__ == '__main__':
    listaPlan = []
    archivo = open(path.dirname(__file__) + '/planes.csv') #visual

    reader = csv.reader(archivo, delimiter=";")
    for fila in reader:
        p = PlanAhorro(fila[0], fila[1], fila[2], fila[3])
        #PlanAhorro.cuotas(fila[4], fila[5])
        listaPlan.append(p)
        
    archivo.close()
    
    llamarMenu(listaPlan)