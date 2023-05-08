import random

n = int(input("Ingrese la cantidad de elementos en los arreglos: "))

arreglo1 = [random.randint(1, 100) for _ in range(n)]
arreglo2 = [random.randint(1, 100) for _ in range(n)]

suma_arreglo1 = sum(arreglo1)
suma_arreglo2 = sum(arreglo2)

if suma_arreglo1 > suma_arreglo2:
    print("El arreglo 1 tiene la suma más alta.")
elif suma_arreglo1 < suma_arreglo2:
    print("El arreglo 2 tiene la suma más alta.")
else:
    print("Ambos arreglos tienen la misma suma.")

max_arreglo1 = max(arreglo1)
max_arreglo2 = max(arreglo2)
min_arreglo1 = min(arreglo1)
min_arreglo2 = min(arreglo2)

print("El número mayor del arreglo 1 es:", max_arreglo1)
print("El número mayor del arreglo 2 es:", max_arreglo2)
print("El número menor del arreglo 1 es:", min_arreglo1)
print("El número menor del arreglo 2 es:", min_arreglo2)

promedio_conjunto = sum(arreglo1 + arreglo2) / (2 * n)
promedio_arreglo1 = sum(arreglo1) / n
promedio_arreglo2 = sum(arreglo2) / n

print("El promedio conjunto es:", promedio_conjunto)

if promedio_arreglo1 > promedio_conjunto:
    print("El promedio del arreglo 1 está por encima del promedio conjunto.")
elif promedio_arreglo1 < promedio_conjunto:
    print("El promedio del arreglo 1 está por debajo del promedio conjunto.")
else:
    print("El promedio del arreglo 1 es igual al promedio conjunto.")

if promedio_arreglo2 > promedio_conjunto:
    print("El promedio del arreglo 2 está por encima del promedio conjunto.")
elif promedio_arreglo2 < promedio_conjunto:
    print("El promedio del arreglo 2 está por debajo del promedio conjunto.")
else:
    print("El promedio del arreglo 2 es igual al promedio conjunto.")

pares_arreglo1 = sum(1 for num in arreglo1 if num % 2 == 0)
pares_arreglo2 = sum(1 for num in arreglo2 if num % 2 == 0)
impares_arreglo1 = n - pares_arreglo1
impares_arreglo2 = n - pares_arreglo2

print("El arreglo 1 tiene", pares_arreglo1, "números pares.")
print("El arreglo 2 tiene", pares_arreglo2, "números pares.")
print("El arreglo 1 tiene", impares_arreglo1, "números impares.")
print("El arreglo 2 tiene", impares_arreglo2, "números impares.")