def ultimosDigitos(n, cant): 
   num = n
   aux = cant
   while cant > 0:
        n = n // 10
        cant = cant - 1
   total =  (num - (n * (10 ** aux)))
   return total

dig = 3537
cant = 2
print(ultimosDigitos(dig,cant))