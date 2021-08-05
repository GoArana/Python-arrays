def seleccion(vec):
    largo = len(vec)
    for i in range(largo-1):
        for j in range(i+1,largo):
            if v[i] > v[j]:
                aux = v[i]
                v[i] = v[j]
                v[j] = aux