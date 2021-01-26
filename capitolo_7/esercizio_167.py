#!/bin/python3
import os
def spell(file_1):
    name = ""
    #list_final = list()
    list_moment = list()
    list_finally = list()
    file_path = os.path.abspath(file_1)
    file_open = open(file_path, "r")
    list_file = list(file_open)
    for letter_2 in list_file:
        for letter in letter_2:
            if letter != "," and letter != "\n" and letter != " ":
                name+=letter
            elif letter == ",":
                list_moment.append(name)
                name=''
    for letter in list_moment:
        if not letter in list_finally:
            cont = list_moment.count(letter)
            print(letter, ": ", cont)
            list_finally.append(letter)
        
def main():
    file_1 = input("Enter the name of the file: ")
    spell(file_1)

if __name__ == '__main__':
    main()