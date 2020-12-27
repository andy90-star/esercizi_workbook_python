#!/bin/python3
def conversione_metri(a,b):
    a /= 3.28
    b /= 3.28
    return print("Ecco i valori convertiti in metri: \n" + str(a) +" " + str(b) + "\n")
def conversione_acri(area):
    area /=  4047
    return print("ecco l'area in acri\n" + str(area))


def main():
    try:    
        lunghezza = float(input("Inserisci la lunghezza in piedi "))
        larghezza = float(input("Inserisci la lunghezza in piedi "))
        conversione_metri(lunghezza, larghezza)
        area = lunghezza * larghezza
        conversione_acri(area)
    except ValueError:
        print("accetto solo valori float ")
        main()

if __name__ == '__main__':
    main()
