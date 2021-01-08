#!/bin/python3
import os
def longest(file_enter):
    counter_1 = 0
    list_prove = list()
    list_complete = list()
    file_find = os.path.abspath(file_enter)
    file_open = open(file_find, "r")
    list_file = list(file_open)
    for counter in range(0, len(list_file)):
        string = ""
        moment = list()
        moment = list(list_file[counter])
        for index_moment in moment:
            if index_moment != " ":
                string += index_moment
            elif index_moment == " ":
                list_complete.append(string)
                string = ""
        word_plus = list_complete[0]
    for index_word in list_complete:
        if len(word_plus) < len(index_word):
            word_plus = index_word
    print("The word longest is " + word_plus)


def main():
    try:
        file_enter=input("Enter the file name: ")
        longest(file_enter)
    except FileNotFoundError:
        print("File not found!")

if __name__ == '__main__':
    main()