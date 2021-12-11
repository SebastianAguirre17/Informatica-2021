
def triangular_formula(numero_natural):
    """ Recibe por parámetro un número natural n, y muestre en pantalla el número triangular de orden n que resulta de aplicar la ecuación  n ∗ ( n + 1 ) / 2. """
    numero_triangular = numero_natural * (numero_natural + 1) // 2
    print("\nEl número trinagular de orden", numero_natural, "es:", numero_triangular, "\nPara calcularlo se aplicó la fórmula: ", numero_natural, " * (", numero_natural, " + 1) / 2")

def suma_n(numero_natural):
    """ Recibe por parámetro un número natural y devuelva como resultado la suma de naturales desde 1 hasta num (incluido). """
    suma_n = 0
    for i in range (1, numero_natural + 1):
        suma_n = suma_n + i
    return suma_n

def main():
    """ Solicita el ingreso por teclado de un número natural. 
        Con el valor ingresado invoca a la función triangular_formula.
        Muestra el resultado de invocar a función suma_n, pasándole como parámetro el número ingresado por el usuario.
    """
    nro = int(input("Ingrese por teclado un número natural: "))
    triangular_formula(nro)
    sumatoria = suma_n(nro)
    print("\nEl valor de la variable sumatoria es:", sumatoria, "\n")

main()
