# Ejercicio 2.1. Desarrolle los primeros 3 pasos de la metodología de construcción de
# programas, para el caso que se enuncia a continuación: 
# Escribir un programa que le solicite al usuario una cantidad de pesos (capital), una tasa de interés anual (tasa) y un
# número entero de años (tiempo), para mostrar, como resultado, el monto final a obtener,
# de acuerdo a la fórmula:
# C n = C x (1 + t / 100) n
# Donde C es el capital inicial, t es la tasa de interés y n es el tiempo en años.
# Identifique las variables con nombres adecuados a su significado.

def calcularInteres(capital, tasa, tiempo):
    return round((capital * (1 + tiempo / 100) ** tasa), 2)

def main():
    capital = int(input("Ingrese el capital inicial: $"))
    tasa = int(input("Ingrese la tasa anual: %"))
    tiempo = int(input("Ingrese el tiempo (en años): "))

    print(f"El monto final es: {calcularInteres(capital, tasa, tiempo)}")

main()
