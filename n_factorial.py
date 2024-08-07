def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1 # Declarar variable result   
    for i in range(1, n + 1): # n + 1 porque loop inicia desde 0.
        result *= i
    return result 

print(factorial(5)) 

"""
factorial: producto de todos los números enteros positivos desde 1 hasta n
n. 
n! = n * (n - 1) * (n - 2) * ...n 
5! = 5 *    4    *    3     * 2 * 1 = 120
"""