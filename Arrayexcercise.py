import random

#Array with random numbers of X digits. 
def get_random_array():
  num_of_elements = random.randint(5, 10)
  array = []
  for i in range(num_of_elements):
    array.append(random.randint(10, 99))
  return array

#sum of elements of the array.

def get_sum(array):
  return sum(array)

#delete a value chosen by the user 

def remove_num(array):
  number_to_delete = int(input("Input the number to delete: "))
  for num in array:
    if (num == number_to_delete):
      array.remove(num)

#check is the array is palindromic

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

if __name__ == "__main__":
  print("Esta es una lista random:")
  array = get_random_array()
  print(array)
  print("La sumatoria de todos los elementos es: %d" % get_sum(array))
  remove_num(array)
  print("The array without the number is: ",array)
  
if is_palindromic(array)==True:
    print("The array is palindromic")
else:
    print("It is not palindromic")