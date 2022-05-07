

class Proyecto:
    __idProyecto = str
    __titulo = str
    __palabrasClave = str
    __puntajeTotal = float

    def __init__(self, id, tit, palabraC):
        self.__idProyecto = id
        self.__titulo = tit
        self.__palabrasClave = palabraC


    def getId(self):
        return self.__idProyecto

    def getTitulo(self):
        return self.__titulo

    def getPalabraClave(self):
        return self.__palabrasClave

    def guardarPuntaje(self, tot):
        self.__puntajeTotal=tot

    def getpuntajetotal(self):
        return self.__puntajeTotal

    def __gt__(self, otro):
        return self.__puntajeTotal>otro.__puntajeTotal



