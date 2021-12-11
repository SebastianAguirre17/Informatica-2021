# Ejercicio 4.2. Definir y documentar una función denominada “val_abs”, que reciba un
# número por parámetro y devuelva como resultado su valor absoluto. 
# [No utilizar la función abs () provista por Python]

# Forma corta
# def val_abs(numero):
#     return numero if numero > 0 else numero * -1

def val_abs(numero):
    """ Reciba un número por parámetro y devuelva como resultado su valor absoluto. """
    if numero > 0:
        return numero
    else:
        return numero * -1

print(val_abs(0))
print(val_abs(-7))
print(val_abs(7))