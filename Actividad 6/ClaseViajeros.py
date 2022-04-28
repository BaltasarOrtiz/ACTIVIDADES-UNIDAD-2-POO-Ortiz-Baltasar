from __future__ import annotations

class Viajero:
    __numeroViajero = ""
    __DNI = ""
    __nombre = ""
    __apellido = ""
    __millasAcum = ""
    
    
    def __init__(self, numV, dni, nom, ape, milla):
        self.__numeroViajero = int(numV)
        self.__DNI = dni
        self.__nombre = nom
        self.__apellido = ape
        self.__millasAcum = milla
    
    #obtener atributos
    def cantidadTotalMillas(self):
        return(self.__millasAcum)
    
    def getNombre(self):
        return self.__nombre
    
    def getNumViajero(self):
        return(self.__numeroViajero)
    
    
    #comparar inciso 1          
    def __gt__(self, otro: Viajero):
        return (self.__millasAcum > otro.cantidadTotalMillas())
    
    #acumular inciso 2
    def __add__(self, numero: int):
        self.__millasAcum=self.__millasAcum+numero
        return self
    
    #canjear inciso 3
    def __sub__(self, numero: int):
        self.__millasAcum=self.__millasAcum-numero
        return self
    