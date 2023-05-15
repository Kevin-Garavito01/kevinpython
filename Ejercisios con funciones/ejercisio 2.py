import random

def generar_arreglo(n):
    arreglo = []
    for _ in range(n):
        arreglo.append(random.randint(1, 100))
    return arreglo

def comparar_arreglos(arreglo1, arreglo2):
    # a. Comparar la suma de los arreglos
    suma_arreglo1 = sum(arreglo1)
    suma_arreglo2 = sum(arreglo2)

    print("Suma del arreglo 1:", suma_arreglo1)
    print("Suma del arreglo 2:", suma_arreglo2)

    if suma_arreglo1 > suma_arreglo2:
        print("El arreglo 1 tiene la suma más alta.")
    elif suma_arreglo1 < suma_arreglo2:
        print("El arreglo 2 tiene la suma más alta.")
    else:
        print("Ambos arreglos tienen la misma suma.")

    # b. Encontrar el número mayor de los arreglos
    max_arreglo1 = max(arreglo1)
    max_arreglo2 = max(arreglo2)

    print("Número mayor del arreglo 1:", max_arreglo1)
    print("Número mayor del arreglo 2:", max_arreglo2)

    if max_arreglo1 > max_arreglo2:
        print("El arreglo 1 tiene el número mayor.")
    elif max_arreglo1 < max_arreglo2:
        print("El arreglo 2 tiene el número mayor.")
    else:
        print("Ambos arreglos tienen el mismo número mayor.")

    # c. Encontrar el número menor de los arreglos
    min_arreglo1 = min(arreglo1)
    min_arreglo2 = min(arreglo2)

    print("Número menor del arreglo 1:", min_arreglo1)
    print("Número menor del arreglo 2:", min_arreglo2)

    if min_arreglo1 < min_arreglo2:
        print("El arreglo 1 tiene el número menor.")
    elif min_arreglo1 > min_arreglo2:
        print("El arreglo 2 tiene el número menor.")
    else:
        print("Ambos arreglos tienen el mismo número menor.")

    # d. Calcular el promedio conjunto
    promedio_conjunto = (sum(arreglo1) + sum(arreglo2)) / (len(arreglo1) + len(arreglo2))
    print("Promedio conjunto:", promedio_conjunto)

    # e. Comparar los promedios individuales con el promedio conjunto
    promedio_arreglo1 = sum(arreglo1) / len(arreglo1)
    promedio_arreglo2 = sum(arreglo2) / len(arreglo2)

    print("Promedio del arreglo 1:", promedio_arreglo1)
    print("Promedio del arreglo 2:", promedio_arreglo2)

    if promedio_arreglo1 > promedio_conjunto and promedio_arreglo2 > promedio_conjunto:
        print("Ambos arreglos están por encima del promedio conjunto.")
    elif promedio_arreglo1 < promedio_conjunto and promedio_arreglo2 < promedio_conjunto:
        print("Ambos arreglos están por debajo del promedio conjunto.")
    else:
        print("Al menos uno de los arreglos está por encima y el otro está por debajo del promedio conjunto.")

    # f. Calcular la cantidad de números pares en cada arreglo
    pares_arreglo1 = sum(1 for num in arreglo1 if num % 2 == 0)
   

