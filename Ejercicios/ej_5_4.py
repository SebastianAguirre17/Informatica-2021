# Ejercicio 5.4. 
# Definir una función “max_com_div” que, dados por parámetro dos números n y m, 
# devuelva como resultado el Máximo Común Divisor entre ambos, implementando el
# algoritmo de Euclides. 
# Se describen a continuación los pasos de ese algoritmo matemático:
# 1. Teniendo n y m, se obtiene r, el resto de la división entera de m / n.
# 2. Si r es cero, entonces n es el MCD de los valores iniciales.
# 3. Se reemplaza m ← n, n ← r, y se vuelve al primer paso.
# Hacer un seguimiento del algoritmo implementado, para los pares de números: 
# (15,9); (9,15); (10,8) y (12,6)

def max_com_div(n, m):
    r = m % n
    while r > 0:
        m, n = n, r
        r = m % n
    return n

print(max_com_div(15, 9))
print(max_com_div(9, 15))
print(max_com_div(10, 8))
print(max_com_div(12, 6))
