def rellenar_diagonal(matriz):
    filas = len(matriz)
    n = 1
    total = 0
    for i in range(filas):
           matriz[i][i]= n
           n+= 2