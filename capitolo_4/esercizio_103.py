#!/bin/python3
from esercizio_102 import check
from esercizio_100 import password_generate

def main():
    cont_1 = 0
    boolean = True
    while boolean:
        response = check()
        if response == True:
            print("After",cont_1,"times")
            boolean=False
        else:
            cont_1 += 1


if __name__ == "__main__":
    main()
