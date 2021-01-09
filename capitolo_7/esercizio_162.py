#!/bin/python3
import os
def element(file_1, dicto):
    file_find = os.path.abspath(file_1)
    file_open = open(file_find, "r")
    list_file = list(file_open)
    for index in list_file:
            for counter in range(0, len(index)):
                index[counter]
                if index[counter] in dicto:
                    dicto[index[counter]] += 1
    for index_dicto in dicto:
        print(index_dicto + ": " + str(dicto.get(index_dicto)))
def main(dicto):
    file_1 = input("Enter the name of the file: ")
    element(file_1, dicto)

if __name__ == '__main__':
    dicto = {
        "a":0,
        "b":0,
        "c":0,
        "d":0,
        "e":0,
        "f":0,
        "g":0,
        "h":0,
        "i":0,
        "j":0,
        "k":0,
        "l":0,
        "m":0,
        "n":0,
        "o":0,
        "p":0,
        "q":0,
        "r":0,
        "s":0,
        "t":0,
        "u":0,
        "v":0,
        "w":0,
        "x":0,
        "y":0,
        "z":0,

    }
    main(dicto)