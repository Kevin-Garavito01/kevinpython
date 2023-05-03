N = int(input("Introduce el número N: "))

multiplos = []

for i in range(1, N+1):
    if i % 5 == 0:
        multiplos.append(i)

print("Los múltiplos de 5 comprendidos entre 1 y", N, "son:")
print(multiplos)
