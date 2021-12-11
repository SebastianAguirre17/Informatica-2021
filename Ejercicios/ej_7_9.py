# Ejercicio 7.9. 
# Definirdos funciones. Una funcióndenominada...
# a) ‘interseccion’ que reciba por parámetro dos listas,que representan conjuntos, y devuelva 
# como resultado otra lista que incluya, sin repeticiones, los elementos comunes a 
# ambas listaspasadas como argumentos.
# b) ‘union’ que reciba por parámetro dos listas, que representan conjuntos, y devuelva como
# resultado otra lista que incluya, sin repeticiones, los elementos que pertenezcan
# a una u otra listapasadas como argumentos.

def interseccion(lis_a, lis_b):
    """ Reciba por parámetro dos listas, que representan conjuntos, y devuelva 
        como resultado otra lista que incluya, sin repeticiones, los elementos comunes a 
        ambas listaspasadas como argumentos 
    """
    result = []
    for elem in lis_a:
        if elem in lis_b and elem not in result:
            result.append(elem)
            
    return result

def union(lis_a, lis_b):
    """ Reciba por parámetro dos listas, que representan conjuntos, y devuelva como
        resultado otra lista que incluya, sin repeticiones, los elementos que pertenezcan
        a una u otra lista pasadas como argumentos 
    """
    result = []
    for elem in lis_a:
        result.append(elem)
    for elem in lis_b:
        if elem not in result:
            result.append(elem)
        
    return result

def main():
    lis_a = [1, 'b', 8, 5, 'j', 3, 4, 'd', 3]
    lis_b = ['a', 4, 'c', 'd', 3, 8]
    
    print(interseccion(lis_a, lis_b))
    print(union(lis_a, lis_b))
    
main()