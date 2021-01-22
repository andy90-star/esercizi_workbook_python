#!/bin/python3
import random
def call(call_list):
    for _ in range(0,5):
        call_number = random.randint(1,60)
        call_list.append(call_number)
    return call_list

def vicotry(call_1):
    men = 1
    list_vertical = list()
    list_diagonal = list()
    diagonal = 0
    contator = 0
    letter = 0
    vicotry = 0
    add = 0
    lista_bingo = ["b","i","n","g","o"]
    for index_letter in lista_bingo:
        contator = 0
        vicotry = 0
        add += 15
        index_letter = list()
        for _ in range(0, 5):
            moment = random.randint(men,add)
            index_letter.append(moment)
        list_vertical.append(index_letter[0])
        list_diagonal.append(index_letter[diagonal])
        diagonal += 1
        print("List orrizontal ",lista_bingo[letter], index_letter)
        letter += 1
        for number in index_letter:
            if number == call_1[contator]:
                vicotry +=1
                contator +=1
                if vicotry == 6:
                    print("Victory")
        for number in list_vertical:
            if number == call_1[contator]:
                vicotry +=1
                contator +=1
                if vicotry == 6:
                    print("Victory") 
        for number in list_diagonal:
            if number == call_1[contator]:
                vicotry +=1
                contator +=1
                if vicotry == 6:
                    print("Victory")
    print("List vertical ", list_vertical)            
    print("List diagonal ", list_diagonal)
    print("List win ", call_1)      
def main():
    print("If you win the program will print Victory")
    call_list = list()
    call_1 = call(call_list)
    vicotry(call_1)
if __name__ == "__main__":
    main()