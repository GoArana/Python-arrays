def es_simetrica(matriz):
    simetrica = True
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        for j in range(columnas):
            if (matriz[i][j]!=matriz[j][i]):
                simetrica = False
    return simetrica

sime = es_simetrica(matriz)

if sime==True:
    print("si")
else:
    print("no")