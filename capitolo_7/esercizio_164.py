#!/bin/python3
import os
def name(year):
    file_1 = os.path.abspath("names.txt")
    file_open = open(file_1, "r")
    list_open = list(file_open)
    for letter in list_open:
        if letter.startswith(year):
            return letter
def main():
    year = input("Enter the year: ")
    first = name(year)
    print(first)

if __name__ == '__main__':
    main()