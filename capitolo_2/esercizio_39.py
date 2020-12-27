#!/bin/python3
def main():
    dizio = {
        "gennaio" : 31,
        "febbrario" : 29,
        "marzo" : 31,
        "aprile" : 30,
        "maggio" : 31,
        "giugno" : 31,
        "luglio" : 31,
        "agosto" : 31,
        "settembre" : 30,
        "ottobre" : 31,
        "novembre" : 30,
        "dicembre" : 31,
    }
    mese = input("Inserire il mese ").lower()
    if mese in dizio:
        print("Il mese " + mese + " è composto da " + str(dizio.get(mese)))
    else :
        print("Quando non inserisci il nome viene usata una funzione ricorsiva")
        main()
if __name__ == '__main__':
    main()