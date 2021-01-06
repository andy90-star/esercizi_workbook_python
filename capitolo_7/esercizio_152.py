#!/bin/python3
import os
def control(file_know, counter):
    list_per = list()
    find = os.path.abspath(file_know)
    opene = open(find, "r")
    list_file = list(opene)
    lung = len(list_file)
    print(lung)
    file_open = open("nuovo.txt", "w")
    #for i in range(0, lung):
    for index_list in list_file:
        count = str(counter)
        count += "; " + index_list
        file_open.write(count)
        counter += 1
    file_open.close()
            


def main():
    try:
        counter = 1
        file_know=input("Enter the file name ")
        control(file_know, counter)
    except FileNotFoundError:
        print("File non trovato")

if __name__ == '__main__':
    main()