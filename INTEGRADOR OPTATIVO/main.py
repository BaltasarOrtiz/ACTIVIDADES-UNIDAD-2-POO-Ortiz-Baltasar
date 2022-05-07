from ManejadorIntegrantesProyecto import ManejIntegrante
from ManejadorProyecto import ManejProyecto


if __name__ == '__main__':
    #generar objetos de integrantes
    manInteg = ManejIntegrante()
    manInteg.cargarobjetos()
    #generar objetos de proyectos
    manProyect = ManejProyecto()
    manProyect.cargarobjetos()

    #apartado 3
    ListaIdsProy = manProyect.obteneridproyecto()
    for i in range(len(ListaIdsProy)):
        total = manInteg.calcularpuntaje(ListaIdsProy[i])
        print("Puntaje total en el main: ", total)
        print("\n")
        manProyect.guardartotal(i, total)

    #apartado 4
    manProyect.mostrarordenado()
