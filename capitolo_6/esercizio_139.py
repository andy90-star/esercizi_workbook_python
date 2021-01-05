#!/bin/python3
def main():
    a = ""
    dicto_letter = {
        "A" : ".-",
        "B" : "-...",
        "C" : "-.-.", 
        "D" : "-..", 
        "E" : ".", 
        "F" : "..-.", 
        "G" : "--.", 
        "H" : "....", 
        "I" : "..", 
        "J" : ".---", 
        "K" : "-.-", 
        "L" : ".-..", 
        "M" : "--", 
        "N" : "-.",
        "O" : "---", 
        "P" : ".--.", 
        "Q" : "--.-", 
        "R" : ".-.", 
        "S" : "...", 
        "T" : "-", 
        "U" : "..-", 
        "V" : "...-", 
        "W" : ".--", 
        "X" : "-..-", 
        "Y" : "-.--", 
        "Z" : "--..",
        " " : "_",
        "." : "."
    }
    sentence = input("Enter the semtence ").upper() 
    list_sentence = list(sentence)
    print(list_sentence)
    for i in list_sentence:
        print(i)
        if i in dicto_letter:
            a += dicto_letter.get(i)
    print(a)
if __name__ == '__main__':
    main()