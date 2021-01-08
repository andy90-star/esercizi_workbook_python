#!/bin/python3
import os
def remove(file_1):
    counter_2 = 0
    counter_1 = 0
    list_prove = list()
    list_complete = list()
    file_find = os.path.abspath(file_1)
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
    for index_moment in list_complete:
            if index_moment == " " or index_moment == "":
                list_complete.pop(counter_2)
                counter_2 += 1
            else:
                counter_2 +=1
    counter_2  =0
    for index_moment in list_complete:
        if index_moment.startswith("#"):
            list_complete.pop(counter_2)
            counter_2 += 1
        else:
            counter_2 += 1
            
    print(list_complete)



def main():
    try:
        file_1=input("Enter the  name of the file: ")
        remove(file_1)
    except FileNotFoundError:
        print("file not found!")

if __name__ == '__main__':
    main()