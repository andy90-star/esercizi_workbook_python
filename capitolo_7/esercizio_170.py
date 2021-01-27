#!/bin/python3
import os
def comment(list_file):
    cont = 0
    if len(list_file) == 2:
        file_path = os.path.abspath(list_file[0])
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
            if letter.startswith("#"):
                cont+= 1
        print("In this file there are:", cont, list_file[0])
    elif len(list_file) > 2:
        for file_1 in list_file:
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
                if letter.startswith("#"):
                    cont+= 1
            print("In this file there are:", cont, file_1)
def main():
    try:
        list_file = list()
        boolean = True
        while boolean:
            file_find = input("Enter the words sensitive, If you want end digit stop: ").lower()
            list_file.append(file_find)
            if file_find == "stop" or file_find == "Stop" or file_find == "STOP":
                boolean = False
        comment(list_file)
    except FileNotFoundError:
        print("A file isn't found, you control")
if __name__ == '__main__':
    main()