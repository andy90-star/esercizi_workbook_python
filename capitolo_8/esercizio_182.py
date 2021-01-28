#!/bin/python3
import os
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
        if len(letter) == 2 or  len(letter) == 1:
            list_final.append(letter)
    return list_final

def chimical(word, first,cont,final,length, list_word):
    letteral = list_word[cont]
    if  letteral.upper() in first and length > 1:
        letter = letteral.upper()
        moment = first.index(letter)
        final += first[moment].upper()
        cont += 1
        length -= 1
        chimical(word, first,cont,final, length, list_word)
    elif not list_word[cont] is first and length > 1:
        final += letteral.lower()
        cont += 1
        length -= 1
        chimical(word, first,cont,final,length,list_word)
    else:
        if list_word[-1] in first:
            letter= list_word[-1]
            moment = first.index(letter)
            final += first[moment]
        else:
            final += list_word[-1]
        print(final)




def main():
    final = ""
    cont = 0
    word = input("Enter the sentence: ")
    length = len(word)
    first = remove(word)
    list_word = list(word)
    print(first)
    chimical(word, first, cont,final,length, list_word)
if __name__ == '__main__':
    main()