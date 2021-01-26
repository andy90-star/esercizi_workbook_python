#!/bin/python3
import os
def list_name(file_1, file_2):
    name=""
    list_final = list()
    list_final_girls = list()
    list_boy = list()
    list_girl = list()
    file_1_1 =os.path.abspath(file_1)
    file_2_2 =os.path.abspath(file_2)
    file_boy_open = open(file_1, "r")
    file_girl_open = open(file_2, "r")
    for letter_2 in file_boy_open:
        for letter in letter_2:
            if letter != "," and letter != "\n" and letter != " ":
                name+=letter
            elif letter == ",":
                list_boy.append(name)
                name=''
    for letter in list_boy:
        if not letter in list_final:
            list_final.append(letter)
        elif letter in list_final:
            continue

    name=''
    for letter_2 in file_girl_open:
        for letter in letter_2:
            if letter != "," and letter != "\n" and letter != " ":
                name+=letter
            elif letter == ",":
                list_girl.append(name)
                name=''
    for letter in list_girl:
        if not letter in list_final_girls:
            list_final_girls.append(letter)
        elif letter in list_final_girls:
            continue

    
    return list_final, list_final_girls

def main():
    file_1 = input("Enter the male file: ")
    file_2 = input("Enter the male file: ")
    first = list_name(file_1, file_2)
    print(first)

if __name__ == '__main__':
    main()