#!/bin/python3
from esercizio_130 import unary_or_binary
from esercizio_129 import token
def postfix(first):
    list_operat = list()
    list_postfix = list()
    for each in range(0,len(first)-1):
        if first[each] == "+" or first[each] == "-" or first[each] == "+u" or first[each] == "-u" or first[each] == "u":
            list_postfix.append(first[each])
            if  list_operat != [] and list_operat[-1] != "(" \
                and first[each-1] < first[-1]:
                inde = list_operat[-1]
                list_postfix.append(inde)
            list_operat.append(first[each])
        elif int(first[each]):
            list_postfix.append(first[each])
        elif first[each] == "(":
            list_operat.append(first[each])
        elif first[each] == ")":
            if list_operat[-1] != "(":
                inde = list_operat[-1] 
                list_operat.remove(inde)
                list_postfix.append(inde)
        elif list_operat != [] :
            inde = list_operat[-1] 
            list_operat.remove(inde)
            list_postfix.append(inde)
    return list_postfix

def main():
    expression = input("Enter the expression mathematical: ")
    first_1 = token(expression)
    first = unary_or_binary(first_1)
    postfix(first)
    print(first)
if __name__ == "__main__":
    main()