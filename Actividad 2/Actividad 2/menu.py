

def llamarMenu(lista):
        
    salir = False
    opcion = 0
        
    numiD = int(input("Ingrese id del viajero, 0 para terminar "))
    while numiD != 0:
            
        b = busqueda(lista, numiD)
        print("Esta es la posicion"+str(b))
        while not salir:
                
            print ("1. Consultar Cantidad de Millas - Opcion 1")
            print ("2. Acumular Millas - Opcion 2")
            print ("3. Canjear Millas - Opcion 3")
            print ("4. Salir")
                
            print ("Elige una opcion")
             
            opcion = pedirNumeroEntero()
             
            if opcion == 1:
                print ("Consultar Cantidad de Millas ")
                print(lista[b].cantidadTotalMillas())
            elif opcion == 2:
                print ("Acumular Millas ")
                print(lista[b].acumularMillas())
            elif opcion == 3:
                print("Canjear Millas ")
                print(lista[b].canjearMillas())
            elif opcion == 4:
                salir = True
            else:
                print ("Introduce un numero entre 1 y 3")
             
        print ("Fin")
          
    
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

def busqueda(lista, numiD):
    for i in range(len(lista)):
        if (lista[i].getNumViajero() == numiD):
            return i
        