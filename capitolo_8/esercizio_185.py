#!/bin/python3
def runLength(list_values, cont, list_final, length, cont_1):
    letter = list_values[cont]
    if list_values[cont-1] == letter and length > 0:
        cont -=1
        cont_1 += 1
        length -= 1
        runLength(list_values, cont, list_final, length,cont_1)
    elif list_values[cont-1] != letter and length > 0 :
        cont_1 += 1
        letter = list_values[cont]
        list_final.append(letter)
        list_final.append(cont_1)
        cont_1 = 0
        cont -=1
        length -= 1
        runLength(list_values, cont, list_final, length,cont_1)
    elif length == 0:
        print(list_final)
def main():
    list_final = list()
    cont_1 = 0
    list_values = ["a","a","b","b","b","b","c","c"]
    cont = len(list_values)-1
    length = len(list_values)
    runLength(list_values, cont, list_final, length,cont_1)

if __name__ == '__main__':
    main()