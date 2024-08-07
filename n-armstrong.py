def num_arms(num):
    num_to_str = str(num)
    suma = 0
    for i in range(len(num_to_str)):
        suma = suma + (int(num_to_str[i]) ** len(num_to_str))
    return suma

# print(num_arms(153))


# 153 = 1**3 3**3 5**3 = 1 + 125 + 27 = 153

def num_narciso(num):
    n_str = str(num)
    suma = 0
    for i in n_str:
        suma += int(i) ** len(n_str)
    return suma

print(num_narciso(153))
    