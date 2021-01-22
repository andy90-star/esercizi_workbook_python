#!/bin/python3
import random
from tabulate import tabulate 
def bingo():
    index = 0
    men = 1
    add = 0
    lista_bingo = ["b","i","n","g","o"]
    for index_letter in lista_bingo:
        add += 15
        index_letter = list()
        for _ in range(0, 5):
            moment = random.randint(men,add)
            index_letter.append(moment)
        print(tabulate([[str(lista_bingo[index]).upper()], [str(index_letter)]], headers=["Letter:"],  tablefmt='orgtbl'))
        print("------------------------------------------")
        men += 15
        index += 1
    return index_letter
def main():
    bingo()

if __name__ == '__main__':
    main()