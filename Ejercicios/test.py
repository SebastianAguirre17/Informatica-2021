def reparte_txt(txt, tupla_bin):
    cad_1 = ''
    cad_2 = ''
    
    for i in range(len(tupla_bin)):
        if tupla_bin[i] == 1:
            cad_1 = cad_1 + txt[i]
        else:
            cad_2 = cad_2 + txt[i]

    return cad_1, cad_2

def main():
    
    lista = [1, 12, 2021]
    lista.append("Siglo XXI")
    
    renombre = lista
    renombre.insert(0, 'Hoy es:')
    
    print(lista)
    print(renombre)
    
    
main()
