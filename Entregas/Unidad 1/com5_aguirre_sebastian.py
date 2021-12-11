# Ejercicio:
# 
# Jimena vende sombreros. Inicialmente tiene 1000 pesos y una cierta cantidad de sombreros, que pone a la venta a un determinado precio.
# 
# Definir una función main() que exprese la situación que se describe a continuación, a través de asignaciones sobre cuatro variables cuyos identificadores son:
#     dinero (representa la cantidad de dinero que tiene en caja), 
#     sombreros (representa la cantidad de sombreros disponibles para la venta), 
#     precio (representa el precio de venta de cada sombrero) y 
#     cant_venta (representa la cantidad de sombreros que vende en cada operación de venta):
# 
# -   Escriba instrucciones que pidan al usuario que ingrese la cantidad inicial de sombreros (por ejemplo: 13 o 16 o 19) 
#     y el precio de venta de cada unidad (por ejemplo, 500 pesos). 
#     Agregue una instrucción que muestre en pantalla con descripciones expresivas, los valores iniciales de las variables dinero y sombreros.
# 
# -   Agregue instrucciones que describan las variaciones que resultan de la venta de la tercera parte (entera) de los sombreros disponibles para la venta. 
#     Luego muestre en pantalla las consecuencias de la venta: cuántos sombreros se vendieron y a qué precio; cuántos sombreros quedan y cuánto dinero hay en caja.
# 
# -   Agregue instrucciones para representar y mostrar la venta de la mitad (entera) de sombreros restantes, con las respectivas variaciones sobre las variables: 
#     cuántos sombreros se vendieron y a qué precio, finalmente, cuántos sombreros quedaron y cuánto dinero en caja.
# 
# Por último, invoque (llame para su ejecución) a la función y compruebe su comportamiento correcto, 
# ingresando los valores descriptos como ejemplo entre paréntesis y verificando los resultados mostrados en pantalla.

def saludo():
    print("*******************************")
    print("***** SOMBREROS DE JIMENA *****")
    print("*******************************\n")

def getInt(msg):
    try:
        aux = int(input(msg))
        return aux
    except ValueError:
        print("ERROR! Ingrese un valor numérico.\n")
        return 0

def showInfo(dinero, sombreros, precio):
    print(f"\nStock de Sombreros: {sombreros}")
    print(f"Dinero en caja: ${dinero}")
    print(f"Precio por unidad: ${precio}\n")

def mostrarVenta(cant_venta, precio, stock, dinero):
    print(f"Se vendieron {cant_venta} sobreros a un precio de ${precio}")
    print(f"Total de la venta: ${cant_venta * precio}")
    print(f"Dinero en caja: ${dinero}")
    print(f"Stock de Sombreros: {stock}\n")

def main():
    dinero = 1000
    sombreros = 0
    precio = 0
    cant_venta = 0
    
    saludo()

    while sombreros <= 0:
        sombreros = getInt("Ingrese la cantidad inicial de sombreros: ")
        if sombreros <= 0:
            print("Debe Ingresar un número positivo.")
    
    while precio <= 0: 
        precio = getInt("Ingrese el precio de cada sombrero: $")
        if precio <= 0:
            print("Debe Ingresar un número positivo.")

    showInfo(dinero, sombreros, precio)

    #Vender 1/3
    if sombreros > 3:
        print("Vendo 1 tercio del stock.\n")
        cant_venta = sombreros // 3
        dinero += cant_venta * precio
        sombreros -= cant_venta
        mostrarVenta(cant_venta, precio, sombreros, dinero)
    else:
        print("No hay suficientes sombreros para vender 1 tercio del total\n")
    
    #Vender 1/2
    if sombreros > 2:
        print("Vendo la mitad del stock.\n")
        cant_venta = sombreros // 2
        dinero += cant_venta * precio
        sombreros -= cant_venta

        mostrarVenta(cant_venta, precio,sombreros, dinero)
    else:
        print("No hay suficientes sombreros para la venta especificada.\n")
    
# Ejecuto main    
main()

