import random

def rellenar_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    n = 0
    for f in range(filas):
           for c in range(columnas):
               matriz[f][c] = randint(0,10)

def imprimir_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d"%matriz[f][c],end="")
        print()

#def spiralFill(m, n, a): 
    val = 1
    k, l = 0, 0
    while (k < m and l < n): 
        for i in range(l, n): 
            a[k][i] = val 
            val += 1
        k += 1
        for i in range(k, m): 
            a[i][n - 1] = val 
            val += 1
        n -= 1
        if (k < m): 
            for i in range(n - 1, l - 1, -1): 
                a[m - 1][i] = val 
                val += 1
            m -= 1
        if (l < n): 
            for i in range(m - 1, k - 1, -1): 
                a[i][l] = val 
                val += 1
            l += 1
    for i in range(len(a)):
        print(a[i])



filas = 3
columnas = 3
resultado = []
matriz=[]
for i in range(filas):
    matriz.append([0]*columnas)
imprimir_matriz(matriz)
F=0
f=filas
C=0
c=columnas
#resultado = spiralFill(f,c,matriz)