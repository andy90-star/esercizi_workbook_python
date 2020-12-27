#!/bin/python3
import os
def leggo(a):
    trova = os.path.abspath(a)
    opene = open(trova, "r")
    li = list(opene)
    for i in range(0, 10, 1):
       print(li[i])

def main():
    nome = input("Inserisci il nome del file ")
    leggo(nome)

if __name__ == '__main__':
    main()