

class Conjunto:
    __conjunto = []

    def __init__(self, cj):
        self.__conjunto = cj
    
    def __str__(self):
        return str(self.__conjunto)
    
    def __add__(self, otro):
        resultado = []
        for elemento in self.__conjunto:
            resultado.append(elemento)

        for elemento in otro.__conjunto:
            if elemento not in resultado:
                resultado.append(elemento)
        
        return Conjunto(resultado)

    
    # A = {1, 2, 3, 4}    B = {4, 6, 7}    C = {1, 2, 3}
    def __sub__(self, otro):
        resultado = []

        for elemento in self.__conjunto:
            if elemento not in otro.__conjunto:    
                resultado.append(elemento)
        
        return Conjunto(resultado)

    def __eq__(self, otro):
        resultado = True
        if len(self.__conjunto) != len(otro.__conjunto):
            resultado = False
        
        for elemento in self.__conjunto:
            if elemento not in otro.__conjunto:
                resultado = False

        return resultado

        


    