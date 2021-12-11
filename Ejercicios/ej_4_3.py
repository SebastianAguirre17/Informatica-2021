# Ejercicio 4.3. Definir una función denominada “mayor_de_3” que devuelva como resultado
# el mayor de tres números dados por parámetro. Pruebe la función con 6 ternas de valores

def mayor_de_3(a, b, c):
    """ Devuelva como el mayor de tres números dados por parámetro. """
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
        

print(mayor_de_3(2, 3, 6))
print(mayor_de_3(3, 0, 6))
print(mayor_de_3(-5, -6, 5))
print(mayor_de_3(-2, -4, 0))
print(mayor_de_3(2, 3, 6))
print(mayor_de_3(1, 8, 6))