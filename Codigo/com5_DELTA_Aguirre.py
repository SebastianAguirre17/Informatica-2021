from com5_Catalano import valida_fecha
from com5_Rey import solicita_tipos_situaciones
from com5_Rivera import mostrar_denuncia
from com5_Rivera import mostrar_estadisticas

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
        semestre = int(input("\nIngrese semestre del informe: "))
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
                mes = int(input("\nIngrese mes de la denuncia: "))
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
                genero_denunciante = input("\nIngrese el género de la persona denunciante (x - m - v): ")
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
                claustro_denunciante = input("\nIngrese el claustro de la persona denunciante (e, n, d, g): ")
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
                genero_denunciado = input("\nIngrese el género de la persona denunciada (x - m - v): ")
                if genero_denunciado != 'm' and genero_denunciado != 'v' and genero_denunciado != 'x':
                    print("¡El dato ingresado es incorrecto! Reingrese el género.")
            
            # Clasutro denunciado
            claustro_denunciado = '-'
            while claustro_denunciado != 'e' and claustro_denunciado != 'n' and claustro_denunciado != 'd' and claustro_denunciado != 'g':
                claustro_denunciado = input("\nIngrese el claustro de la persona denunciada (e, n, d, g): ")
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
