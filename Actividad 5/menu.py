
#APARTADO 2a
def actualizaValor(lista):
    for i in range(len(lista)):
        print("\n")
        print("Codigo de Plan:{} Modelo:{} Version del Vehiculo:{}".format(lista[i].getCodPlan(), lista[i].getModelo(), lista[i].getVer()))
        actual=float(input("Ingrese el nuevo valor del vehiculo: "))
        lista[i].modificaPrecio(actual)

#APARTADO 2b
def valorCuota(lista):
    v = int(input("Ingrese un valor:"))
    for i in range(len(lista)):
        if v<lista[i].getValorCuota():
            print("Codigo de Plan:{} Modelo:{} Version del Vehiculo:{}".format(lista[i].getCodPlan(), lista[i].getModelo(), lista[i].getVer()))

#APARTADO 2c
def MostrarMonto(lista):
    for i in range(len(lista)):
        print("Monto que se debe haber pagado para licitar el vehiculo: {:.2f}".format(lista[i].MontoPagar()))

#APARTADO 2d
def buscaPlan(lista):
    c = int(input("Ingrese codigo del vehiculo: "))
    for i in range(len(lista)):
        if(c==lista[i].getCodPlan()):
            print("Cuotas actuales que debe tener pagas:{}".format(lista[i].getCuotaPagar()))
            lista[i].modificaCuotaPagar(int(input("Ingrese las nuevas cuotas a licitar: ")))
            
#MENU
def pedirNumeroEntero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
    return num

def llamarMenu(lista):
        
    salir = False
    opcion = 0
             
    while not salir:
        print("\n")       
        print ("1. Actualizar el valor del vehículo de cada plan. - Opcion 1")
        print ("2. Dado un valor, mostrar. - Opcion 2")
        print ("3. Mostrar Monto. - Opcion 3")
        print ("4. Modificar la cantidad cuotas que debe tener pagas para licitar. - Opcion 3")
        print ("5. Salir")
                
        print ("Elige una opcion")
             
        opcion = pedirNumeroEntero()
             
        if opcion == 1:
            actualizaValor(lista)
        elif opcion == 2:
            valorCuota(lista)
        elif opcion == 3:
            MostrarMonto(lista)
        elif opcion == 4:
            buscaPlan(lista)
        elif opcion == 5:
            salir = True
        else:
            print ("Introduce un numero entre 1 y 3")
             
        print ("Fin")

