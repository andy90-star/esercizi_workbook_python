#!/bin/python3
"""The file 144 is embedded here"""
def confront(first, second):
    lista_first = list(first)
    lista_second = list(second)
    lista_first.sort()
    lista_second.sort()
    if lista_first == lista_second:
        print("The words are anagrams")
    else:
        print("The words aren't anagrams")

def main():
    try:
        first = input("Enter the first word ").lower()
        second = input("Enter the first word ").lower()
        confront(first, second)
    except:
        print("Error, Repeat")
        main()


if __name__ == '__main__':
    main()