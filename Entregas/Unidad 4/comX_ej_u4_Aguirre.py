""" Módulo para completar definición de funciones. Tarea de Unidad 4 """

def suma_multi(a, b, c):
    """Recibe por parámetro tres números naturales distintos entre sí.
       Determina "el menor", "el mayor" y el restante.
       Devuelve como resultado la suma de los múltiplos del número restante,
       que se encuentren en la secuencia de enteros comprendida entre
       "el menor" y "el mayor" (incluidos)
    """
    if a > b and a > c:
        mayor = a
        if b < c:
            menor, restante = b, c
        else:
            menor, restante = c, b
    elif b > a and b > c:
        mayor = b
        if a < c:
            menor, restante = a, c
        else:
            menor, restante = c, a
    else:
        mayor = c
        if a < b:
            menor, restante = a, b
        else:
            menor, restante = b, a

    mayor = mayor + 1 
    suma = 0
    for iterador in range (menor, mayor):
        if iterador % restante == 0:
            suma = suma + iterador
    return suma


def main():
    """Pruebas de función de Unidad 4 """
    uno = 3   
    dos = 7
    tres = 21
    print ('Resultados esperados de función suma_multi()')
    print ('Suma de múltiplos con 3 7 21 es: 42')
    print ('Suma de mútliplos con 7 3 21 es: 42')
    print ('Suma de mútliplos con 3 21 7 es: 42')
    print ('Suma de mútliplos con 21 3 7 es: 42')
    print ('Suma de mútliplos con 7 21 3 es: 42')
    print ('Suma de mútliplos con 21 7 3 es: 42')
    print ('\nResultados reales de función suma_multi()')
    print ('Suma de mútliplos con',uno,dos,tres,'da =>',suma_multi(uno,dos,tres))
    print ('Suma de mútliplos con',dos,uno,tres,'da =>',suma_multi(dos,uno,tres))
    print ('Suma de mútliplos con',uno,tres,dos,'da =>',suma_multi(uno,tres,dos))
    print ('Suma de mútliplos con',tres,uno,dos,'da =>',suma_multi(tres,uno,dos))
    print ('Suma de mútliplos con',dos,tres,uno,'da =>',suma_multi(dos,tres,uno))
    print ('Suma de mútliplos con',tres,dos,uno,'da =>',suma_multi(tres,dos,uno))
    print ('\nResultado esperado de función suma_multi() con datos erróneos')
    print ('Suma de mútliplos con 3 3 3 es: 3')
    print ('\nResultado real de función suma_multi() con datos erróneos')
    print ('Suma de mútliplos con',uno,uno,uno,'da =>',suma_multi(uno,uno,uno))

# help(suma_multi)
main()
