#!/bin/python3
import random
def main():
    licens = ""
    letters = random.randint(3,4)
    for _ in range(0, letters):
        letter = random.randint(97,122)
        letter_1 = chr(letter)
        licens += letter_1
    for _ in range(0,3):
        number = random.randint(1,9)
        licens += str(number)
    print(licens)

if __name__ == "__main__":
    main()