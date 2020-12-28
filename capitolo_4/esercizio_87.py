#!/bin/python3
def shipping(a, cal, c):
    FIRST_ORDER = 10.95
    ORDER = 2.95
    if c == a:
        cal += FIRST_ORDER
        c -= 1
        shipping(a,cal,c)
    elif c == 0:
        print("Costo totale " + str(round(cal, 3)))
    elif c < a:
        cal += ORDER
        c -= 1
        shipping(a,cal,c)
    
    
def main():
    try:
        cal = 0.0
        items = int(input("Quanti articoli hai ascquistato?"))
        pop = items
        shipping(items, cal, pop)
    except ValueError:
        print("Inserisci un valore tipo int")
        main()
if __name__ == '__main__':
    main()