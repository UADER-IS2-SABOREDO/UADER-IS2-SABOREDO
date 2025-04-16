#!/usr/bin/python
# *-------------------------------------------------------------------------*
# * collatz.py                                                               *
# * Calcula el número de iteraciones de la conjetura de Collatz para 1-10000 *
# * y grafica los resultados                                                 *
# *-------------------------------------------------------------------------*
import os
import matplotlib.pyplot as plt
#!/usr/bin/python
# *-------------------------------------------------------------------------*
# * collatz.py                                                               *
# * Calcula el número de iteraciones de la conjetura de Collatz para 1-10000 *
# * y grafica los resultados                                                 *
# *-------------------------------------------------------------------------*
import os
import matplotlib.pyplot as plt

def collatz_steps(n):
    """Calcula cuántas iteraciones tarda un número en llegar a 1 según la conjetura de Collatz."""
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2  # Si es par, divide entre 2
        else:
            n = 3 * n + 1  # Si es impar, aplica 3n + 1
        steps += 1
    return steps

# Generar datos para los números del 1 al 10000
x_values = list(range(1, 10001))  # Números de inicio
y_values = [collatz_steps(n) for n in x_values]  # Iteraciones hasta converger

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.scatter(y_values, x_values, color='blue', s=1)  # Gráfico de dispersión
plt.xlabel("Número de Iteraciones")
plt.ylabel("Número Inicial n")
plt.title("Conjetura de Collatz: Iteraciones hasta converger")
plt.grid()

# Asegurar que la carpeta existe antes de guardar
output_dir = os.path.join(os.getcwd(), "CollatzGraficos", "collatz")
os.makedirs(output_dir, exist_ok=True)

# Guardar la imagen en la carpeta correcta
output_path = os.path.join(output_dir, "collatz_plot.png")
plt.savefig(output_path)
plt.show()

print(f"Gráfico guardado en: {output_path}")
