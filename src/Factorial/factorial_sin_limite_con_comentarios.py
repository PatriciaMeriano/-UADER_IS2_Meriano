import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return None
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while num > 1: 
            fact *= num 
            num -= 1
        return fact 

def calcular_factoriales(desde, hasta):
    # Verifica si el límite superior del rango es menor o igual a cero
    # Si lo es, establece el límite superior en 60
    if hasta <= 0:
        hasta = 60

    # Calcula y muestra los factoriales para cada número en el rango [desde, hasta]
    for num in range(desde, hasta + 1):
        print("Factorial de", num, "! es", factorial(num))

# Verifica si se proporcionan argumentos al ejecutar el script
if len(sys.argv) > 1:
    rango = sys.argv[1]
    # Si hay un guion en el rango, divide la cadena en dos partes y convierte a enteros
    if '-' in rango:
        desde, hasta = map(int, rango.split('-'))
    else:
        # Si no hay guion, asume que se proporciona solo un número como límite superior
        desde, hasta = 1, int(rango)
else:
    # Si no se proporcionan argumentos, solicita al usuario que ingrese un rango manualmente
    rango = input("Por favor, ingrese un rango de números en el formato 'desde-hasta' o '-hasta' para calcular sus factoriales: ")
    # Si hay un guion en el rango, divide la cadena en dos partes y convierte a enteros
    if '-' in rango:
        desde, hasta = map(int, rango.split('-'))
    else:
        # Si no hay guion, asume que se proporciona solo un número como límite superior
        desde, hasta = 1, int(rango)

# Llama a la función calcular_factoriales con los límites determinados
calcular_factoriales(desde, hasta)
