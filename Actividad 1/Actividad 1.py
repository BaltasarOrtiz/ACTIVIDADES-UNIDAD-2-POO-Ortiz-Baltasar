import csv

class Email:
    __idCuenta = ""
    __dominio = ""
    __tipoDeDominio = ""
    __contraseña = ""
    
    
    def __init__(self,idc,dom,tipdom,contra):
        self.__idCuenta=idc
        self.__dominio=dom
        self.__tipoDeDominio=tipdom
        self.__contraseña=contra
           
    
    def retornaEmail(self, nombre):
        #print("Estimado " + nombre + "te enviaremos un mensaje a la direccion " + self.__idCuenta +"@"+ self.__dominio +"." + self.__tipoDeDominio)
        print("Estimado " + nombre + "te enviaremos un mensaje a la direccion " + self.__idCuenta+"@"+self.__dominio+"."+self.__tipoDeDominio)
    
    def getDominio(self):
        return self.__dominio
    
    def crearCuenta(self, correo):
        adr=correo.split("@")
        tip=adr[1].split(".")
        self.idCuenta=adr[0]
        self.dominio=tip[0]
        self.tipoDeDominio=tip[1]
        
def modifica_contra(actual,oldpass):
        if actual == oldpass:
            actual=input("Ingrese nueva contraseña:")
            print("Su contraseña se modifico a: " + actual)
            return actual
        else:
            print("Contraseña incorrecta")

def recorreArchiv(direcc):
    lista=[]
    for i in range(len(direcc)):
        ad=Email("","","","")
        ad.crearCuenta(direcc[i])
        lista.append(ad) 
    busca = input("Ingrese ID a buscar:")
    b=0
    for ad in lista:
        if  ad.idCuenta == busca:
            b=1
    if b==1:
        print ("El ID ingresado se encuentra repetido")
    else: 
        print ("No se encuentra el ID ingresado")



if __name__ == "__main__":

    ##APARTADO 1
    name= input("Ingrese nombre:")
    ##p = Email()
    ##p.crearMail()
    p = Email(input("Ingrese su ID:"), input("Ingrese su dominio:"), input("Ingrese su tipo de dominio:"), input("Ingrese su contraseña:"))
    p.retornaEmail(name)
    
    ##APARTADO 2
    p.contraseña = modifica_contra(input("Ingrese contraseña actual"),p.contraseña)
    
    ##APARTADO 3
    correo = Email()
    correo.crearCuenta(input("Ingrese correo"))
    print(correo.crearCuenta())
    
    ##APARTADO 4
    corr = Email()
    corr.crearCuenta(input("Ingrese su correo:"))
    print(corr.retornarEmail())
    archi = open("direcciones.csv")
    direcciones = archi.read().split(",")
    with open("direcciones.csv","r") as archivo:
        direcciones = archivo.read().split(",")
        recorreArchiv(direcciones) 
        archivo.close()