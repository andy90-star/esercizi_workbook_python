#!/bin/python3
def center(word):
    columns = 128
    length = (columns/2)-len(word)
    print(" " * int(length), word)
def main():
    word=input("Enter the word: ")
    center(word)
if __name__ == "__main__":
    main()