
class cama:
    __idCama = int
    __habitacion = int
    __estado = bool
    __apellidoNombre = ""
    __diagnostico = ""
    __fechaInternacion = ""
    __fechaAlta = ""

    def __init__(self, id, hab, est, AyN, diag, finter, falta):
        self.__idCama = id
        self.__habitacion = hab
        self.__estado = est
        self.__apellidoNombre = AyN
        self.__diagnostico = diag
        self.__fechaInternacion = finter
        self.__fechaAlta = falta
    

    def getIdCama(self):
        return self.__idCama
    
    def getNom(self):
        return self.__apellidoNombre
    
    def getHab(self):
        return self.__habitacion
    
    def getEstado(self):
        return self.__estado
    
    def getNyA(self):
        return self.__apellidoNombre
    
    def getDiag(self):
        return self.__diagnostico
    
    def getFechaInter(self):
        return self.__fechaInternacion
    
    def getFechaAlta(self):
        return self.__fechaAlta

    def setAlta(self, fecha):
        self.__fechaAlta = fecha
        self.__estado = False
    