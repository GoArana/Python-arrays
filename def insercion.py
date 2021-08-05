def insercion(vec):
    for i in range(1,len(vec)):
        valorInsertar = lista[i]
        j = i
        while j>0 and lista[j-i] > valorInsertar:
            lista[j] = lista[j-1]
            j = j - 1
        lista[j] = valorInsertar