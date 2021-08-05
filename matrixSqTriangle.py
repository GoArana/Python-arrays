def square(rows):
    for i in range (rows,0,-1):
        for j in range (rows,0,-1):
            print(fill,end="")
        print()
    return 0
def triangle (rows):
    k = rows-1
    for i in range (0,rows):
        for j in range (0,k):
            print(end=" ")
        k-=1
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")

rows = int(input("Insert number of rows: "))
fill = "**"
print("Square = 1, Triangle = 2")
option = int(input("option 1 o 2: "))
while 1>option or option>2:
    option = int(input("Square = 1, Triangle = 2 "))
if option==1:
    print("This is the square:")
    square(rows)
else:
    print("This is the triangle")
    triangle(rows)