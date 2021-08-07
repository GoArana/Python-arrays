def obtenerdivisores(n):
    lista = []
    for i in range(1, n+1):
        if n%i==0:
            lista.append(i)
    return lista

maximo = max(milista)
divisores = obtenerdivisores(maximo)