from ClaseConjunto import Conjunto


if __name__ == '__main__':
    conjuntoA = Conjunto([1, 2, 3, 4])
    conjuntoB = Conjunto([4, 6, 7])
    
    print("Conjunto A =", conjuntoA)
    print("Conjunto B =", conjuntoB)

    union = conjuntoA + conjuntoB
    print("A + B = ", union)

    diferencia = conjuntoA - conjuntoB
    print("A - B = ", diferencia)

    print("A == B", conjuntoA == conjuntoB)

