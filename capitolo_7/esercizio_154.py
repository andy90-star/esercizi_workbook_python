#!/bin/python3
import os
def cripto(file_enter, confront):
    contator = 0
    list_complete = list()
    file_find = os.path.abspath(file_enter)
    file_open = open(file_find,"r")
    list_file = list(file_open)
    for counter in range(0, len(list_file)):
        moment = list()
        moment = list(list_file[counter])
        for index_moment in moment:
            if confront == index_moment:
                contator += 1
    print("The letter " + confront + " is present " + str(contator))

def main():
    file_enter=input("Enter the file name: ")
    confront = input("Enter the letter for the confront: ")
    cripto(file_enter, confront)

if __name__ == '__main__':
    main()