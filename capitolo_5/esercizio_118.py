#!/bin/python3
def polindromo(word):
    i = 0
    sente = ""
    lista = list(word)
    lista3 = list()
    lista.reverse()
    for index in lista:
        if index == word[i]:
            lista3.append(index)
            i +=1
    print("the name", word, "is polindrome")
    


def main():
    try:
        word = input("Enter the word")
        polindromo(word)
    except ValueError:
        print("Enter type of str!")


if __name__ == '__main__':
    main()