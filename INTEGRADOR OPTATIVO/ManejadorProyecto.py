from ClaseProyectos import Proyecto
import csv


class ManejProyecto:
    __lista: list[Proyecto]


    def __init__(self):
        self.__lista = self.cargarobjetos()

    def cargarobjetos(self):
        listatemp = []
        archivo = open("proyectos.csv")
        reader = csv.reader(archivo, delimiter = ";")
        next(reader)
        for fila in reader:
            p = Proyecto(str(fila[0]), str(fila[1]), str(fila[2]))
            listatemp.append(p)

        return listatemp
        archivo.close()


    def obteneridproyecto(self):
        listaIds = []
        for elem in self.__lista:
            listaIds.append(elem.getId())

        return listaIds

    def guardartotal(self, pos, tot):
        self.__lista[pos].guardarPuntaje(tot)


    def mostrarordenado(self):
        listaordenada = sorted(self.__lista, reverse=True)
        for elem in listaordenada:
            print("Proyecto: {}   Titulo: {}   Puntaje Total: {}   Palabras Clave: {}".format(elem.getId(), elem.getTitulo(), elem.getpuntajetotal(), elem.getPalabraClave()))

