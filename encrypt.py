from random import randint

def encrypt(entry):

    if entry=="":
        print("\nInvalid input entered, enter again: "),
        return encrypt(input())
    key = randint(2,26)
    entry = list(entry)

    for i in range(len(entry)):
        if entry[i].islower():
            entry[i] = 97 + ((ord(entry[i])-97)+key)%26
        elif entry[i].isupper():
            entry[i] = 65 + ((ord(entry[i])-65)+key)%26
        elif entry[i].isdigit():
            entry[i] = 48 + ((ord(entry[i])-48)+key)%10
        elif entry[i] == " ":
            entry[i] = ord("_")
        else:
            entry[i] = ord(entry[i])

    res = "".join([chr(x) for x in entry])
    return key,res
