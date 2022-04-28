from re import M
from manejadorViajero import manejador

if __name__ == '__main__':
    #Genero instancias de la clase viajero
    m=manejador()
    m.cargarObjeto()

    #apartado 1
    m.comparar()
    print("\n")

    #apartado 2
    #m.acumular()#
    print("\n")

    #apartado 3
    #m.canjear()