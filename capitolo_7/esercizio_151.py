#!/bin/python3
import os
def leggo(a, b):
    inserire = input("Inserisci il nome del file ")
    a.append(inserire)
    if inserire == "0":
        a.pop(-1)
        for i in a:
            raccolta = os.path.abspath(i)
            b.append(raccolta)
        for i in b:
            apriamo = open(i, "r")
            lista = list(apriamo)
            for i in range(1, len(lista)):
                print(lista[i])
        return
    leggo(a, b)

def main():
    path =[]
    nomi = []
    leggo(nomi, path)
    
    
if __name__ == '__main__':
    main()