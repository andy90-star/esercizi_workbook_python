#!/bin/python3
import os
import random
def names(file_1):
    file_find = os.path.abspath(file_1)
    file_open = open(file_find, "r")
    list_file = list(file_open)
    for index in  list_file:
        print(index)

def main():
    try:
        file_1=input("Enter the years")
        file_1 += ".txt"
        names(file_1)
    except FileNotFoundError:
        print("The years not found!")

if __name__ == '__main__':
    main()