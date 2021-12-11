# Ejercicio    3.3.
# Definir  (y  documentar) dos  funciones con  nombre apropiado.  
# Una  funciónque...:
# a) Calcule la cantidad de segundos de un tiempo dado (por parámetros) en horas, minutos y segundos, y devuelva el resultado al programa principal.
# b) Calcule la cantidad de horas, minutos y segundosde un tiempo dado (por parámetro) en segundos, y devuelva el resultado al programa principal.

def convert_to_seconds(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos

def seconds_to_hours(segundos):
    horas = segundos // 3600
    minutos = segundos % 3600 // 60
    segundos = segundos % 3600 % 60
    
    return horas, minutos, segundos


print(seconds_to_hours(4250))