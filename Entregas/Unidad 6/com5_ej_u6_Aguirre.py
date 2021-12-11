""" Módulo para completar definición de funciones. Tarea de Unidad 6 """

def reparte_txt(txt, tupla_bin):
    cadena_1 = cadena_2 = ''
    
    for indice in range(len(txt)):
        if tupla_bin[indice] == 1:
            cadena_1 = cadena_1 + txt[indice]
        else:
            cadena_2 = cadena_2 + txt[indice]

    return cadena_1, cadena_2

def main():
    """ Prueba el comportamiento de la función reparte_txt() """
    binario = 1
    cade = 'Ve-Murciélago'
    tup_unos = ()
    tup_ceros = ()
    tup_varios = ()
    for car in cade:
        if binario == 0:
            binario = 1
        else:
            binario = 0
        tup_unos = tup_unos + (1,)
        tup_ceros = tup_ceros + (0,)
        tup_varios = tup_varios + (binario,)
    print ('Salidas esperadas de función reparte_txt():')
    print ('Cadena:->', cade,'-Tupla:->', tup_unos)
    print ('debe dar:----------------------->', (cade,''))
    print ('Cadena:->', cade,'-Tupla:->', tup_ceros)
    print ('debe dar:----------------------->', ('',cade))
    print ('Cadena:->', cade,'-Tupla:->', tup_varios)
    print ('debe dar:----------------------->', ('eMrilg','V-ucéao'))
    print ('\nResultados reales de función reparte_txt():')
    print ('Cadena:->', cade,'-Tupla:->', tup_unos)
    print ('da:----------------------------->', reparte_txt(cade,tup_unos))
    print ('Cadena:->', cade,'-Tupla:->', tup_ceros)
    print ('da:----------------------------->', reparte_txt(cade,tup_ceros))
    print ('Cadena:->', cade,'-Tupla:->', tup_varios)
    print ('da:----------------------------->', reparte_txt(cade,tup_varios))

# help(reparte_txt)
main()