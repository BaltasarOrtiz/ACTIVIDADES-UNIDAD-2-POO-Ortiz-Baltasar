#3.1.        Mostrar para cada variable el día y hora de menor y mayor valor.
def varMaxMin(lista):
    #TEMPERATURA
    maxTemp = lista[0][0].getTemp()
    minTemp = lista[0][0].getTemp()
    diaTmax = 0
    horaTmax = 0
    diaTmin = 0
    horaTmin = 0
    
    #HUMEDAD
    maxHum = lista[0][0].getHum()
    minHum = lista[0][0].getHum()
    diaHmax = 0
    horaHmax = 0
    diaHmin = 0
    horaHmin = 0
    
    #PRESION
    maxPres = lista[0][0].getPres()
    minPres = lista[0][0].getPres()
    diaPmax = 0
    horaPmax = 0
    diaPmin = 0
    horaPmin = 0
        
    for i in range(30):
        for p in range(24):
            #TEMPERATURA
            if(lista[i][p].getTemp()>maxTemp):
                maxTemp = lista[i][p].getTemp()
                diaTmax = i+1
                horaTmax = p
                
            if(lista[i][p].getTemp()<minTemp):
                minTemp = lista[i][p].getTemp()
                diaTmin = i+1
                horaTmin = p
                    
            #HUMEDAD
            if(lista[i][p].getHum()>maxHum):
                maxHum = lista[i][p].getHum()
                diaHmax = i+1
                horaHmax = p
                
            if(lista[i][p].getHum()<minHum):
                minHum = lista[i][p].getHum()
                diaHmin = i+1
                horaHmin = p
                
            #PRESION
            if(lista[i][p].getPres()>maxPres):
                maxPres = lista[i][p].getPres()
                diaPmax = i+1
                horaPmax = p
                
            if(lista[i][p].getPres()<minPres):
                minPres = lista[i][p].getPres()
                diaPmin = i+1
                horaPmin = p
        
    print("\n")    
    print("TEMPERATURA")
    print("Valor Maximo - Dia: {} Hora: {}".format(diaTmax, horaTmax))
    print("Valor Minimo - Dia: {} Hora: {}".format(diaTmin, horaTmin))
    print("\n")
    print("HUMEDAD")
    print("Valor Maximo - Dia: {} Hora: {}".format(diaHmax, horaHmax))
    print("Valor Minimo - Dia: {} Hora: {}".format(diaHmin, horaHmin))
    print("\n")
    print("PRESION")
    print("Valor Maximo - Dia: {} Hora: {}".format(diaPmax, horaPmax))
    print("Valor Minimo - Dia: {} Hora: {}".format(diaPmin, horaPmin))

#3.2.        Indicar la temperatura promedio mensual por cada hora.
def promedioT(lista):
    for p in range(24):
        acum=0
        for i in range(30):
            acum += float(lista[i][p].getTemp())
        print("Hora: {}  Promedio: {:.2f}".format(p, acum/30))

#3.3.        Dado un número de día listar los valores de las tres variables para cada hora del día dado. El listado debe tener el siguiente formato.
def listado(lista, dia):
    print("Hora Temperatura Humedad Presion")
    for j in range(24):
        print("{} {} {} {}".format(j, lista[dia-1][j].getTemp(), lista[dia-1][j].getHum(), lista[dia-1][j].getPres()))
     

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
        print ("1. Consultar Valores Maximos y Minimos de Variables (Dia y Hora) - Opcion 1")
        print ("2. Promedio de Temperaturas Mensual - Opcion 2")
        print ("3. Listado - Opcion 3")
        print ("4. Salir")
                
        print ("Elige una opcion")
             
        opcion = pedirNumeroEntero()
             
        if opcion == 1:
            varMaxMin(lista)
        elif opcion == 2:
            promedioT(lista)
        elif opcion == 3:
            dia = int(input("Ingrese el dia a imprimir el listado: "))
            print(listado(lista, dia))
        elif opcion == 4:
            salir = True
        else:
            print ("Introduce un numero entre 1 y 3")
             
        print ("Fin")
          
    



    




