#!/bin/python3
def main():
    lunghezza = float(input("Inserisci la lunghezza della stanza "))
    larghezza = float(input("Inserisci la lunghezza della stanza "))
    area = lunghezza * larghezza
    areap = area * 3.28
    print("ecco lel aree " + str(area) + " " + str(areap))


if __name__ == '__main__':
    main()
