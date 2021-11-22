import os

def es_bisiesto(anio):
    return anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0

def cant_dias_mes(mes, anio):
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
    return cant_dias_mes(mes, anio) != 0 and dia <= cant_dias_mes(mes, anio)

def devuelve_situaciones(identificador):
    if identificador == 'a':
        return "Hechos de violencia sexual"
    elif identificador == 'b':
        return "Hechos de acoso sexual"
    elif identificador == 'c':
        return "Hechos con connotación sexista"
    else: 
        return "Comportamientos y acciones de violencia"

def devuelve_genero(identificador):
    if identificador == 'm':
        return "Mujer"
    elif identificador == 'v':
        return "Varón"
    else:
        return "Otre"

def devuelve_claustro(identificador):
    if identificador == 'e':
        return "Estudiante"
    elif identificador == 'n':
        return "No Docente"
    elif identificador == 'd':
            return "Docente"
    else:
        return "Graduade"

def solicita_tipos_situaciones():
    tipos = ''
    contador = 0
    flag = True
    print("Tipos de situaciones vivenciadas:")
    print("a) Hechos de violencia sexual \nb) Hechos de acoso sexual \nc) Hechos con connotación sexista \nd) Comportamientos y acciones de violencia")
    while flag:
        tipo = input("Elija una opción: ")
        
        if tipo != 'a' and tipo != 'b' and tipo != 'c' and tipo != 'd':
            print("La opción ingresada es incorrecta.")
        else:
            tipos = tipos + devuelve_situaciones(tipo) + " - "
            eleccion = input("¿Desea ingresar otra opción? S/N: ")
            contador = contador + 1
            if eleccion == 'N' or eleccion == 'n':
                flag = False
                
    return tipos, contador

def mostrar_denuncia(anio, nro_exp, dia, mes, genero_denunciante, claustro_denunciante, genero_denunciado, claustro_denunciado, tipos_situaciones):
    os.system('cls')
    print("Datos de la denuncia:")
    print("Número de expediente:", nro_exp)
    print("Fecha de denuncia:", dia, "/", mes, "/", anio)
    print("Género auto percibido de la persona denunciante:", devuelve_genero(genero_denunciante))
    print("Claustro al que pertenece la persona denunciante:", devuelve_claustro(claustro_denunciante))
    print("Tipo/s de situación/es vivenciada/s:", tipos_situaciones)
    print("Género de la persona denunciada:", devuelve_genero(genero_denunciado))
    print("Claustro de la persona denunciada:", devuelve_claustro(claustro_denunciado))
    input("Presione Enter para continuar.")

def mostrar_estadisticas(anio, semestre, total_denuncias, porcentaje, cant_pares, mayor_exp, cant_den_mujeres, cant_den_varones, cant_den_otres, cant_den_docentes, cant_den_nodocentes, cant_den_estudiantes, cant_den_graduades):
    os.system('cls')
    print("Informe del semestre", semestre, "del año", anio)
    print("Cantidad total de denuncias:", total_denuncias)
    print("Porcentaje de clasificadas en más de un tipo de situación vivenciada:", porcentaje, "%")
    print("Cantidad de denuncias entre pares del mismo claustro:", cant_pares)
    print("Mayor número de expediente ingresado:", mayor_exp)
    print("Cantidad de denunciantes mujeres:", cant_den_mujeres)
    print("Cantidad de denunciantes varones:", cant_den_varones)
    print("Cantidad de denunciantes otres:", cant_den_otres)
    print("Cantidad de denunciantes del claustro de estudiantes:", cant_den_estudiantes)
    print("Cantidad de denunciantes del claustro de no docentes:", cant_den_nodocentes)
    print("Cantidad de denunciantes del claustro de docentes:", cant_den_docentes)
    print("Cantidad de denunciantes del claustro de graduades:", cant_den_graduades)
    input("Presione Enter para continuar.")

def main():
    anio = 0
    while anio < 2021:
        anio = int(input("Ingrese en año del informe: "))
        if anio < 2021:
            print("El año ingresado es incorrecto!")
    
    semestre = 0
    while semestre != 1 and semestre != 2:
        semestre = int(input("Ingrese en semestre del informe: "))
        if semestre != 1 and semestre != 2:
            print("El semestre ingresado es incorrecto!")
    
    cant_den_mujeres = cant_den_varones = cant_den_otres = cant_den_estudiantes = cant_den_nodocentes = cant_den_docentes = cant_den_graduades = mayor_exp = cant_pares = acum_varios_tipos = 0
    
    continuar = 'S'
    while continuar == 'S' or continuar == 's':
        continuar = input("Presione 'S' para ingresar una denuncia, cualquier otra tecla para continuar: ")
        if continuar == 'S' or continuar == 's':
            # EXPEDIENTE
            expediente = int(input("Ingrese el número de expediente: "))
            if expediente > mayor_exp:
                mayor_exp = expediente
            
            # MES
            mes_valido = False
            while not mes_valido:
                mes = int(input("Ingrese el mes de la denuncia: "))
                if mes > 12 or mes < 1:
                    print("El mes ingresado es incorrecto! Reintente.") 
                elif (semestre == 1 and mes > 6) or (semestre == 2 and mes < 7):
                    print("El mes no se corresponde con el semestre! Reintente.")
                else:
                    mes_valido = True
            
            # FECHA
            fecha_valida = False
            while not fecha_valida:
                dia = int(input("Ingrese el dia de la denuncia: "))
                fecha_valida = valida_fecha(dia, mes, anio)
                if not fecha_valida:
                    print("Los datos ingresados son incorrectos! Reingrese día")

            # GENERO DENUNCIANTE
            genero_denunciante = '-'
            while genero_denunciante != 'm' and genero_denunciante != 'v' and genero_denunciante != 'x':
                genero_denunciante = input("Ingrese el género autopercibido de la persona denunciante (x - m - v): ")
                if genero_denunciante != 'm' and genero_denunciante != 'v' and genero_denunciante != 'x':
                    print("El dato ingresado es incorrecto! Reingrese el género.")
            if genero_denunciante == 'm':
                cant_den_mujeres = cant_den_mujeres + 1  
            elif genero_denunciante == 'v':
                cant_den_varones = cant_den_varones + 1   
            else:    
                cant_den_otres = cant_den_otres + 1
            
            #CLAUSTRO DENUNCIANTE
            claustro_denunciante = '-'
            while claustro_denunciante != 'e' and claustro_denunciante != 'n' and claustro_denunciante != 'd' and claustro_denunciante != 'd':
                claustro_denunciante = input("Ingrese el claustro al que pertenece de la persona denunciante (e, n, d, g): ")
                if claustro_denunciante != 'e' and claustro_denunciante != 'n' and claustro_denunciante != 'd' and claustro_denunciante != 'd':
                    print("El dato ingresado es incorrecto! Reingrese el claustro.")
            if claustro_denunciante == 'e':
                cant_den_estudiantes = cant_den_estudiantes + 1  
            elif claustro_denunciante == 'n':
                cant_den_nodocentes = cant_den_nodocentes + 1   
            elif claustro_denunciante == 'd':
                cant_den_docentes = cant_den_docentes + 1  
            else:    
                cant_den_graduades = cant_den_graduades + 1            
                    
            # TIPOS
            tipos_situaciones, cont_tipos = solicita_tipos_situaciones()
            if cont_tipos > 1:
                acum_varios_tipos = acum_varios_tipos + 1
            
            # GENERO DENUNCIADO
            genero_denunciado = '-'
            while genero_denunciado != 'm' and genero_denunciado != 'v' and genero_denunciado != 'x':
                genero_denunciado = input("Ingrese el género autopercibido de la persona denunciada (x - m - v): ")
                if genero_denunciado != 'm' and genero_denunciado != 'v' and genero_denunciado != 'x':
                    print("El dato ingresado es incorrecto! Reingrese el género.")
            
            #CLAUSTRO DENUNCIADO
            claustro_denunciado = '-'
            while claustro_denunciado != 'e' and claustro_denunciado != 'n' and claustro_denunciado != 'd' and claustro_denunciado != 'g':
                claustro_denunciado = input("Ingrese el claustro ala que pertenece de la persona denunciada (e, n, d, g): ")
                if claustro_denunciado != 'e' and claustro_denunciado != 'n' and claustro_denunciado != 'd' and claustro_denunciado != 'g':
                    print("El dato ingresado es incorrecto! Reingrese el claustro.")
    
            if claustro_denunciado == claustro_denunciante:
                cant_pares = cant_pares + 1
                
            mostrar_denuncia(anio, expediente, dia, mes, genero_denunciante, claustro_denunciante, genero_denunciado, claustro_denunciado, tipos_situaciones)
            
        
        # FIN BUCLE

    total_denuncias = cant_den_mujeres + cant_den_varones + cant_den_otres
    porcentaje = cant_pares * 100 * total_denuncias
    
    mostrar_estadisticas(anio, semestre, total_denuncias, porcentaje, cant_pares, mayor_exp, cant_den_mujeres, cant_den_varones, cant_den_otres, cant_den_docentes, cant_den_nodocentes, cant_den_estudiantes, cant_den_graduades)

main()

