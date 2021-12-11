# Ejercicio    5.1. 
# Considerando  la  siguiente  función  para  obtener  la  multiplicación  de  dos números, por sumas sucesivas:
def prod_en_sumas_for (num, cant):
    """Calcula el producto de dos números por sumas sucesivas"""
    prod = 0
    for i in range(cant):
        prod = prod + num
        print("-- [DEBUG FOR] --", num, "x", i + 1, "=", prod)
    return prod
    
# Definir (y documentar) una función denominada “prod_en_sumas” que reciba por parámetros dos números enteros y devuelva como resultado su multiplicación, 
# obtenida por sumas sucesivas mediante un ciclo indefinido. Incluya instrucciones de depuración (debugging) 
# que muestren todas las sumas que se realizan hasta obtener el resultado final. 
# Pruebe el comportamiento de la función cuando el primero de los dos números es negativo. 
# ¿Qué sucede si el número negativo es el segundo?

def prod_en_sumas (num, cant):
    prod, i = 0, 0
    while i < cant:
        prod = prod + num
        i = i + 1
        print("-- [DEBUG WHILE] --", num, "x", i, "=", prod)
    return prod

def main():
    print(prod_en_sumas_for(5, 8))
    print(prod_en_sumas(5, 8))

main()