def convertirBinario(n):
    suma = 0
    cont = 0
    while n!=0:
        digBin = n%2
        suma = suma + digBin*(10**cont)
        cont= cont + 1
        n = n//2
    return suma

n = 15

numero = convertirBinario(n)
print(numero)