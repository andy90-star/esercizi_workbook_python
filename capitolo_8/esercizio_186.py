#!/bin/python3
def runLength(list_values, cont, list_final, length, cont_1,list_finally, list_moment, name, alfabet):
    letter = alfabet[cont_1]
    if not letter  in list_finally and cont_1 > 0:
        count = list_values.count(letter)
        cont_1 -= 1
        cont -= 1
        list_finally.append(letter)
        list_finally.append(count)
        runLength(list_values, cont, list_final, length, cont_1,list_finally, list_moment, name,alfabet)
    elif letter in list_final  and cont_1 > 0:
        cont_1 -= 1
        cont -= 1 
        runLength(list_values, cont, list_final, length, cont_1,list_finally, list_moment, name,alfabet)
    elif cont_1 == 0:
        print(list_finally)





        
        

def main():
    alfabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y",]
    name=''
    list_finally = list()
    list_final = list()
    cont_1 = 24
    word = input("Enter the sentence: ")
    list_values = list(word)
    list_moment = list()
    cont = len(list_values)
    length = len(list_values)
    runLength(list_values, cont, list_final, length,cont_1,list_finally, list_moment,name,alfabet)

if __name__ == '__main__':
    main()