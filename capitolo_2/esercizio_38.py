#!/bin/python3
def main():
    try:
        lati = int(input("Quanti lati vuoi inserire ?"))
        dizionario = {
            3 : "triangolo",
            4 : "quadrilatero",
            5 : "penatagono",
            6 : "esagono",
            7 : "ettagono",
            8 : "ottagono",
            9 : "ennagono",
            10 : "decagono"
        }
        if lati in dizionario:
            print("Il tuo poligono è un " + dizionario.get(lati))
        elif lati is not dizionario:
            print("poligono non presente")   
            main()     
    except ValueError:
        print("inserire un valore di tipo int")
        main()
if __name__ == '__main__':
    main()