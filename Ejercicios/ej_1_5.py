#Ejercicio 1.5. Implementar algoritmos que permitan:
#    a) Obtener el perímetro de un rectángulo, dada su base y su altura.
#    b) Obtener el área de un rectángulo, dada su base y su altura.
#    c) Dados dos números n1 y n2, indicar la suma, resta, multiplicación, división y división
#    entera de ambos. Analizar el resultado, con los números: 5 y 2 ; 2 y 5 ; 5 y 0.

def cPerimetro(base, alt):
    if base > 0 and alt > 0:
        return base * 2 + alt * 2
    else:
        return "ERROR! Debe ingresar valores diferentes de cero."

def cArea(base, alt):
    if base > 0 and alt > 0:
        return base * alt  
    else:
        return "ERROR! Debe ingresar valores diferentes de cero."

def suma(n1,n2):
    return n1 + n2

def resta(n1, n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

def division(n1, n2):
    if n2 != 0:
        return n1 / n1
    else:
        return "ERROR! No se puede dividir por cero"

print(f'Obtener el perímetro de un rectángulo de base 5 y altura 2 es: {cPerimetro(5, 2)}')
print(f'Obtener el perímetro de un rectángulo de base 2 y altura 5 es: {cPerimetro(2, 5)}')
print(f'Obtener el perímetro de un rectángulo de base 5 y altura 0 es: {cPerimetro(5, 0)}')

print("*******************************************************")

print(f'Obtener el área de un rectángulo de base 5 y altura 2 es: {cArea(5, 2)}')
print(f'Obtener el área de un rectángulo de base 2 y altura 5 es: {cArea(2, 5)}')
print(f'Obtener el área de un rectángulo de base 5 y altura 0 es: {cArea(5, 0)}')

print("*******************************************************")

print("Suma")
print(f"5 + 2 = {suma(5, 2)}")
print(f"2 + 5 = {suma(2, 5)}")
print(f"5 + 0 = {suma(5, 0)}")

print("*******************************************************")

print("Resta")
print(f"5 + 2 = {resta(5, 2)}")
print(f"2 + 5 = {resta(2, 5)}")
print(f"5 + 0 = {resta(5, 0)}")

print("*******************************************************")

print("Multiplicación")
print(f"5 + 2 = {multi(5, 2)}")
print(f"2 + 5 = {multi(2, 5)}")
print(f"5 + 0 = {multi(5, 0)}")

print("*******************************************************")

print("División")
print(f"5 + 2 = {division(5, 2)}")
print(f"2 + 5 = {division(2, 5)}")
print(f"5 + 0 = {division(5, 0)}")