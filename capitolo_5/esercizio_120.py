#!/bin/python3
def concaten(list_word):
    length = len(list_word)
    for i in list_word:
        if length == 1:
            print("and ", end=i)
        else:
            print(i, end=",")
            length -= 1

def main():
    list_word = list()
    boolean = True
    while boolean:
        word=input("Enter the words")
        if word == "":
            boolean = False
        else:
            list_word.append(word)
    concaten(list_word)


if __name__ == '__main__':
    main()