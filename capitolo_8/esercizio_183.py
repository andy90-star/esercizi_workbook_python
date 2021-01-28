#!/bin/python3
import os, time
def remove(word):
    list_final = list()
    file_path = os.path.abspath("chimical.txt")
    file_open = open(file_path, "r")
    list_file = list(file_open)
    list_moment = list()
    name =''
    for letter_2 in list_file:
        for letter in letter_2:
            if letter != "," and letter != "\n" and letter != " " and letter != "\t" and letter != "2" and letter != "1"and letter != "3"and letter != "4"\
                and letter != "5"and letter != "6"and letter != "7"and letter != "8" and letter != "9" and letter != "0":
                name+=letter
            elif letter == "," or letter == " ":
                list_moment.append(name)
                name=''
    for letter in list_moment:
        if len(letter) > 2:
            list_final.append(letter)
    return list_final
def element_sequence(word, first, cont):
    if not word in first:
        print("Element isn't present: ")
    elif word in first:
        letter = word[-1].upper()
        moment = first[cont]
        if moment.startswith(letter):
            print(first[cont])
            word = first[cont]
            cont += 1
            element_sequence(word, first, cont)
        else:
            cont+= 1
            element_sequence(word, first, cont)


def main():
    try:
        cont= 0
        word=input("Enter the word: ")
        element = word[0].upper()
        fine = element + word[1:]
        first = remove(word)
        element_sequence(fine,first, cont)
    except IndexError:
        print("Finish !")
if __name__ == '__main__':
    main()