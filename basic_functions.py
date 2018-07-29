from random import randint
from helpers import *
from basic_functions import *
import time
import sys

def encrypt(passw):

    if passw=="":
        print("\nInvalid input entered, enter again: "),
        return encrypt(input())
    key = randint(1,26)


    passw = list(passw)

    for i in range(len(passw)):
        if passw[i].islower():
            passw[i] = 97 + ((ord(passw[i])-97)+key)%26
        elif passw[i].isupper():
            passw[i] = 65 + ((ord(passw[i])-65)+key)%26
        elif passw[i].isdigit():
            passw[i] = 48 + ((ord(passw[i])-48)+key)%10
    res = "".join([chr(x) for x in passw])
    f = open("keys.txt", "a")
    f.write("\n{} {}".format(key,"".join(res)))
    f.close()
    return res

def decrypt(passw,key):
    passw = list(passw)
    for i in range(len(passw)):
        if passw[i].islower():
            passw[i] = 97 + ((ord(passw[i])-97)-key)%26
        elif passw[i].isupper():
            passw[i] = 65 + ((ord(passw[i])-65)-key)%26
        elif passw[i].isdigit():
            passw[i] = 48 + ((ord(passw[i])-48)-key)%10

    res =  "".join([chr(x) for x in passw])
    return res

def decrypt_main():
    def inp_de():
        print("\nEnter encrypted value: "),

        while True:
            try:
                passw = str(input())
                if len(passw)<1:
                    return inp_de()
                break
            except:
                print("\nInvalid input")
                continue

        print("\nEnter offset of the encrypted value: "),

        while True:
            try:
                key = int(input())
                break
            except:
                print("\nInvalid input,number expected")
                continue
        return decrypt(passw,key)

    def list_de():
        f = open("keys.txt","r")
        l = [[pos+1,x] for pos,x in enumerate(f.read().split()[1::2])]
        f.seek(0)
        keys = [int(x) for x in f.read().split()[::2]]

        if len(l)==0:
            print("\nkeys.txt is empty, do you wish to decrypt from input? (y/n): "),
            while True:
                try:
                    x = str(input())
                    if x in ["y","yes","Y","YES"]:
                        print("\nDecrypted value:"),
                        slow_print(inp_de())
                        return

                    elif x in ["n","no","N","NO"]:
                        break
                except:
                    print("\nInvalid input")
                    continue


            print("\n")
            return

        print ("{} |{}".format("Pos","Encrypted value"))

        for x in l:
            print(x)
            time.sleep(0.05)

        for x in "Enter the position of value you wish to decrypt:":
            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(0.01)

        while True:
            try:
                x = int(input())-1
                key = keys[x]
                f.seek(0)
                line = f.readlines()[x+1]
                break
            except:
                print("\nInvalid position entered")
                for x in "Enter the position of value you wish to decrypt:":
                    sys.stdout.write(x)
                    sys.stdout.flush()
                    time.sleep(0.01)
                continue
        time.sleep(0.01)
        print("\nThe decrypted password is: "),
        for x in decrypt(l[x][1],key):
            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(0.075)

        print("\nDo you wish to delete the password from keys.txt? (y/n):"),
        while True:
            try:
                x = str(input())
                if x in ["y","yes","Y","YES"]:

                    f.seek(0)
                    lines = f.readlines()
                    f.close()

                    f = open("keys.txt","w")

                    for x in lines:
                        if x!=line:
                            f.write(x)
                    f.close()
                    break

                elif x in ["n","no","N","NO"]:
                    break
            except:
                print("\nInvalid input")
                continue

    print("\nDo you wish to decrypt value from list or from input?\n")
    time.sleep(0.1)
    print("1.List")
    time.sleep(0.1)
    print("2.Input")

    while True:
        x = int(input())

        if x == 1:
            list_de()
            print("\n")
            return

        elif x == 2:
            inp = inp_de()
            slow_print("\nDecrypted value: "),
            slow_print(inp,0.10)
            print("\n")
            return

        else:
            print("\nInvalid input entered, enter 1 or 2")
            continue