#!/bin/python3
def provo():
        print("per usscire ricordiamo di digitare 0")
        numero = int(input("Inserisci il numero "))
        if numero == 0:
            return 
        elif numero%2 == 0:
            print("il numero è pari ")
            provo()
        elif numero%2 != 0:
            print("Numero dispari ")
            provo()
def main():
    try:
        provo()
    except ValueError:
        print("Inserisci un valore di tipo int ")
        main()
if __name__ == '__main__':
    main()