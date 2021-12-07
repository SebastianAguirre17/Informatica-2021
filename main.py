def es_bisiesto(anio):
    """ Recibe por parámetro un número que representa un año, y devuelva un resultado 
        booleano que indique si es o no bisiesto. 
    """
    return anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0

def cant_dias_mes(mes, anio):
    """ Recibe por parámetro dos números que representan el mes y el año, devuelva 
        como resultado la cantidad de días correspondientes al mes o cero si el mes no existe.
    """
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        return 31
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return 30
    elif mes == 2 and es_bisiesto(anio):
        return 29
    elif mes == 2 and not es_bisiesto(anio):
        return 28
    else:
        return 0
    
def valida_fecha(dia, mes, anio):
    """ Recibe por parámetros una fecha en números, devuelve
        un resultado booleano que indica si es válida o no.
    """
    return dia > 0 and cant_dias_mes(mes, anio) != 0 and dia <= cant_dias_mes(mes, anio)

def devuelve_situaciones(identificador):
    """ Recibe por parámetro una letra, devuelve de forma textual el tipo de 
        denuncia que repressenta.
    """
    if identificador == 'a':
        return "Hechos de violencia sexual"
    elif identificador == 'b':
        return "Hechos de acoso sexual"
    elif identificador == 'c':
        return "Hechos con connotación sexista"
    else: 
        return "Comportamientos y acciones de violencia"

def devuelve_genero(identificador):
    """ Recibe por parámetro una letra, devuelve de forma textual 
        el género que respresenta.
    """
    if identificador == 'm':
        return "Mujer"
    elif identificador == 'v':
        return "Varón"
    else:
        return "Otre"

def devuelve_claustro(identificador):
    """ Recibe por parámetro una letra, devuelve de forma textual 
        el claustro que respresenta.
    """
    if identificador == 'e':
        return "Estudiante"
    elif identificador == 'n':
        return "No Docente"
    elif identificador == 'd':
            return "Docente"
    else:
        return "Graduade"

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

def mostrar_denuncia(anio, nro_exp, dia, mes, genero_denunciante, claustro_denunciante, 
                     genero_denunciado, claustro_denunciado, tipos_situaciones):
    """ Recibe por parámetro datos de la denuncia y los imprime en pantalla
        de forma descriptiva y ordenada.
    """
    fecha = str(dia) + "/" + str(mes) + "/" + str(anio)
    print("\n----------------------------------------------------------------------------------")
    print("--   Datos de la denuncia:")
    print("----------------------------------------------------------------------------------")
    print("--   Número de expediente:               ", nro_exp)
    print("--   Fecha de denuncia:                  ", fecha)
    print("--   Género de la persona denunciante:   ", devuelve_genero(genero_denunciante))
    print("--   Claustro de la persona denunciante: ", devuelve_claustro(claustro_denunciante))
    print("--   Tipo/s de situación/es vivenciada/s:", tipos_situaciones)
    print("--   Género de la persona denunciada:    ", devuelve_genero(genero_denunciado))
    print("--   Claustro de la persona denunciada:  ", devuelve_claustro(claustro_denunciado))
    print("----------------------------------------------------------------------------------")
    
    input("Presione Enter para continuar.")

def mostrar_estadisticas(anio, semestre, total_denuncias, porcentaje, cant_pares, mayor_exp, cant_den_mujeres, cant_den_varones, 
                         cant_den_otres, cant_den_docentes, cant_den_nodocentes, cant_den_estudiantes, cant_den_graduades):
    """ Recibe por parámetro los datos estadísticos y los imprime en pantalla
        de forma descriptiva y ordenada.
    """
    print("\n---------------------------------------------------------------------")
    print("--   Informe del semestre", semestre, "del año", anio)
    print("---------------------------------------------------------------------")
    print("--  Total de denuncias:                                    ", total_denuncias)
    print("--  Clasificadas en más de un tipo de situación vivenciada:", porcentaje, "%")
    print("--  Denuncias entre pares del mismo claustro:              ", cant_pares)
    print("--  Mayor número de expediente ingresado:                  ", mayor_exp)
    print("--  Denunciantes mujeres:                                  ", cant_den_mujeres)
    print("--  Denunciantes varones:                                  ", cant_den_varones)
    print("--  Denunciantes otres:                                    ", cant_den_otres)
    print("--  Denunciantes del claustro de estudiantes:              ", cant_den_estudiantes)
    print("--  Denunciantes del claustro de no docentes:              ", cant_den_nodocentes)
    print("--  Denunciantes del claustro de docentes:                 ", cant_den_docentes)
    print("--  Denunciantes del claustro de graduades:                ", cant_den_graduades)
    print("---------------------------------------------------------------------")
    input("\nPresione Enter para salir.")

def main():
    """ Función Princpipal
    """
    print("-----------------------------------------------------")
    print("--   Programa Transversal de Políticas de Género   --")
    print("--          y Diversidad de la UNDAV               --")
    print("-----------------------------------------------------")
    
    anio = 0
    while anio < 2021:
        anio = int(input("\nIngrese año del informe: "))
        if anio < 2021:
            print("¡Año Incorrecto! Debe ser mayor a 2020.")
    
    semestre = 0
    while semestre != 1 and semestre != 2:
        semestre = int(input("Ingrese semestre del informe: "))
        if semestre != 1 and semestre != 2:
            print("¡Semestre incorrecto!")
    
    cant_den_mujeres = cant_den_varones = cant_den_otres = cant_den_estudiantes = cant_den_nodocentes = 0
    cant_den_docentes = cant_den_graduades = mayor_exp = cant_pares = acum_varios_tipos = 0
    
    continuar = 'S'
    while continuar == 'S' or continuar == 's':
        continuar = input("\nPresione 'S' para ingresar una denuncia u otra letra para continuar: ")
        if continuar == 'S' or continuar == 's':
            # Expediente
            expediente = int(input("\nIngrese número de expediente: "))
            if expediente > mayor_exp:
                mayor_exp = expediente
            
            # Fecha
            fecha_valida = False
            while not fecha_valida:
                mes = int(input("Ingrese mes de la denuncia: "))
                if mes > 12 or mes < 1:
                    print("¡Mes incorrecto! Reintente.") 
                elif (semestre == 1 and mes > 6) or (semestre == 2 and mes < 7):
                    print("¡El mes no pertenece al semestre! Reintente.")
                else:
                    dia = int(input("Ingrese dia de la denuncia: "))
                    fecha_valida = valida_fecha(dia, mes, anio)
                    if not fecha_valida:
                        print("¡Fecha incorrecta! Reingrese")
                    else:
                        fecha_valida = True

            # Género Denunciante
            genero_denunciante = '-'
            while genero_denunciante != 'm' and genero_denunciante != 'v' and genero_denunciante != 'x':
                genero_denunciante = input("Ingrese el género de la persona denunciante (x - m - v): ")
                if genero_denunciante != 'm' and genero_denunciante != 'v' and genero_denunciante != 'x':
                    print("¡El dato ingresado es incorrecto! Reingrese el género.")
            if genero_denunciante == 'm':
                cant_den_mujeres = cant_den_mujeres + 1  
            elif genero_denunciante == 'v':
                cant_den_varones = cant_den_varones + 1   
            else:    
                cant_den_otres = cant_den_otres + 1
            
            # Clasutro denunciante
            claustro_denunciante = '-'
            while claustro_denunciante != 'e' and claustro_denunciante != 'n' and claustro_denunciante != 'd' and claustro_denunciante != 'g':
                claustro_denunciante = input("Ingrese el claustro de la persona denunciante (e, n, d, g): ")
                if claustro_denunciante != 'e' and claustro_denunciante != 'n' and claustro_denunciante != 'd' and claustro_denunciante != 'g':
                    print("¡El dato ingresado es incorrecto! Reingrese el claustro.")
            if claustro_denunciante == 'e':
                cant_den_estudiantes = cant_den_estudiantes + 1  
            elif claustro_denunciante == 'n':
                cant_den_nodocentes = cant_den_nodocentes + 1   
            elif claustro_denunciante == 'd':
                cant_den_docentes = cant_den_docentes + 1  
            else:    
                cant_den_graduades = cant_den_graduades + 1            
                    
            # Tipos de situaciones
            tipos_situaciones, cont_tipos = solicita_tipos_situaciones()
            if cont_tipos > 1:
                acum_varios_tipos = acum_varios_tipos + 1
            
            # Género denunciado
            genero_denunciado = '-'
            while genero_denunciado != 'm' and genero_denunciado != 'v' and genero_denunciado != 'x':
                genero_denunciado = input("Ingrese el género de la persona denunciada (x - m - v): ")
                if genero_denunciado != 'm' and genero_denunciado != 'v' and genero_denunciado != 'x':
                    print("¡El dato ingresado es incorrecto! Reingrese el género.")
            
            # Clasutro denunciado
            claustro_denunciado = '-'
            while claustro_denunciado != 'e' and claustro_denunciado != 'n' and claustro_denunciado != 'd' and claustro_denunciado != 'g':
                claustro_denunciado = input("Ingrese el claustro de la persona denunciada (e, n, d, g): ")
                if claustro_denunciado != 'e' and claustro_denunciado != 'n' and claustro_denunciado != 'd' and claustro_denunciado != 'g':
                    print("¡El dato ingresado es incorrecto! Reingrese el claustro.")
    
            if claustro_denunciado == claustro_denunciante:
                cant_pares = cant_pares + 1
                
            mostrar_denuncia(anio, expediente, dia, mes, genero_denunciante, claustro_denunciante, genero_denunciado, claustro_denunciado, tipos_situaciones)
        # Fin ciclo

    total_denuncias = cant_den_mujeres + cant_den_varones + cant_den_otres
    porcentaje = 0
    if acum_varios_tipos != 0:
        porcentaje = acum_varios_tipos * 100 / total_denuncias
    
    mostrar_estadisticas(anio, semestre, total_denuncias, porcentaje, cant_pares, mayor_exp, cant_den_mujeres, cant_den_varones, 
                         cant_den_otres, cant_den_docentes, cant_den_nodocentes, cant_den_estudiantes, cant_den_graduades)
    
main()

# Pruebas de documentación
# help(es_bisiesto)
# help(valida_fecha)
# help(cant_dias_mes)
# help(devuelve_claustro)
# help(devuelve_genero)
# help(devuelve_situaciones)
# help(solicita_tipos_situaciones)
# help(mostrar_denuncia)
# help(mostrar_estadisticas)