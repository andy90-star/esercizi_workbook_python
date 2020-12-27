#!/bin/python3
def conversione(anni, conta, b, età):
    if conta != anni and b < 2:
        età += 10
        conta += 1
        b +=1
        conversione(anni, conta, b, età)
    if conta != anni and b >= 2:
        età += 4
        conta += 1
        b += 1
        conversione(anni, conta, b, età)
    elif conta == anni:
        età += 1
        return print(età)

def main():
    try:
        b = 0
        età  = 0
        conta = 0
        anni = int(input("Inserire l'età "))
        conversione(anni, conta, b, età)
    except ValueError:
        print("inserisci un valore di tipo int")
        main()
if __name__ == '__main__':
    main()