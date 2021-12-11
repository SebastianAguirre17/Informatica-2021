# Ejercicio 4.5. 
# Definir una función denominada “es_bisiesto” que reciba por parámetro un número, 
# que representa un año, y devuelva un resultado booleano que indique si es, o no es, bisiesto. 
# Pruebe la función para múltiplos de 4, de 100 y de 400. 
# [Nota: un año es bisiesto si es un número divisible por 4, pero no es divisible por 100, excepto que
# también sea divisible por 400. Ejemplos: 1984 y 2000 son bisiestos, 1800 no es bisiesto]

def es_bisiesto(anio):
    return anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0

print(es_bisiesto(2021))
print(es_bisiesto(1984))
print(es_bisiesto(2000))
print(es_bisiesto(1800))