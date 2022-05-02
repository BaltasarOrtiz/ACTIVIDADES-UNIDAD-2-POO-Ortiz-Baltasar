from ClaseMedicamentos import medicamento
import csv 
from os import path


class ManejaMedicamento:
    __listaMedic: list[medicamento] #atributo de la clase medicamento que almacena la lista que voy a manipular


    def __init__(self):
        self.__listaMedic = self.cargarObjetoM()

    def cargarObjetoM(self):
        listaTemp = []
        archivo = open(path.dirname(__file__) + '/medicamentos.csv') #para abrir el archivo camas.csv
        reader = csv.reader(archivo, delimiter = ";")
        next(reader)
        for fila in reader:
            med = medicamento(int(fila[0]), int(fila[1]), str(fila[2]), str(fila[3]), str(fila[4]), int(fila[5]), float(fila[6]))
            listaTemp.append(med)
        
        archivo.close()
        return listaTemp


    def mostrarMedicamentos(self, idCama):
        totalAdeudado=0
        print("Medicamento/monodroga    Presentacion    Cantidad    Precio")
        for elem in self.__listaMedic:
            if elem.getIdCama() == idCama:
                print ("{}\t{}\t\t{}\t\t {}\n".format(elem.getMedic(), elem.getPresen(), elem.getCantidad(), elem.getPrecio()))
                totalAdeudado+=float(elem.getPrecio())

        print("Total Adeudado: {}".format(totalAdeudado))

    

    