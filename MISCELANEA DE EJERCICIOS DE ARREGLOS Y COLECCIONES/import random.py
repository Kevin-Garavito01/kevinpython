import random
from statistics import mode, median

def llenar_arreglo(n):
    arreglo = []
    for _ in range(n):
        numero = random.randint(1, 100)  # Generar número aleatorio entre 1 y 100
        arreglo.append(numero)
    return arreglo

def imprimir_arreglo(arreglo):
    print("Arreglo original:", arreglo)

def suma_arreglo(arreglo):
    suma = sum(arreglo)
    return suma

def promedio_arreglo(arreglo):
    promedio = sum(arreglo) / len(arreglo)
    return promedio

def mayor_arreglo(arreglo):
    mayor = max(arreglo)
    return mayor

def menor_arreglo(arreglo):
    menor = min(arreglo)
    return menor

def ordenar_ascendente(arreglo):
    ordenado = sorted(arreglo)
    return ordenado

def ordenar_descendente(arreglo):
    ordenado = sorted(arreglo, reverse=True)
    return ordenado

def moda_arreglo(arreglo):
    moda = mode(arreglo)
    return moda

def mediana_arreglo(arreglo):
    mediana = median(arreglo)
    return mediana

def buscar_elemento(arreglo, elemento):
    indices = []
    count = arreglo.count(elemento)
    for i, num in enumerate(arreglo):
        if num == elemento:
            indices.append(i)
    return indices, count

# Main
n = int(input("Ingrese la cantidad de elementos para el arreglo: "))
arreglo = llenar_arreglo(n)

while True:
    print("\n--- Menú ---")
    print("a. Imprimir arreglo original")
    print("b. Suma del arreglo")
    print("c. Promedio del arreglo")
    print("d. Mayor elemento del arreglo")
    print("e. Menor elemento del arreglo")
    print("f. Ordenar arreglo en forma ascendente")
    print("g. Ordenar arreglo en forma descendente")
    print("h. Moda del arreglo")
    print("i. Mediana del arreglo")
    print("j. Buscar elemento en el arreglo")
    print("q. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "a":
        imprimir_arreglo(arreglo)
    elif opcion == "b":
        suma = suma_arreglo(arreglo)
        print("La suma del arreglo es:", suma)
    elif opcion == "c":
        promedio = promedio_arreglo(arreglo)
        print("El promedio del arreglo es:", promedio)
    elif opcion == "d":
        mayor = mayor_arreglo(arreglo)
        print("El mayor elemento del arreglo es:", mayor)
    elif opcion == "e":
        menor = menor_arreglo(arreglo)
        print("El menor elemento del arreglo es:", menor)
    elif opcion == "f":
        orden_ascendente = ordenar_ascendente(arreglo)
        print("El arreglo ordenado en forma ascendente es:", orden_ascendente)
    elif opcion == "g":
        orden_descendente = ordenar_descendente(arreglo)
        print("El arreglo ordenado en forma descendente es:", orden_descendente)
    elif opcion == "h":
        moda = moda_arreglo(arreglo)
        print("La moda del arreglo es:", moda)
    elif opcion == "i":
        mediana = mediana_arreglo(arreglo)
        print("La mediana del arreglo es:", mediana)
    elif opcion == "j":
        elemento = int(input("Ingrese el elemento a buscar: "))
        indices,
