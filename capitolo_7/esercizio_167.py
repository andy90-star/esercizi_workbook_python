#!/bin/python3
import os
def ortography(file_1):
    i = 0
    cont = 0
    list_word_know = ["ciao", "a","tutti","", "io","sono","il","vostro", "aiutante", "controllo", "la","vostra","grammatica", "felice", "di", "aiutarvi"]
    name = ""
    list_moment = list()
    file_path = os.path.abspath(file_1)
    file_open = open(file_path, "r")
    list_file = list(file_open)
    for letter_2 in list_file:
        for letter in letter_2:
            if letter != "," and letter != "\n" and letter != " ":
                name+=letter
            elif letter == "," or letter == " ":
                list_moment.append(name)
                name=''
    length = len(list_word_know)-1
    for letter_2 in list_moment:
        if i <length:
            if letter_2 != list_word_know[i]:
                cont+=1
                i+=1
            else:
                i+=1

    print(list_moment)
    print(cont)
def main():
    file_1 = input("Enter the name of the file: ")
    ortography(file_1)

if __name__ == '__main__':
    main()
