#!/bin/python3
def edit(str_1, str_2, cost, cont, d1,d2,d3,cont_1, cont_2):
    if len(str_1) == 0:
        return len(str_2)
    elif len(str_2) == 0:
        return len(str_1)
    else:
        if str_1[-1] != str_2[-1]:
            cost += 1
        elif str_1[cont] != str_2[cont] and d1 < len(str_1)-1:
            cont += 1
            d1 += 1
            edit(str_1, str_2, cost, cont, d1,d2, d3,cont_1,cont_2)
        elif str_1[cont_1] != str_2[cont_1] and cont_1 < len(str_2)-1:
            cont_1 += 1
            d2 += 2
            edit(str_1, str_2, cost, cont, d1,d2,d3, cont_1,cont_2)
        elif str_1[cont_2] != str_2[cont_2] and cont_2 < len(str_2)-1:
            cont_2 += 1
            d3 += 2
            edit(str_1, str_2, cost, cont, d1,d2,d3, cont_1,cont_2)
        else:
            print(d2, d2+1, d3+cost)
            
def main():
    try:
        str_1 = input("Enter the string the word must be of the same length:")
        str_2 = input("Enter the string: ")
        cost = 0
        cont = 0
        cont_1 = 0
        cont_2 = 0
        d1 = 0
        d2 = 0
        d3  =0
        edit(str_1, str_2, cost, cont, d1,d2,d3, cont_1,cont_2)
    except IndexError:
        print("Index esc of the tail")
        
    

if __name__ == '__main__':
    main()