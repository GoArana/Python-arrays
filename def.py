import random

def generarlista():
    lista = []
    n = random.randint(0, 999)
    while n!=0:
        lista.append(n)
        n = random.randint(0, 999)
    return lista

def obtenerdivisores(n):
    lista = []
    for i in range(1, n+1):
        if n%i==0:
            lista.append(i)
    return lista

# Programa principal
milista = generarlista()
print(milista)
maximo = max(milista)
divisores = obtenerdivisores(maximo)
print("\nLos divisores de", maximo, "son", *divisores)
milista.sort(key=lambda x:x%10)
print("\nLista ordenada según el último dígito de cada número:")
print(*milista)
