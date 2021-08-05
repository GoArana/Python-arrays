def contarApariciones(vec,valor):
   cont = 0
   for i in range(len(vec)):
         if vec[i]==valor:
                cont = cont + 1
   return unicos

def contarUnicos(vec):
   contUnicos = 0
   for i in range(len(vec)):
        cont = 0
        for j in range(len(vec)):
            if vec[i]==vec[j]:
                    cont = cont + 1
        if cont == 1:
            contUnicos = contUnicos + 1
  return contUnicos

print(listaLeg[cont]),print(listaC[cont]),print(listaS[cont])