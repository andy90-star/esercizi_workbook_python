#!/bin/python3
import os
def leggo(a):
    trova = os.path.abspath(a)
    opene = open(trova, "r")
    li = list(opene)
    max_1 = len(li)
    min_1 = max_1 - 10
    for i in range(max_1-1, min_1-1, -1):
        print(li[i])
def main():
    nome = input("Inserisci il nome del file ")
    leggo(nome)

if __name__ == '__main__':
    main()