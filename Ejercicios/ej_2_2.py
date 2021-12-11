# Ejercicio 2.2. Ídem anterior: Escribir un programa Python que le solicite al usuario que
# ingrese el costo (en pesos) de cada uno de los siguientes dispositivos de almacenamiento:
#  Memoria RAM de 4GB para PC
#  Pendrive 16 GB
#  Disco rígido interno 2 TB
# Considerando que en el Sistema Internacional de Unidades (Decimal) un Terabyte (TB)
# equivale a 1012 bytes y un Gigabyte (GB) equivale a 109 bytes, el programa deberá informar
# en la pantalla:
# a) ¿Cuánto costaría almacenar 1 GB en cada uno de esos dispositivos?
# b) ¿Cuánto más cara (en forma relativa) es la memoria RAM que el pendrive?
# c) ¿Cuánto más cara (en forma relativa) es la memoria RAM que el disco rígido?
# d) ¿Cuánto más caro (en forma relativa) es el pendrive que el disco rígido?

def calcularCostoDelGB(gb, precio):
    return round(precio / gb, 2)

def tbToGb(tb):
    return tb * 1024

def calcularPorcentaje(mayor, menor):
    return 100 * menor / mayor 

ram = 4
pendrive = 16
disco = 2048

precioRam = 2000
precioPendrive = 4000
precioDisco = 20000

print(f"Almacenar 1 BG en RAM cuesta: ${calcularCostoDelGB(ram, precioRam)}")
print(f"Almacenar 1 BG en Pendrive cuesta: ${calcularCostoDelGB(pendrive, precioPendrive)}")
print(f"Almacenar 1 BG en Disco cuesta: ${calcularCostoDelGB(disco, precioDisco)}")

