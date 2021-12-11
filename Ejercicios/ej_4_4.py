# Ejercicio 4.4. Escribir un programa que pida al usuario que ingrese dos números naturales, n1 y n2, e imprima en pantalla la secuencia de enteros 
# comprendida  entre n1 y n2 (incluidos) con la siguiente particularidad: 
# si el número es múltiplo de 3, en lugar del número debe imprimir “TRES”, 
# si es múltiplo de 5, en vez del número debe imprimir “CINCO” y  
# si es múltiplo de 3 y de 5, en lugar del número debe imprimir “TRES Y CINCO”.

# def mostrar_secuencia(n1, n2):
#     for n in range (n1, n2 + 1):
#         if n % 3 == 0 and n % 5 == 0:
#             print("TRES Y CINCO")
#         elif n % 3 == 0:
#             print("TRES")
#         elif n % 5 == 0:
#             print("CINCO")
#         else:
#             print(n)

def mostrar_secuencia(n1, n2):
    for n in range (n1, n2 + 1):
        if n % 3 == 0:
            if n % 5 == 0:
                print("TRES Y CINCO")
            else:
                print("TRES")
        elif n % 5 == 0:
            print("CINCO")
        else:
            print(n)

def main():
    n1 = int(input("Ingrese el primer número entero: "))
    n2 = int(input("Ingrese el segundo número entero: "))

    mostrar_secuencia(n1, n2)  

main()