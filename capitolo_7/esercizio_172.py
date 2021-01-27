#!/bin/python3
import os
def find(file_1):
    cont = 0
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
    for letter in list_moment:
        for letterr in letter:
            if letterr == "a":
                cont += 1
            elif letterr == "e" and cont == 1:
                cont+=1
            elif letterr == "i" and cont == 2:
                cont+=1
            elif letterr == "o" and cont == 3:
                cont+=1
            elif letterr == "u" and cont == 4:
                cont+=1
            elif letterr == "y" and cont == 5:
                print(letter)
                cont = 0
def main():
    try:
        file_1 = input("Enter the name of the file:")
        find(file_1)
    except FileNotFoundError:
        print("File not found! ")

if __name__ == '__main__':
    main()