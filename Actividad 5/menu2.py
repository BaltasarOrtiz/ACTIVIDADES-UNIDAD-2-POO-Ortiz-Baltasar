from manejadorPlan import ManejadorPlan
import os

class Menu:
    __op: int
    __control: ManejadorPlan  

    def __init__(self):
        self.__op=0
        self.__control=ManejadorPlan()

    def mostrar(self):
        centinela=None
        while(centinela!=0):
            self.__op=int(input("""
            **Menu**        
Opcion ->[1] : Actualizar(Valor del vehi­culo de cada plan)
Opcion ->[2] : Mostrar Valores Inferiores [Cod. Plan] [Modelo] [Version](Ingrese el Importe)
Opcion ->[3] : Mostrar monto c/plan
Opcion ->[4] : Modificar la cantidad cuotas que debe tener pagas para licitar.

Ingrese Opcion-> """))
            if(self.__op==1):
               self.opcion1()

            elif(self.__op==2):
                self.opcion2()
            
            elif(self.__op==3):
                self.opcion3()
            
            elif(self.__op==4):
                self.opcion4()

            elif(self.__op==0):
                centinela=0
            else:
                print("Error")

    def opcion1(self):
        os.system("cls")
        self.__control.actualizaValor()
    
    def opcion2(self):
        os.system("cls")
        self.__control.valorCuota()
    
    def opcion3(self):
        os.system("cls")
        self.__control.MostrarMonto()
    
    def opcion4(self):
        os.system("cls")
        self.__control.buscaPlan()