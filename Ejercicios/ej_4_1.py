# Ejercicio 4.1. 
# Definir y documentar : …
# a) una función denominada “es_par” que, dado un número entero por parámetro,
# devuelva un valor booleano que indique si es par, o no. Dé un ejemplo de invocación.
# b) Modificar la solución anterior, para que devuelva como resultado “S” si es par, “N” si
# es impar o “0” si es cero. Consulte la documentación mediante la función help ()

def es_par(numero):
    return numero % 2 == 0

def es_par_o_cero(numero):
    if numero == 0:
        return 0
    elif numero % 2 == 0:
        return 'S'
    else:
        return 'N'


print(es_par_o_cero(0))