# Ejercicio 7.4. 
# Definiruna función ‘suma_vectores’ que, dadas por parámetrodos tuplas que representan  vectores
# de igual dimensión, devuelva comoresultado la tupla que representa su suma.  
# [La  suma  de  vectores  (u1,  u2,  u3)  y  (v1,  v2,  v3), se puede calcular como el vector 
# que resulta de sumar sus componentes homólogas: (u1 + v1,u2 + v2,u3 + v3) ].

def suma_vectores(vector_1, vector_2):
    result = ()
    for indice in range(len(vector_1)):
        result = result + (vector_1[indice] + vector_2[indice],)
    return result

def main():
    vector_1 = 2, 4, 2, 8
    vector_2 = 3, 7, 5, 1
    print(suma_vectores(vector_1, vector_2))

main() 