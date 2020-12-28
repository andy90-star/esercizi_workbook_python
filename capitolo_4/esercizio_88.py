#!/bin/python3
def median(c, lista, media):
    if c < 3:
        valori = int(input("Inserire valore numerico "))
        c += 1
        lista.append(valori)
        median(c, lista, media)
    else: 
        for i in lista:
            media += i 
        cal = media / 3
        print(cal)

def main():
    try:
        lista = []
        media = 0
        c = 0
        median(c, lista, media)
    except ValueError:
        print("Inserire valori numerici")
        main()

if __name__ == '__main__':
    main()