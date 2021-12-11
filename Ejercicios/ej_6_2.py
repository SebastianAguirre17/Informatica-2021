# Ejercicio 6.2. 
# Definir una función “segm_3_txt” que, dados como parámetros una cadena de caracteres y un carácter (que denominaremos selector), 
# a) imprima los tres primeros caracteres de la cadena, si el valor del selector es la letra ‘P’,
#   o los tres últimos caracteres si el valor del selector es ‘U’, o el mensaje ‘Error en el selector’ si el valor del selector no es ‘P’ ni ‘U’.
# b) modificar  la  solución  anterior,  para  que  sólo  imprima  el primero o el último  carácter, respectivamente, cuando la longitud de la cadena sea menorque 3.

def segm_3_text(cadena, selector):
    if selector == 'P':
        print(cadena[:3])
    elif selector == 'U':
        print(cadena[-3:])
    else:
        print("Error en el selector")
        
def main():
    segm_3_text("Esto es una cadena", 'U')
    
main()