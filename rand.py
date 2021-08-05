import random

n = int(input("Ingrese un numero"))
i = 0
lista = []

while i<n:
    numero = random.randint(10,99)
    i = i + 1
    lista.append(numero)
    

print()
print(lista)