# Create an array with the square roots numbers between 1 and N 
# N is input from the user, and he can choose to print N last numbers from the same array

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