#!/bin/python3
def poetry(select):
    list_poetry = {
    1:"Twelve drummers drumming",
    2:"Eleven pipers piping",
    3:"Ten lords a-leaping",
    4:"Nine ladies dancing",
    5:"Eight maids a-milking",
    6:"Seven swans a-swimming",
    7:"Six geese a-laying",
    8:"Five golden (gold) rings",
    9:"Four calling (colly) birds",
    10:"Three french hens",
    11:"Two turtle doves",
    12:"And a partridge in a pear tree"}
    if select in list_poetry:
        print(list_poetry.get(select))
        

def main():
    try:
        list_add = list()
        print(F"""1.Twelve drummers drumming
        2.Eleven pipers piping
        3.Ten lords a-leaping
        4.Nine ladies dancing
        5.Eight maids a-milking
        6.Seven swans a-swimming
        7.Six geese a-laying
        8.Five golden (gold) rings
        9.Four calling (colly) birds
        10.Three french hens
        11.Two turtle doves
        12.And a partridge in a pear tree""")
        for i in range(1, 12):
            select=int(input("Enter the number of line for select the sentence. "))
            if select in list_add:
                print("line already called")
            else:
                list_add.append(select)
                poetry(select)
    except:
        print("Sorry!I don't understand")
        main()
if __name__ == '__main__':
    main()