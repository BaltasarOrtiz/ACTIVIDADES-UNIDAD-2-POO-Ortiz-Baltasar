
class medicamento:
    __idCama = int
    __idMedicamento = int
    __nombreComercial = ""
    __monodroga = ""
    __presentacion = ""
    __cantidadAplicada = int
    __precioTotal = float

    def __init__(self, idCam, idMedic, nomCom, monoDrog, presen, cantApli, preTot):
        self.__idCama = idCam
        self.__idMedicamento = idMedic
        self.__nombreComercial = nomCom
        self.__monodroga = monoDrog
        self.__presentacion = presen
        self.__cantidadAplicada = cantApli
        self.__precioTotal = preTot

    def getIdCama(self):
        return self.__idCama
    
    def getMedic(self):
        return self.__monodroga
    
    def getPresen(self):
        return self.__presentacion
    
    def getCantidad(self):
        return self.__cantidadAplicada
    
    def getPrecio(self):
        return self.__precioTotal
