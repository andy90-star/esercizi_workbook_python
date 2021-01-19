#!/bin/python3
import random
from tabulate import tabulate
def runs():
    dice = 0
    list_dice = list() 
    for index in range(0, 1000):
        dice = random.randint(1,12)
        list_dice.append(dice)
    return list_dice
    
def percentual(dice_1):
    dicto_2 = dict()
    moment = 0
    for index_1 in range(1,13):
        moment = 0
        for index in dice_1:
            if index == index_1:
                moment += 1
        dicto_2[index_1] = moment
    return dicto_2
            
def stampo(final):
    for i in range(1,13):
        print(tabulate([[i, final.get(i)]], headers=['Number', 'esc'], tablefmt='orgtbl'))

def main():
    dice_1 = runs()
    final = percentual(dice_1)
    stampo(final)
if __name__ == "__main__":
    main()