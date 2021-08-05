def esPrimo(n):
    cont = 2
    prime = True

    if n < 2:
        prime = False
    elif n >= 2:
        while cont < n and prime == True:
            if n % cont == 0:
                prime = False
            cont = cont + 1
    return prime
        
number = esPrimo(int(input("Ingrese un número: ")))

if number:
    print("El numero es primo")
else:
    print("El numero no es primo")
