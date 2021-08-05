def suma_listas(a,b):
    lista = []
    cont = 0
    for i in a:
        suma = a[cont] + b[cont]
        lista.append(suma)
        cont = cont + 1
    return lista    