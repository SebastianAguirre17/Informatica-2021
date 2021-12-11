# Ejercicio 1.9. Reescribir el programa del ejercicio 1.3 para que pida al usuario que ingrese
# la cantidad de agua inicial del tanque y la pileta, y que muestre los cambios, al transvasar
# un balde, luego otros dos, luego otros tres, luego otros cuatro y, finalmente, otros cinco

def main():
    tanque = int(input("Ingrese la cantidad de agua del tanque: "))
    pileta = int(input("Ingrese la cantidad de agua de la pileta: "))
    balde = int(input("Ingrese la cantidad de agua del balde: "))
    limit = int(input("Cantidad de baldes a cargar: "))

    for i in range(1, limit + 1):
        print('\nEl tanque contiene:', tanque, 'litros de agua y la pileta:', pileta, 'litros')
        print ('Transvasa', i, 'baldes de agua de:', balde, 'litros')
        tanque -= i * balde
        pileta += i * balde

main()