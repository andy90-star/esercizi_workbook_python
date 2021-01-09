#!/bin/python3
import os
import random 
def names(file_1, file_2):
    file_find = os.path.abspath(file_1)
    file_find_1 = os.path.abspath(file_2)
    file_open = open(file_find, "r")
    file_open_1 = open(file_find_1, "r")
    list_file = list(file_open)
    list_file_1 = list(file_open_1)
    file_write = open("years.txt", "w")
    for index_years in range(0, 12):
        moment = random.randint(0, len(list_file)-1)
        file_write.write(list_file[moment])
    file_write.close()
    file_read_3 = open("years.txt", "r")
    list_3 = list(file_read_3)
    file_write_1 = open("years_f.txt", "w")
    for index_years_1 in range(0, 12):
        moment_1 = random.randint(0, len(list_file_1)-1)
        file_write_1.write(list_file_1[moment_1])
    file_write_1.close()
    file_read_4 = open("years_f.txt", "r")
    list_4 = list(file_read_4)
    print(list_3)
    print(list_4)

def main():
    try:
        file_1=("Enter the name of the file")
        file_2=("Enter the name of the file")
        names(file_1, file_2)
    except FileNotFoundError:
        print("File not found!")

if __name__ == '__main__':
    main()