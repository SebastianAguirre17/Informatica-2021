# Ejercicio 7.8. Suponer qué hace el siguiente código y luego comprobar su ejecución:
    
    
def pba_listas():
    """ Prueba operaciones con listas """
    palabra = "murcielago"
    tup1 = (1, "manzana", "uva", "pera")
    tup4 = (4, "roja", "azul", "amarilla")
    listup = [tup1]
    listup.append(tup4)
    listup.append(palabra[3:-3])
    longi = len(listup)
    pausa = input('dar enter para seguir >>> ')
    print ("listup:", listup)
    print ("longi:", longi)
    print ("listup [1:2]", listup [1:2])
    nom1, nom2, nom3 = listup
    nome = listup[0][1]
    pausa = input('dar enter para seguir >>> ')
    print ("nom1:", nom1,"  nome:", nome)
    pos = listup.index('ciel')
    listup.insert(pos,'mur')
    pausa = input('dar enter para seguir >>> ')
    print ("pos:", pos)
    print ("listup:", listup)
    listup.remove('mur')
    pausa = input('dar enter para seguir >>> ')
    print ("listup:", listup)
    lisa = []
    for digi in range(97,102):
        lisa.append(digi)
    pausa = input('dar enter para seguir >>> ')
    print ('lisa:', lisa)
    for num in lisa:
        if num < 100:
            letra = chr(num)
            pos = lisa.index(num)
            lisa.remove(num)
            lisa.insert(pos,letra)
    lisa[4] = 'd'
    pausa = input('dar enter para seguir >>> ')
    print ('lisa:', lisa)

pba_listas()
