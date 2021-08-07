def intercambiar_columnas(matriz):
    c1=int(input("Ingrese la primer columna a intercambiar: "))
    c2=int(input("Ingrese la segunda columna a intercambiar: "))
    for i in range(3):
        aux = matriz[i][c1-1]
        matriz[i][c1-1] = matriz[i][c2-1]
        matriz[i][c2-1] = aux
    return matriz