#!/bin/python3
def display_number(number, lista):
    lista.append(number)
    return lista
def main():
    lista = list()
    boolean = True
    while boolean:
        number = input("Enter the number: ")
        if number != '' or number != "":
            a = display_number(int(number), lista)
        else:
            boolean = False
            print(a)

        

if __name__ == "__main__":
    main()
    