def fibonacci(n):
    """
    Genera la serie de Fibonacci hasta el término n.
    """
    fibonacci_array = [0, 1]  # Inicializamos el arreglo con los dos primeros términos

    while len(str(fibonacci_array[-1])) < n:  # Verificamos que el último término tenga menos dígitos que n
        fibonacci_array.append(fibonacci_array[-1] + fibonacci_array[-2])

    return fibonacci_array


digitos = int(input("Ingrese la cantidad de dígitos para la serie de Fibonacci: "))

serie_fibonacci = fibonacci(digitos)

print("Serie de Fibonacci con", digitos, "dígitos:")
print(serie_fibonacci)
