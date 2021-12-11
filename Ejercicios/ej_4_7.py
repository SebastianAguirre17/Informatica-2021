# Ejercicio 4.7. Definir una función “fecha_valida” que, dada por parámetros una fecha en
# números (día, mes, año), devuelva un resultado booleano que indique si es válida o no.
# ¿Qué función debería invocar?

import ej_4_6

def fecha_valida(dia, mes, anio):
    return ej_4_6.cant_dias_mes(mes, anio) != 0 and dia <= ej_4_6.cant_dias_mes(mes, anio)

print(fecha_valida(29,2,2021))