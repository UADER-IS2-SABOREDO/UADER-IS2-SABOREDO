#!/usr/bin/python
# *-------------------------------------------------------------------------*
# * factorial_OOP.py                                                         *
# * Calcula el factorial de un número usando Programación Orientada a Objetos *
# * Basado en código original de Dr. P.E. Colla (c) 2022                     *
# * Creative Commons                                                        *
# *-------------------------------------------------------------------------*

import sys

class Factorial:
    """Clase para calcular el factorial de un número."""

    def __init__(self, num):
        """Constructor que recibe el número a calcular."""
        self.num = num

    def calcular(self):
        """Calcula el factorial de un número usando la misma lógica del código original."""
        if self.num < 0:
            print("Factorial de un número negativo no existe")
            return 0
        elif self.num == 0:
            return 1
        
        fact = 1
        while self.num > 1:
            fact *= self.num
            self.num -= 1
        return fact 

# Manejo de argumentos desde la línea de comandos
if len(sys.argv) == 1:  # Si no se ingresó argumento, pedir manualmente
    try:
        num = int(input("Ingrese un número: "))
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        sys.exit(1)
else:
    try:
        num = int(sys.argv[1])
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")
        sys.exit(1)

# Crear instancia de Factorial y ejecutar cálculo
factorial_obj = Factorial(num)
print(f"Factorial {num}! es {factorial_obj.calcular()}")
