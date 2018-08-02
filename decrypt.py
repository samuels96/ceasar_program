

def decrypt(entry,key):
    entry = list(entry)
    for i in range(len(entry)):
        if entry[i].islower():
            entry[i] = 97 + ((ord(entry[i])-97)-key)%26
        elif entry[i].isupper():
            entry[i] = 65 + ((ord(entry[i])-65)-key)%26
        elif entry[i].isdigit():
            entry[i] = 48 + ((ord(entry[i])-48)-key)%10
        elif entry[i] == "_":
            entry[i] = ord(" ")
        else:
            entry[i] = ord(entry[i])

    res =  "".join([chr(x) for x in entry])
    return res
