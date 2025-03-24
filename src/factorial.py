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
        return 0
    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

#Modificaciones de que si se omite el numero como argumento, lo solicite
if len(sys.argv) == 1:  # Si el usuario no ingresó un número
    try:
        num = int(input("Ingrese un número: "))  # Pedir número manualmente
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        sys.exit(1)
else:
    try:
        num = int(sys.argv[1])  # Convertir argumento en número
    except ValueError:
        print("Error: El argumento debe ser un número entero.")
        sys.exit(1)
