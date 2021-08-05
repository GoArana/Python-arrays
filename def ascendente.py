def es_ascendente(vec):
    largo = len(vec-1)
    cont = 0
    cont2 = 1
    for n in vec:
        if cont2==largo:
            return True
        elif vec[cont]<vec[cont2]:
            cont =+1
            cont2=+1
        else:
            return False