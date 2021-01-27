#!/bin/python3
def isPolindrome(word, cont, length,cont_2): 
    if word[cont] == word[cont_2]:
        cont+=1
        cont_2 -=1
        print(cont, length)
        if cont == length:
            print("yes, the word is polindrome")
        else:
            isPolindrome(word,cont,length, cont_2)
    else:
        print("The word isn't polindrome")

def main():
    cont = 0
    word = input("Enter the word:")
    length = len(word)-1
    cont_2 = length
    isPolindrome(word, cont, length, cont_2)
if __name__ == '__main__':
    main()
