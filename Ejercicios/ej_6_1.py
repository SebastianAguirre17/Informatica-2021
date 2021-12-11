def pba_cadenas():
    """ Prueba operaciones con cadenas """
    palabra = "murcielago"
    pausa = input('dar enter para seguir >>> ')
    print ( 'palabra:', palabra )
    print ( 'palabra [0]:', palabra [0] )
    print ( 'palabra [-1]:', palabra [-1] )
    seg1 = palabra [:3]
    seg2 = palabra [3:6]
    seg3 = palabra [6:]
    pausa = input('\ndar enter para seguir >>> ') # '\n' salta linea
    print ( 'seg1 + seg2 + seg3:', seg1 + seg2 + seg3 )
    print ( 'seg1 , seg2 , seg3:', seg1, seg2, seg3 )
    print ( 'seg3 [0:2] * 3:', seg3 [0:2] * 3 )
    pausa = input('\ndar enter para seguir >>> ')
    print ( 'seg3 [0:-1]:', seg3 [0:-1] )
    print ( 'seg3 [-4:-1]:', seg3 [-4:-1] )
    largo = len(seg3)
    pausa = input('\ndar enter para seguir >>> ')
    print ( 'largo:', largo )
    print ( 'seg3[-largo]:', seg3[-largo] )
    pausa = input('\ndar enter para seguir >>> ')
    #print 'seg3[largo]:', seg3[largo]
    for ind in range(largo):
        print ('indice:', ind, 'caracter:', seg3[ind])
        pausa = input('\ndar enter para seguir >>> ')
    for letra in seg3:
        print ( 'caracter:', letra )
        pausa = input('\ndar enter para seguir >>> ')
        #palabra[1] = 'o'
        copia = ""
        print ( 'copia:', copia, ' ==> len():', len(copia) )
    for letra in seg3:
        copia = copia + letra
        print ('copia:', copia, ' ==> len():', len(copia))
        
pba_cadenas()