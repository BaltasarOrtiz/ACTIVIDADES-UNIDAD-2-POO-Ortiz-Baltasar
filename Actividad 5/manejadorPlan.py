from ClasePlan import PlanAhorro
import csv
from os import path #visual

class ManejadorPlan:
    __lista: list[PlanAhorro] #atributo de la clase manejador que almacena la lista que voy a manipular

    def __init__(self):
        self.__lista=self.cargarObjetos()

    #GENERADOR DE OBJETOS
    def cargarObjetos(self):
        listaPlan = []
        archivo = open(path.dirname(__file__) + '/planes.csv') #visual
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:  
            objeto = PlanAhorro(int(fila[0]), str(fila[1]), str(fila[2]), int(fila[3]))
            PlanAhorro.cambiarCantCuota(fila[4])
            PlanAhorro.cambiarCantCuotaPaga(fila[5])
            listaPlan.append(objeto)
        
        return(listaPlan)
        archivo.close()
        

    #APARTADO 2a
    def actualizaValor(self):
        for i in self.__lista:
            print("\n")
            print("Codigo de Plan:{} Modelo:{} Version del Vehiculo:{}".format(i.getCodPlan(), i.getModelo(), i.getVer()))
            actual=input("Ingrese el nuevo valor del vehiculo: ")
            i.modificaPrecio(actual)

    #APARTADO 2b
    def valorCuota(self):
        v = int(input("Ingrese un valor:"))
        for i in self.__lista:
            if v<i.getValorCuota():
                print("Codigo de Plan:{} Modelo:{} Version del Vehiculo:{}".format(i.getCodPlan(), i.getModelo(), i.getVer()))

    #APARTADO 2c
    def MostrarMonto(self):
        for i in self.__lista:
            print("Monto que se debe haber pagado para licitar el vehiculo: {:.2f}".format(i.MontoPagar()))

    #APARTADO 2d
    def buscaPlan(self):
        c = int(input("Ingrese codigo del vehiculo: "))
        for i in self.__lista:
            if(c==i.getCodPlan()):
                print("Cuotas actuales que debe tener pagas:{}".format(i.getCuotaPagar()))
                i.cambiarCantCuotaPaga(int(input("Ingrese las nuevas cuotas a licitar: ")))