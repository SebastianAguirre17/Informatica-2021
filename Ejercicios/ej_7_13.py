# Ejercicio 7.13. 
# Definir una función que reciba como parámetro una lista de tuplas, cada una
# de la forma (apellido, nombre, inicial_segundo_nombre), y devuelva como resultado una lista
# de cadenas de caracteres, cada una de las cuales contenga primero el nombre, un espacio,
# luego la inicial con un punto, un espacio y luego el apellido.

def tup_to_cadenas(lista):
    result = []
    
    for apellido, nombre, inicial in lista:
        texto = ''
        texto = texto + nombre + ' ' + inicial + '. ' + apellido
        result.append(texto) 
        
    return result

def main():
    """ Prueba de funciones """
    lista = [('Pérez', 'José', 'E'), ('Giménez', 'Jorge', 'A'), ('Aguirre', 'Sebastián', 'N')]
    
    nueva_lista = tup_to_cadenas(lista)
    for elem in nueva_lista:
        print(elem)
    
main()