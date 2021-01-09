#!/bin/python3
import os 
import random
def plus(file_1):
    index = 3
    concaten = ""
    file_find=os.path.abspath(file_1)
    file_open=open(file_find, "r")
    list_file=list(file_open)
    print(list_file)
    for index_file in range(0, len(list_file)):
        casual = random.randint(0, len(list_file)-1)
        concaten += list_file[casual]
        if index == 3:
            concaten = concaten[0:index]
            concaten = concaten.upper()
        elif index == 8:
            concaten = concaten[0:index]
        index += 5
        if index > 8:
            break
    print(concaten)
        
    
def main():
    file_1=input("Enter the name of the file: ")
    plus(file_1)

if __name__ == '__main__':
    main()