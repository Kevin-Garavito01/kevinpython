import random

def generar_arreglo(n):
    arreglo = []
    for _ in range(n):
        arreglo.append(random.randint(1, 100))
    return arreglo

def imprimir_arreglo(arreglo):
    print("Arreglo original:", arreglo)

def suma(arreglo):
    total = sum(arreglo)
    print("Suma:", total)

def promedio(arreglo):
    avg = sum(arreglo) / len(arreglo)
    print("Promedio:", avg)

def mayor(arreglo):
    max_num = max(arreglo)
    print("Mayor:", max_num)

def menor(arreglo):
    min_num = min(arreglo)
    print("Menor:", min_num)

def ordenar_ascendente(arreglo):
    sorted_arreglo = sorted(arreglo)
    print("Arreglo ordenado ascendente:", sorted_arreglo)

def ordenar_descendente(arreglo):
    sorted_arreglo = sorted(arreglo, reverse=True)
    print("Arreglo ordenado descendente:", sorted_arreglo)

def moda(arreglo):
    counts = {}
    for num in arreglo:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    max_count = max(counts.values())
    moda_nums = [num for num, count in counts.items() if count == max_count]
    print("Moda:", moda_nums)

def mediana(arreglo):
    sorted_arreglo = sorted(arreglo)
    n = len(sorted_arreglo)
    if n % 2 == 0:
        median = (sorted_arreglo[n // 2 - 1] + sorted_arreglo[n // 2]) / 2
    else:
        median = sorted_arreglo[n // 2]
    print("Mediana:", median)

def buscar(arreglo, num):
    indices = [i for i, x in enumerate(arreglo) if x == num]
    count = len(indices)
    if count > 0:
        print("El número", num, "se encontró en la(s) posición(es):", indices)
        print("Se encontró", count, "vez(veces).")
    else:
        print("El número", num, "no se encontró en el arreglo.")


# Programa principal
n = int(input("Ingrese la cantidad de elementos para el arreglo: "))
arreglo_original = generar_arreglo(n)
arreglo = list(arreglo_original)  # Creamos una copia del arreglo original

while True:
    print("\n-- Menú --")
    print("a. Imprimir arreglo original")
    print("b. Suma")
    print("c. Promedio")
    print("d. Mayor")
    print("e. Menor")
    print("f. Ordenar ascendente")
    print("g. Ordenar descendente")
    print("h. Moda")
    print("i. Mediana")
    print("j. Buscar")
    print("q. Salir")

    opcion = input("\nIngrese una opción: ")

    if opcion == "a":
        imprimir_arreglo(arreglo_original)
    elif opcion == "b":
        suma(arreglo)
    elif opcion == "c":
        promedio(arreglo)
    elif opcion == "d":
        mayor(arreglo)
    elif opcion == "e":
        menor(arreglo)
    elif opcion == "f":
        ordenar_ascendente(arreglo)
    elif opcion == "g":
        ordenar_descendente(arreglo)
