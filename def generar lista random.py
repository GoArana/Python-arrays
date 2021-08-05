def generar_lista(inicio,n,fin):
     lista = []
     for i in range(n):
          a = random.randint(inicio, fin)
          lista.append(a)
     return lista