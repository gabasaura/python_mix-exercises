from math import factorial

def pascal(filas): # n = numero de filas
    for n in range(filas): 
        # loop filas
        for j in range(filas - n + 1):
            print(end = ' ')
        for r in range(n + 1): 
        # loop piramide
            numero = factorial(n) / (factorial(n - r) * factorial(r))
            print(int(numero), end = ' ')
        # salto de linea
        print()


print(pascal(5))