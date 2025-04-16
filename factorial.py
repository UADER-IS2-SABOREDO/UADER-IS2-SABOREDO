#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(n):
    """ Calcula el factorial de un número n de forma recursiva. """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    # Si no hay argumento, pedir el número o rango manualmente
    if len(sys.argv) != 2:
        entrada = input("Ingrese un número o un rango (ej. 4-8, -10, 20-): ")
    else:
        entrada = sys.argv[1]

    try:
        if "-" in entrada:
            partes = entrada.split("-")

            if entrada.startswith("-"):  # Caso "-10" → de 1 a 10
                hasta = int(partes[1])
                desde = 1
            elif entrada.endswith("-"):  # Caso "20-" → de 20 a 60
                desde = int(partes[0])
                hasta = 60
            else:  # Caso normal "4-8"
                desde, hasta = map(int, partes)

            if desde > hasta:
                print("Error: El primer número debe ser menor o igual al segundo.")
            else:
                for i in range(desde, hasta + 1):
                    print(f"Factorial de {i} es {factorial(i)}")
        else:
            num = int(entrada)
            print(f"Factorial de {num} es {factorial(num)}")

    except ValueError:
        print("Error: Entrada no válida. Debes ingresar un número o un rango válido.")
