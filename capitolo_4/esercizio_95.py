#!/bin/python3
def change(word):
    cont =0
    list_word = list(word)
    list_new = list()
    for i in range(0, len(list_word)):
        if list_word[i] != " ":
            list_new.append(list_word[i].upper())
            break

    for letter in word[1:]:
        if letter == "." :
            cont += 1
            list_new.append(letter)
            continue
        elif cont == 1:
            moment = letter.upper()
            list_new.append(moment)
            cont = 0
        else:
            list_new.append(letter)
    return list_new

def change_i(list_new):
    cont = 0
    port = 0
    for letter in list_new[1:]:
        if letter == " ":
            cont += 1
            continue
        elif letter == "i" and cont == 1:
            port = list_new.index(letter)
            c = letter.upper()
            list_new[port] = c
        else:
            cont = 0
    string = "".join(list_new)
    return string

def main():
    try:
        word=input("Enter the sentence")
        first = change(word)
        second = change_i(first)
        print(second)
    except ValueError:
            print("Error value")
if __name__ == "__main__":
    main()