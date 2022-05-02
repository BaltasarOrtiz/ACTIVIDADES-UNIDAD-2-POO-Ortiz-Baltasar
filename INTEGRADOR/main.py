from ManejadorCama import ManejaCama
from ManejadorMedicamento import ManejaMedicamento

if __name__ == '__main__':
    #generar objetos de camas
    manC = ManejaCama()
    manC.cargarObjetoC()
    #generar objetos de medicamento
    manM = ManejaMedicamento()
    manM.cargarObjetoM()

    
    #apartado 3
    pos = manC.buscaCama(input("Ingrese el apellido y nombre del paciente (Ejemplo: Ortiz, Juan): "))
    if pos != -1:
        manC.mostrarDatosPaciente(pos)
        idCama=manC.obtenerIdCama(pos)
        manM.mostrarMedicamentos(idCama)
    else: 
        print("Nombre del paciente incorrecto")
    

    #apartado 4
    manC.Diagnostico(input("Ingrese el diagnostico del paciente: "))

