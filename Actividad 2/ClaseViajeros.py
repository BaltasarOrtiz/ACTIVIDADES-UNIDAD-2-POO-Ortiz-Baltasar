

class ViajeroFrecuente:
    __numeroViajero = int("")
    __DNI = int
    __nombre = ""
    __apellido = ""
    __millasAcum = float
    
    
    def __init__(self, numV, dni, nom, ape, milla):
        self.__numeroViajero = numV
        self.__DNI = dni
        self.__nombre = nom
        self.__apellido = ape
        self.__millasAcum = milla
        
    def cantidadTotalMillas(self):
        return(self.__millasAcum)
    
    def acumularMillas(self, cantM):
        return(self.__millasAcum+cantM)
    
    def canjearMillas(self, cantCanjeM):
        if(cantCanjeM<=self.__millasAcum):
            return(self.__millasAcum-cantCanjeM)
        else:
            return("Error en la operacion")
    

                
        
    