#!/bin/python3
from esercizio_115 import list_div

def control(lista, number):
    contator = 0
    for i in range(1, len(lista)):
        contator += lista[i]
    if contator == number:
        print("The number ", number, "is perfect") 
    elif contator != number:
        print("The number ", number, "isn't perfect") 

def main():
    try:
        number=int(input("Enter the number"))
        lista = list_div(number)
        control(lista, number)
    except ValueError:
        print("Enter the value of type int")
        main()


if __name__ == '__main__':
    main()