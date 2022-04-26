
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
        self.__valorVH = float(val)

    def getCodPlan(self):
        return self.__codPlan

    def getModelo(self):
        return self.__modelo

    def getVer(self):
        return self.__versionVH

    def getValorCuota(self):
        return ((self.__valorVH/self.__cantCuota)+self.__valorVH*0.10)
    
    def MontoPagar(self):
        return self.getValorCuota()*self.__cantCuotaPaga