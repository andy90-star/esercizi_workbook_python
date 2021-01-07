#!/bin/python3
import os
def word_counter(file_enter, word):
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
    for index_complete in list_complete:
        if word == index_complete:
            counter_1 += 1
    print("The word " + word + " is present " + str(counter_1))
            
        
def main():
    try:
        file_enter=input("Enter the file name: ")
        word = input("Enter the word: ")
        word_counter(file_enter, word)
    except FileNotFoundError:
        print("File not found!")

if __name__ == '__main__':
    main()