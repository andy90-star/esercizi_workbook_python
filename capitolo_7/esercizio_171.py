#!/bin/python3
import os
def margin_display(file_1):
    list_final = list()
    terminal = 160
    file_path = os.path.abspath(file_1)
    file_open = open(file_path, "r")
    list_file_1 = list(file_open)
    list_moment = list()
    name =' '
    for letter_2 in list_file_1:
        for letter in letter_2:
            if letter != "," and letter != "\n" and letter != " " and letter != "":
                name+=letter
            elif letter == "," or letter == " ":
                list_moment.append(name)
                name=''
    for letter in list_moment:
        terminal = terminal - len(letter)
        if  terminal > 80:
            list_final.append(letter)
        elif terminal <= 80:
            letter += "\n"
            list_final.append(letter)
            terminal = 160
    final=" ".join(list_final)
    print(final)
            


def main():
    try:
        file_1 = input("Enter the name of the file: ")
        margin_display(file_1)
    except FileNotFoundError:
        print("File not found! ")
if __name__ == '__main__':
    main()