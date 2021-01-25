#!/bin/python3
from esercizio_129 import token
f"""A +
or - operator is unary if it is the first token in the list, or if the token that imme-
diately precedes it is an operator or open parenthesis. Otherwise the operator is
binary."""
def unary_or_binary(first):
    list_operator = ["-","+","*","/","("]
    if first[0] == "-" :
        first.pop(0)
        first.insert(0, "-u")
    elif  first[0] == "+":
        first.pop(0)
        first.insert(0, "+u")
    for index in range(1, len(first)-1):
            for operator in list_operator:
                if first[index-1] == operator and first[index] == "-":
                    first.pop(index)
                    first.insert(index, "-u")
                if first[index-1] == operator and first[index] == "+":
                    first.pop(index)
                    first.insert(index, "+u")
    final= "".join(first)
    return final




def main():
    expression = input("Enter the expression mathematical: ")
    first = token(expression)
    first_1 = unary_or_binary(first)
    print(first_1)
if __name__ == "__main__":
    main()