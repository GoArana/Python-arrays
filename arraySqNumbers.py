# Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos),
# donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores
# de la lista.

import math
N=int(input("Input a number: " ))
array=[]
array2=[]
for i in range(0,N):
    i=i+1
    array.append(i)

lenght=int(input("Input how many last numbers you want: "))
lastNum= array[-lenght:]
for i in range(0,N):
     j=array[i]
     i+=1
     sq=j**2
     array2.append(sq)

print("The entire array is: ", array)
print("The last",lenght,"are:", lastNum)
print("The square root numbers are: ", array2)