#!/bin/python3
def main():
    vocali = ["a","b","i","o","u"]
    lettera = input("Inserisci la vocale ")
    for i in vocali:
        if lettera == i:
            print(lettera + " è una vocale")
            break
        elif lettera != i:
            print(lettera + " è una consonante")
            break
    

if __name__ == '__main__':
    main()