#!/bin/python3
def verifica(valore, neri, bianchi):
    for i in neri:
        if valore.startswith(i):
            prova = list(valore)
            if int(prova[1]) % 2 == 0 and int(prova[1]) < 8:
                print("Il quadrato è nero")
            elif int(prova[1]) > 8:
                print("valore non riconosciuto")
            else:
                print("Valore è bianco")
                break
    for i in bianchi:
        if valore.startswith(i):
            prova = list(valore)
            if int(prova[1]) % 2 == 1 and int(prova[1]) < 8:
                print("Il quadrato è bianco")
            
            else:
                print("Valore è nero")
                break
        
def main():
    try:
        neri = ["a","c","e","g"]
        bianchi = ["b","d","f","h"]
        valore = input("Inserisci il valore es:b4; ")
        verifica(valore, neri, bianchi)
    except ValueError:   
        print("Inserisci un valore come: b3,a6,c6")
        main()


if __name__ == '__main__':
    main()