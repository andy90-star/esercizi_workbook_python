#!/bin/python3
import os
def chemical(number):
    file_1 = os.path.abspath("chemical.txt")
    file_open = open(file_1, "r")
    list_file = list(file_open)
    for letter in list_file:
        if letter.startswith(number):
            return letter 
def main():
    number = input("Enter the number:  min=1; max=29: ")
    first = chemical(number)
    print(first)

if __name__ == '__main__':
    main()