from decrypt import *
from encrypt import *
from builtins import input
import os,sys,time

def refresh():
    os.system('cls' if os.name in "nt" else "clear")

def en():
    refresh()
    print("Enter the text you wish to encrypt\n")
    f = open("keys.txt", "a")
    inp = encrypt(str(input("> ")))
    f.write("{} {}\n".format(inp[0],inp[1]))
    f.close()
    print("\n\t" + inp[1] + " saved to keys.txt...\n")
    time.sleep(1)
    refresh()


def de():
    file = open("keys.txt","a+")
    text = [[pos+1,x] for pos,x in enumerate(file.read().split()[1::2])]
    file.seek(0)
    keys = [int(x) for x in file.read().split()[::2]]

    if len(text)==0:
        print("Keys.txt is empty, text has to be encrypted first...")
        time.sleep(1)
        en()
        de()

    else:
        print ("\t{} |{}".format("Pos","Encrypted value"))
        for x in text:
            print("\t{}".format(x))
        print("\nEnter the position of text you wish to be decrypted\n")

        while True:
            try:
                inp = int(input("> "))-1
                file.seek(0)
                line = file.readlines()[inp]
                break
            except:
                continue
        print("\nThe decrypted text is: {}".format('\033[1m+'+decrypt(text[inp][1],keys[inp])+'\033[0m'))

        while True:
            inp = input("\nDo you wish to delete the text from keys.txt? (Y/N) > ")
            if inp in ["y","Y","YES","no"]:
                file.seek(0)
                lines = file.readlines()
                file.close()

                file = open("keys.txt","w")
                for x in lines:
                    if x!=line:
                        file.write(x)
                file.close()
                print("\nEntry deleted from keys.txt")
                break
            elif inp in ["n","N","NO","no"]:
                break
            else:
                continue

    time.sleep(1)
    refresh()

def main():
    print("\nDo you wish to encrypt or decrypt?\n1.Encrypt\n2.Decrypt\n")

    while True:
        choice = input("> ")
        if choice not in ["1","2"]:
            refresh()
            main()

        elif choice == "1":
            en()
            main()

        else:
            refresh()
            de()
            main()

if __name__ == "__main__":
    main()
