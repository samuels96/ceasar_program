from helpers import *
from basic_functions import *
import time
import sys

def main():
    print("\nDo you wish to encrypt new entry or decrypt existing one?\n")
    time.sleep(0.1)
    print("1.Encrypt")
    time.sleep(0.1)
    print("2.Decrypt: "),
    while True:
        try:
            x = int(input())
            if x == 1:
                sys.stdout.write("Enter entry you wish to be encrypted: "),
                res = encrypt(str(input()))
                print ( "\nEncrypted: {}".format(res))
                time.sleep(0.05)
                slow_print("\nEncrypted entry saved to keys.txt\n",0.02)
                main()
            if x == 2:
                decrypt_main()
                main()
            else:
                print("Invalid input entered, enter 1 or 2")
                continue
        except:
            print("Invalid input entered, enter 1 or 2")
            continue


if __name__ == "__main__":
    main()
