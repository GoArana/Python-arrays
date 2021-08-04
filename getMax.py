def getGreatest(a, b, c):
    my_list = sorted([a, b, c])
    if my_list[1] == my_list[2]:
        return -1
    return my_list[2]

def getUserInput():
    num1 = int(input("Input the first number: "))
    num2 = int(input("Input the second number: "))
    num3 = int(input("Input the third number: "))

    largest = getGreatest(num1, num2, num3)
    if (largest == -1):
        print("They are equal")
    else:
        print(
            "The biggest number between ", num1, ", ", num2, "and ", num3, "is: ", largest)

if __name__ == "__main__":
    getUserInput()