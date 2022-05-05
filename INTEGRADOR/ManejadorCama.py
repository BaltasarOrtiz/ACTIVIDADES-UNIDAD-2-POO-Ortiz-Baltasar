#archivos
from os import path #para abrir el archivo camas.csv
import csv
import os

#clases y manejadores
from ClaseCamas import cama

#arreglos
from numpy import ndarray
import numpy as np


class ManejaCama:
    __arreCama: ndarray


    #carga de objetos
    def __init__(self):
        self.__arreCama=self.cargarObjetoC()
    

    def cargarObjetoC(self):
        listaCamas = []
        archivo = open(path.dirname(__file__) + '/camas.csv') #para abrir el archivo camas.csv
        reader = csv.reader(archivo, delimiter = ";")
        next(reader) #saltear la cabecera del archivo
        for fila in reader:
            ca = cama(int(fila[0]), int(fila[1]), bool(fila[2]), str(fila[3]), str(fila[4]), str(fila[5]), str(fila[6]))
            listaCamas.append(ca)
    
        archivo.close()
        arre = np.array(listaCamas)
        return arre


    def buscaCama(self, NomyApe):
        i=0
        while i<len(self.__arreCama) and self.__arreCama[i].getNom() != NomyApe:
            i+=1

        if i < len(self.__arreCama):
            return i
        else:
            return -1 
    

    def mostrarDatosPaciente(self, pos):
        #realizo el alta
        self.__arreCama[pos].setAlta(input("Ingrese fecha del alta (dd/mm/aaaa): "))
        #muestro los datos del paciente
        os.system("cls")
        print("Paciente: {}         Cama: {}     Habitacion: {}".format(self.__arreCama[pos].getNom(), self.__arreCama[pos].getIdCama(), self.__arreCama[pos].getHab()))
        print("Diagnostico: {}      Fecha Internacion: {}".format(self.__arreCama[pos].getDiag(), self.__arreCama[pos].getFechaInter()))
        print("Fecha de Alta: {}".format(self.__arreCama[pos].getFechaAlta()))
    

    def obtenerIdCama(self, pos):
        #retorno el id de la cama para identificar los medicamentos del paciente
        return self.__arreCama[pos].getIdCama()
    
    def Diagnostico(self, nombreDiag):
        for elem in self.__arreCama:
            if elem.getDiag() == nombreDiag and elem.getFechaAlta() != 'None':
                print("Id Cama: {}  Habitacion: {}  Estado: {}  Apellido y Nombre: {}".format(elem.getIdCama(), elem.getHab(), elem.getEstado(), elem.getNyA()))
                print("Diagnostico: {}  Fecha de Internacion: {}    Fecha Alta: {}".format(elem.getDiag(), elem.getFechaInter(), elem.getFechaAlta()))
