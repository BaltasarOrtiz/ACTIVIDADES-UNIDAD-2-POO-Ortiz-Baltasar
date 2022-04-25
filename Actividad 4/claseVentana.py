
class Ventana:
    __titulo = ""
    __XverSup = float
    __YverSup = float
    __XverInf = float
    __YverInf = float
    
    def __init__(self, tit="ventana", Xsup=0, Ysup=0, Xinf=500, Yinf=500):
        self.__titulo = tit
        self.__XverSup = Xsup
        self.__YverSup = Ysup
        self.__XverInf = Xinf
        self.__YverInf = Yinf
    
    def mostrar(self):
        print("Titulo:", self.__titulo, "Xsup:", self.__XverSup, "Ysup:", self.__YverSup, "Xinf:", self.__XverInf, "Yinf:", self.__YverInf)
    
    def getTitulo(self):
        return self.__titulo
    
    
    def alto(self):
        return (self.__YverInf - self.__YverSup)
        
    def ancho(self):
        return (self.__XverInf - self.__XverSup)
    
    
    def moverDerecha(self, derecha=1):
        if self.__XverSup+derecha>=0: 
            self.__XverSup+=derecha
        
        if self.__XverInf+derecha<=500:
            self.__XverInf+=derecha
            
    
    
    def moverIzquierda(self, izquierda=1):
        if self.__XverSup-izquierda>=0: 
            self.__XverSup-=izquierda
            
        if self.__XverInf-izquierda<=500:
            self.__XverInf-=izquierda
        
    
    def bajar(self, baja=1):
        if self.__YverSup-baja>=0:
            self.__YverSup-=baja
        
        if self.__YverInf-baja<=500:
            self.__YverInf-=baja
            
    def subir(self, sube=1):
        if self.__YverSup+sube>=0:
            self.__YverSup+=sube
        if self.__YverInf+sube<=500:
            self.__YverInf+=sube
            
    
        