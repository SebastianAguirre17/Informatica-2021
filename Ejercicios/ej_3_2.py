# Ejercicio  3.2. Definir (y documentar) con un nombre apropiado, una función:
# a) Que calcule e imprima el valor de cualquier número n elevado al cubo.
# b) Modificarla solución anterior, para que la función calcule cualquier potencia dada, 
#    de cualquier número dado y devuelva el resultado al programa principal.
# Pruebe  la función con valores: 20, 21, 22, 23 y 360.5. 
# Consultar la documentación mediante la función help() provista  por  Python y  verificar: 
# ¿todavía  describe  adecuadamentelo que hace la función?
# ¿el nombre de la función sigue siendo apropiado?


def calculaPotencia(num, potencia):
    return num ** potencia

def mostrarPotencia(num, potencia):
    result = calculaPotencia(num, potencia)
    print(f"{num} elevado a la {potencia} es: {result}")
    return result
