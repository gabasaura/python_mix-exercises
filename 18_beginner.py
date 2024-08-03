"""
IMPRIME PERO NO ES UN STRING.

sing = 0
while sing <= 10:
    if sing == 4:
        print("there will be an answer,")
    elif sing == 10:
        print("whisper words of wisdom, let it be")
    else:
        print("let it be,")
    sing += 1

print(sing)

"""
print("=====================================")


def sing():

    lyrics = ""
    for i in range(11):
        if i == 4:                
            lyrics += "there will be an answer,\n"
        elif i == 10:
            lyrics += "whisper words of wisdom, let it be"
        else:
            lyrics += "let it be,\n"
    print(lyrics)

sing()



"""
SOLUCION DE 4GEEK:

def sing():
    song = ""
    for i in range(11):
        if i == 4:
            song += "there will be an answer,\n"
        elif i == 10:
            song += "whisper words of wisdom, let it be"
        else:
            song += "let it be,\n"
    return song

sing()

"""
