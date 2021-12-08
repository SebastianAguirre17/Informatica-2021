from com5_Gimenez import devuelve_claustro
from com5_Gimenez import devuelve_genero

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
    print("\n--------------------------------------------------------")
    print("--   Informe del semestre", semestre, "del año", anio)
    print("--------------------------------------------------------")
    print("--  Total de denuncias:                      ", total_denuncias)
    print("--  Denunciantes mujeres:                    ", cant_den_mujeres)
    print("--  Denunciantes varones:                    ", cant_den_varones)
    print("--  Denunciantes otres:                      ", cant_den_otres)
    print("--  Denunciantes del claustro de estudiantes:", cant_den_estudiantes)
    print("--  Denunciantes del claustro de docentes:   ", cant_den_docentes)
    print("--  Denunciantes del claustro de no docentes:", cant_den_nodocentes)
    print("--  Denunciantes del claustro de graduades:  ", cant_den_graduades)
    print("--  Denuncias entre pares del mismo claustro:", cant_pares)
    print("--  Porcentaje de situaciones múltiples:     ", porcentaje, "%")
    print("--  Mayor número de expediente ingresado:    ", mayor_exp)
    print("--------------------------------------------------------")
    input("\nPresione Enter para salir.")