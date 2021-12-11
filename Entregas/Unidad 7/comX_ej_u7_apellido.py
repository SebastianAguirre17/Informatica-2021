""" Módulo para completar definición de función. Tarea de Unidad 7 """

#definir función "encera_lista" con la siguiente documentación (ver indentación):
""" Recibe una lista y una tupla, de igual longitud, compuesta por unos y
    ceros (QUE NO SE DEBEN VALIDAR). Reemplaza con el valor cero, cada elemento
    de la lista ubicado en la respectiva posición de un cero de la tupla. 
    Devuelve otra lista, integrada con los elementos de la lista original
    que fueron sustituidos por el valor cero."""



def main():
    """ Función que prueba la función anterior """
    list_in = ['alfa', 'beta', 'gamma', 'beta', 'delta']
    tuplita = ( 1, 1, 1, 0, 0 )
    print ('\nSalidas esperadas de función encera_lista()')
    print ('La función devuelve -->', "['beta', 'delta']")
    print ('Y list_in quedaría  -->', "['alfa', 'beta', 'gamma', 0, 0]")
    list_out = encera_lista(list_in, tuplita)
    print ('\nResultados reales de función encera_lista()')
    print ('La función devolvió -->', list_out)
    print ('Y list_in quedó     -->', list_in)



