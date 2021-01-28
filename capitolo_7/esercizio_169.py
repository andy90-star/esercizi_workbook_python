#!/bin/python3
import os
def sensitive(file_1, list_word_sensitive):
    cont = 0
    file_path = os.path.abspath(file_1)
    file_open = open(file_path, "r")
    list_file = list(file_open)
    list_moment = list()
    name =''
    for letter_2 in list_file:
        for letter in letter_2:
            if letter != "," and letter != "\n" and letter != " ":
                name+=letter
            elif letter == "," or letter == " ":
                list_moment.append(name)
                name=''
    for letter in list_moment:
        for sensitive in list_word_sensitive:
            if sensitive == letter:
                moment = list_moment.index(letter)
                list_moment.remove(letter)
                list_moment.insert(moment, "*****")
    file_write = open("new_file.txt", "w")
    for letter in list_moment:
        cont += 1
        if cont == 4:
            letter = "\n" + letter + " "
            cont = 0 
        else:
            letter = letter + " " 
        file_write.write(letter)
    file_write.close()
    return list_moment
def main():
    try:
        file_1 = input("Enter the name of the file: ")
        list_word_sensitive = list()
        boolean = True
        while boolean:
            word = input("Enter the words sensitive, If you want end digit stop: ").lower()
            list_word_sensitive.append(word)
            if word == "stop" or word == "Stop" or word == "STOP":
                list_word_sensitive.append(word)
                boolean = False
        first = sensitive(file_1, list_word_sensitive)
        print(first)
    except FileNotFoundError:
        print("File not found")

if __name__ == '__main__':
    main()