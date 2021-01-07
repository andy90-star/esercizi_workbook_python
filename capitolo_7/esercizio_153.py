#!/bin/python3
import os
def longest(file_find,control):
    find = os.path.abspath(file_find)
    file_open = open(find, "r")
    list_file = list(file_open)
    control = list_file[0]
    print(control)
    for index_list in list_file:
        if len(control) < len(index_list):
            control = index_list
    print("the name longest is " + control)
def main():
    control = ""
    file_find = input("Enter the file name ")
    longest(file_find, control)

if __name__ == '__main__':
    main()