#!/bin/python3
def costo(a, b):
    if a > 140:
        a -= 140
        b += 0.25
        costo(a ,b)
    else:
        print(b)
    
def main():
    try:
        cost = 4.0
        lunghezza = int(input("Inserisci il valore "))
        costo(lunghezza, cost)
    except ValueError:
        print("Inserisci un valore int")
        main()
if __name__ == '__main__':
    main()