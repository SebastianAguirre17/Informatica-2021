#Ejercicio 1.8. Implementar algoritmos que resuelvan los siguientes problemas:
#    a) Dado un número natural n, imprimir su tabla de multiplicar desde 0 hasta n.
#    b) Dado un número natural n, imprimir la suma total de los naturales de 1 a n

def imprimirTablas(n):
    limit = n + 1
    for i in range (limit):
        print(f"{n} x {i} = {n * i}")

aux = int(input("Numero: "))
imprimirTablas(aux)
