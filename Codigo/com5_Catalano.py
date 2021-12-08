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