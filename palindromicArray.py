import random

def generate_array():
  elements = random.randint(5,5)
  array = []
  for i in range(elements):
        array.append(random.randint(3,5))
  return array

def is_palindromic(vec):
    cont = 0
    lenght = len(vec)
    for n in vec:
        if vec[cont]==vec[lenght-1]:
            cont = cont + 1
            lenght = lenght - 1
        else:
            return False
    return True
##########

array = generate_array()
palindromic = is_palindromic(array)

print(array,end=" ")
print()
if palindromic==False:
    print("Its not palindromic")
else:
    print("It is palindromic")