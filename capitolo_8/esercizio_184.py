#!/bin/python3
def Flattening(list_neasted, list_moment,cont, length, cont_1, list_final):
    if length > 0:
        letter = list_neasted[cont]
        letter = str(letter)
        list_moment.append(letter)
        length -= 1
        cont += 1
        Flattening(list_neasted, list_moment,cont, length,cont_1, list_final)
    else:
        for letter in list_moment:
            for number in letter:
                if number != "[" and number != "]" and number != "," and number != " ":
                    list_final.append(number)
        return print(list_final)
def main():
    list_final  = list()
    cont_1 = 0
    cont = 0
    list_moment = list()
    list_neasted = [1, [2, 3], [4, [5, [6, 7]]],[[[8], 9], [10]]]
    length = len(list_neasted)
    Flattening(list_neasted, list_moment,cont,length, cont_1, list_final)
if __name__ == '__main__':
    main()

