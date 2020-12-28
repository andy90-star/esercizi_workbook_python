#!/bin/python3
def controllo(a):
    dizio = {
        3  : "Triangolo",
        4  : "Quadrilatero",
        5  : "Pentagono",
        6  : "Esagono",
        7  : "Ettagono",
        8  : "Ottagono",
        9  : "Enagono",
        10 : "Decagono",
    }
    if a in dizio:
        print("Il poligono è un " + dizio.get(a))
def main():
    try:
        poligono = int(input("Quanti lati ha il tuo poligono "))
        controllo(poligono)
    except ValueError:
        print("Inserisci un valore di tipo int")
        main()

if __name__ == '__main__':
    main()