
class PlanAhorro:
    __codPlan = int
    __modelo = ""
    __versionVH = ""
    __valorVH = float
    __cantCuota: int = 0
    __cantCuotaPaga: int = 0 

    def __init__(self, codP, model, ver, val):
        self.__codPlan = codP
        self.__modelo = model
        self.__versionVH = ver
        self.__valorVH = val

    def getCodPlan(self):
        return self.__codPlan

    def getModelo(self):
        return self.__modelo

    def getVer(self):
        return self.__versionVH

    def getValorCuota(self):
        return (float(self.__valorVH)/int(self.__cantCuota))+float(self.__valorVH)*0.10
    
    def modificaPrecio(self, price):
        self.__valorVH = price

    def modificaCuotaPagar(self, nuevaC):
        self.__cantCuotaPaga=nuevaC

    
    def MontoPagar(self):
        return self.getValorCuota()*int(self.__cantCuotaPaga)
    
    #METODOS DE CLASE
    @classmethod
    def cambiarCantCuota(cls, cc):
        cls.__cantCuota=cc
    
    @classmethod
    def cambiarCantCuotaPaga(cls, cp):
        cls.__cantCuotaPaga=cp
    
    @classmethod
    def getCuotaPagar(cls):
        return cls.__cantCuotaPaga

    