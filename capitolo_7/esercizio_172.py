#!/bin/python3
import os
def find(file_1):
    file_path = os.path.abspath(file_1)
    file_open = open(file_path, "r")
    list_file_1 = list(file_open)
    list_moment = list()
    name =''
    for letter_2 in list_file_1:
        for letter in letter_2:
            if letter != "," and letter != "\n" and letter != " " and letter != "":
                name+=letter
            elif letter == "," or letter == " ":
                list_moment.append(name)
                name=''
def main():
    try:
        file_1 = input("Enter the name of the file: ")
        find(file_1)
    except FileNotFoundError:
        print("Enter the name of the file: ")

if __name__ == '__main__':
    main()