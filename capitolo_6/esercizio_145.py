#!/bin/python3
def point(word, contator):
    dicto_point = {
    "A" : 1,
    "B" : 3,
    "C" : 3,
    "D" : 2,
    "E" : 1,
    "F" : 4,
    "G" : 2,
    "H" : 4,
    "I" : 1,
    "J" : 8,
    "K" : 5,
    "L" : 1,
    "M" : 3,
    "N" : 1,
    "O" : 1,
    "P" : 3,
    "Q" : 10,
    "R" : 1,
    "S" : 1,
    "T" : 1,
    "U" : 1,
    "V" : 4,
    "W" : 4,
    "X" : 8,
    "Y" : 4,
    "Z" : 10,
    }
    lista_word = list(word)
    for index_word in lista_word:
        if index_word in dicto_point:
            contator += dicto_point.get(index_word)
    print("score: " + str(contator))



def main():
    try:
        contator = 0
        word = input("Enter the name ").upper()
        point(word, contator)
    except ValueError or TypeError as error:
        print(error)
        

if __name__ == '__main__':
    main()