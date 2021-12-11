# Ejercicio 4.6. Definir una función “cant_dias_mes” que, dados por parámetro dos números,
# que representan el mes y el año, devuelva como resultado la cantidad de días
# correspondientes al mes. En la definición se debe invocar a la función del enunciado 4.5.

import ej_4_5

def cant_dias_mes(mes, anio):
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        return 31
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return 30
    elif mes == 2 and ej_4_5.es_bisiesto(anio):
        return 29
    elif mes == 2 and not ej_4_5.es_bisiesto(anio):
        return 28
    else:
        return 0

# print(cant_dias_mes(12, 2024))