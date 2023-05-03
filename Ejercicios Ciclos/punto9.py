x = float(input("Introduce el valor de x: "))
n = int(input("Introduce el valor de n: "))

resultado = 1

if n >= 0:
    for _ in range(n):
        resultado *= x
else:
    for _ in range(abs(n)):
        resultado /= x

print("El resultado de", x, "elevado a la", n, "es:", resultado)
