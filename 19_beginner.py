
print("====================================")

def number_of_bottles():
    song = ""
    number = 10

    while number > 0:
        if number == 1:
            song += "1 bottle of milk on the wall, 1 bottle of milk. Take one down and pass it around, no more bottles of milk on the wall.\n"
        elif number == 2:
            song += "2 bottles of milk on the wall, 2 bottles of milk. Take one down and pass it around, 1 bottle of milk on the wall.\n"
        else:
            song += f"{number} bottles of milk on the wall, {number} bottles of milk. Take one down and pass it around, {number - 1} bottles of milk on the wall.\n"
        
        number -= 1
        
    song += "No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall."

    print(song)

number_of_bottles()

"""
SOLUCION 4GEEK
"""
print("====================================")

def number_of_bottles():
    for x in range(10,2,-1):
        print(str(x) + " bottles of milk on the wall, " + str(x) + " bottles of milk. Take one down and pass it around, " + str(x-1)+ " bottles of milk on the wall.")
    print("2 bottles of milk on the wall, 2 bottles of milk. Take one down and pass it around, 1 bottle of milk on the wall.")
    print("1 bottle of milk on the wall, 1 bottle of milk. Take one down and pass it around, no more bottles of milk on the wall.")
    print("No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall.")
    return None

number_of_bottles()
