#!/bin/python3
import random
def password_generate():
    password =""
    ran = random.randint(7,10)
    for _ in range(0,ran):
        moment= random.randint(33,126)
        letter = chr(moment)
        password += letter
    return password
def main():
    first = password_generate()
    print(first)

if __name__ == "__main__":
    main()