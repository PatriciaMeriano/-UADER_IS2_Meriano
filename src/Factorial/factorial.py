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

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

if len(sys.argv) < 2:  
    num_input = input("Por favor, ingrese un número para calcular su factorial: ")
    try:
        num = int(num_input)
    except ValueError:
        print("¡Debe ingresar un número válido!")
        sys.exit(1)
else:
    num = int(sys.argv[1])