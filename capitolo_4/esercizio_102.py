#!/bin/python3
from esercizio_100 import password_generate
def check():
    cont = 0
    password = password_generate()
    print(password)
    for letter in password[0:]:
        if letter == letter.upper():
            cont += 1
            break
    for letter in password[cont:]:
            try:
                if int(letter):
                    cont += 1
                    break
            except ValueError:
                continue
    if cont == 2:
        print("Strong")
        return True
if __name__ == "__main__":
    check()