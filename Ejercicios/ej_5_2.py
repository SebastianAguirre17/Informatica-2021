# Ejercicio  5.2. 
# Escribir un programa:
# a) que contenga una contraseña de 4 caracteres inventada, que le pregunte al usuario la contraseña y 
# no le permita continuar hasta que la haya ingresado correctamente.
# b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos.  
# Al finalizar, deberá imprimir en pantalla “Eureka” si acertó la clave o, en caso contrario, “Clave incorrecta” y la cantidad de intentos fallidos.
# c) Modificar el programa anterior para que después de cada intento agregue una pausa cada vez mayor, 
# utilizando la función  time.sleep(...)del módulo time

def adivina_contrasenia(password_secret, intentos):
    while intentos > 0:
        password = input("Ingrese la contraseña super secreta: ")
        if password == password_secret:
            print("Eureka :D")   
            return
        else:
            intentos = intentos - 1
            print("Clave incorrecta! Te quedan", intentos, "intentos")
        
def main(): 
    adivina_contrasenia("1111", 5)

main()