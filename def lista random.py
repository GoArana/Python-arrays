import random

def listaRandom(listaZ,n):
    for i in range (n):
        listaZ.append(random.randint(0,12))
    print(listaZ)
    return listaZ

lista = []
lista = listaRandom(lista,3)