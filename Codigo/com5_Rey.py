def devuelve_situaciones(identificador):
    """ Recibe por parámetro una letra, devuelve de forma textual el tipo de 
        denuncia que repressenta.
    """
    if identificador == 'a':
        return "H. violencia sexual"
    elif identificador == 'b':
        return "H. acoso sexual"
    elif identificador == 'c':
        return "H. con. sexista"
    else: 
        return "Comp/Acc. violentas"

def solicita_tipos_situaciones():
    """ Presenta por pantalla un menú con los tipos denuncias, solicita el ingreso de 
        la/s opcion/es. Mientras no se seleccione una opción, se pedirá el reingreso. Retorna en forma 
        textual la/s denuncia/s elegidas y la cantidad de tipos seleccionados.
    """
    tipos = ''
    letrasIngresadas = ''
    contador = 0
    flag = True
    print("\nTipos de situaciones vivenciadas:\n")
    print("a) Hechos de violencia sexual")
    print("b) Hechos de acoso sexual")
    print("c) Hechos con connotación sexista")
    print("d) Comportamientos y acciones de violencia\n")
    while flag:
        tipo = input("Elija una opción: ")
        
        if tipo != 'a' and tipo != 'b' and tipo != 'c' and tipo != 'd':
            print("¡La opción ingresada es incorrecta!")
        else:
            if tipo in letrasIngresadas:
                print("La opción fue elegida con anterioridad.")
            else: 
                letrasIngresadas = letrasIngresadas + tipo
                tipos = tipos + devuelve_situaciones(tipo) + " - "
                eleccion = input("\n¿Desea ingresar otra opción? S/N: ")
                contador = contador + 1
                if eleccion != 'S' and eleccion != 's':
                    flag = False
                if len(letrasIngresadas) == 4:
                    print("Ha elegido el máximo de opciones permitidas.")
                    flag = False
    return tipos, contador