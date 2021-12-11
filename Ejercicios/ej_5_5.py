# Ejercicio 5.5. Escribir un programa que reciba, una a una, las calificaciones del usuario,
# preguntando a cada paso si desea ingresar más notas; finalmente, el programa debe
# imprimir el promedio correspondiente y el valor de la calificación más baja.

def calificaciones():
    flag = 's'
    acum = contador = 0
    menor = 999999
    while flag == 's':
        nota = int(input("Ingrese una nota: "))
        acum = acum + nota
        if nota < menor:
            menor = nota
        contador = contador + 1
        flag = input("Presione 's' para ingresar otra nota: ")

    print("La menor nota fue:", menor)
    print("El promedio es:", acum / contador)

calificaciones()