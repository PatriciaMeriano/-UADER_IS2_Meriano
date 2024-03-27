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
    if desde <= 0:
        desde = 1
    if hasta <= 0:
        hasta = 60

    for num in range(desde, hasta + 1):
        print("Factorial de", num, "! es", factorial(num))

if len(sys.argv) > 1:
    rango = sys.argv[1]
    if '-' in rango:
        desde, hasta = map(int, rango.split('-'))
    else:
        desde, hasta = 1, int(rango)
else:
    rango = input("Por favor, ingrese un rango de números en el formato 'desde-hasta' o '-hasta' para calcular sus factoriales: ")
    if '-' in rango:
        desde, hasta = map(int, rango.split('-'))
    else:
        desde, hasta = 1, int(rango)

calcular_factoriales(desde, hasta)
