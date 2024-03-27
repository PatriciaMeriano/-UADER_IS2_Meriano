#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
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

def calcular_factoriales(rango):
    desde, hasta = map(int, rango.split('-'))
    if desde > hasta:
        print("El primer número del rango debe ser menor o igual que el segundo número.")
        return

    for num in range(desde, hasta + 1):
        print("Factorial de", num, "! es", factorial(num))

if len(sys.argv) > 1:
    rango = sys.argv[1]
else:
    rango = input("Por favor, ingrese un rango de números en el formato 'desde-hasta' para calcular sus factoriales: ")

calcular_factoriales(rango)
