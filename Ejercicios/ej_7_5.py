# Ejercicio 7.5. 
# Definir una función ‘producto_escalar’, que reciba como parámetros dos
# tuplas, que representan vectores de igual dimensión, y devuelva como resultado el valor de
# su producto escalar. 
# [El producto escalar de los vectores (u1, u2, u3) y (v1, v2, v3), se puede
# calcular como el valor numérico que resulta de sumar los productos de las componentes
# homólogas: u1 * v1 + u2 * v2 + u3 * v3]

def producto_escalar(vector_1, vector_2):
    result = 0
    for indice in range(len(vector_1)):
        result = result + vector_1[indice] * vector_2[indice]
    return result

def main():
    vector_1 = 2, 4, 2, 8
    vector_2 = 3, 7, 5, 1
    print(producto_escalar(vector_1, vector_2))

main() 