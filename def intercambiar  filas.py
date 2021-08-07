def intercambiar_filas(matriz):
    f1=int(input("Ingrese la primer fila a intercambiar: "))
    f2=int(input("Ingrese la primer fila a intercambiar: "))
    for i in range(3):
        aux = matriz[f1-1][i]
        matriz[f1-1][i] = matriz[f2-1][i]
        matriz[f2-1][i] = aux
    return matriz