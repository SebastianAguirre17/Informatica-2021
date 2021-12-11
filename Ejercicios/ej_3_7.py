# Ejercicio  3.7.
# Definir (y documentar) dos funciones. Una función...
# a) denominada “numero_pi”, que devuelva como resultado el valor redondeado del número PI: 3.14159.
#    Utilice el dato math.pi del módulo math y la función round(n,d)
# b) con nombre apropiado, que reciba el radio de un círculo por parámetro y devuelva como resultado el valor del área respectiva. 
#    Utilice la función del ítem a.

import math

def numero_pi():
    """Devuelva como resultado el valor redondeado del número PI: 3.14159."""
    return round(math.pi, 5)

def calc_area_circulo(radio):
    """Calcula el área de un cículo recibiendo como parámetro el radio."""
    return numero_pi() * radio ** 2

print("El valor de PI es:", numero_pi())

radio = 2 #Se debe tomar por input
print("El área: de un cículo de radio", radio, "es:", calc_area_circulo(radio))