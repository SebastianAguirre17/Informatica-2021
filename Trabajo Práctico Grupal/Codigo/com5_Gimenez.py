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


