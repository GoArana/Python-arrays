def es_capicua(vec,n):
    cont = 0
    cont2 = n-1
    for n in vec:
        if vec[cont]==vec[cont2]:
            cont = cont + 1
            cont2 = cont2 - 1
        else:
            return False
    return True