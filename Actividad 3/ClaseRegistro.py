
class registro:
    __varTemp = float
    __varHum = float
    __varPres = float
    
    
    def __init__(self, temp, hum, pres):
        self.__varTemp = temp
        self.__varHum = hum
        self.__varPres = pres
    
    
    def getTemp(self):
        return self.__varTemp

    def getHum(self):
        return self.__varHum
    
    def getPres(self):
        return self.__varPres
    