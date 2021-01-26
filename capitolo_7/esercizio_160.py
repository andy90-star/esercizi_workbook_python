#!/bin/python3
import os
def control(file_1):
    list_rule = list()
    file_moment = os.path.abspath(file_1)
    file_open = open(file_moment, "r")
    list_file = list(file_open)
    for index in range(0, len(list_file)):
        list_moment = list_file[index]
        for letter in range(0,len(list_moment)-1):
            if list_moment[letter] == "c" and list_moment[letter+1] == "e" and list_moment[letter+2] == "i":
                list_rule.append(list_file[index])
                break
    return list_rule
def main():
    try:
        file_1 = input("Enter the name of the file: ")
        first = control(file_1)
        print("these are the words with the rule:", first)
    except FileNotFoundError:
        print("File not found!")
if __name__ == '__main__':
    main()