def rellenar_matriz(m):
    n = len(m)
    mitad = n // 2
    for f in range(n):
        for c in range(n):
            if f<mitad and c<mitad:
                relleno = 1
            elif f<mitad and c>=mitad:
                relleno = 2
            elif f>=mitad and c<mitad:
                relleno = 3
            else:
                relleno = 4
            m[f][c] = relleno

def imprimir_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d"%matriz[f][c],end="")
        print()

filas = 6
columnas = 6
matriz = []
resultado = []
for i in range(filas):
    matriz.append([0]*columnas)
    
rellenar_matriz(matriz)
imprimir_matriz(matriz)