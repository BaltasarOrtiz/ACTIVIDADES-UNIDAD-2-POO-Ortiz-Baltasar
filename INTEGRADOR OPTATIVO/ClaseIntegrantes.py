
class Integrantes:
    __idProyecto = str
    __apellidoNombre = str
    __dni = int
    __categoriaIvestigacion = str
    __rol = str

    def __init__(self, pr, AyN, dni, categ, rol):
        self.__idProyecto = pr
        self.__apellidoNombre = AyN
        self.__dni = dni
        self.__categoriaIvestigacion = categ
        self.__rol = rol

    def getId(self):
        return self.__idProyecto

    def getRol(self):
        return self.__rol

    def getCateg(self):
        return self.__categoriaIvestigacion
