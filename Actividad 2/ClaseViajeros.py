

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
        
    def cantidadTotalMillas(self):
        return(self.__millasAcum)
    
    def acumularMillas(self, cantM):
        return(self.__millasAcum+cantM)
    
    def canjearMillas(self, cantCanjeM):
        millas=0
        if(cantCanjeM<=self.__millasAcum):
            return(self.__millasAcum-cantCanjeM)
        else:
            return millas
    
    def getNumViajero(self):
        return(self.__numeroViajero)
                
        
    