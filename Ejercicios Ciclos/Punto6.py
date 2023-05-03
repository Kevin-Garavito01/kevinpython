maximo = 0

while True:
    numero = int(input("Introduce un número: "))
    
    if numero < 0:
        break
    
    if numero > maximo:
        maximo = numero

print("El máximo número positivo introducido es:", maximo)



