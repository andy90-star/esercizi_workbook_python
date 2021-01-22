#!/bin/python3
from esercizio_122 import latin
def latin_1(word_1):
    list_exce = ["?","!","'",".","-","_","+",","]
    list_word = list(word_1)
    for exce in list_exce:
        for letter in list_word:
            if letter == exce:
                list_word.remove(letter)
                list_word.append(exce)
    print(list_word)
                
    
def main():
    word = input("Enter the word: ")
    word_1 = latin(word)
    latin_1(word_1)
    

if __name__ == "__main__":
    main()