#!/bin/python3
def control(list_pass):
    convert = list_pass.copy()
    convert.sort()
    if convert == list_pass:
        print("the list is in order")
    else:
        print("the list isn't in order")
def main():
    list_pass = list()
    boolean = True
    while boolean:
        number = input("Enter the number: ")
        if number != "":
            number_1 = number
            list_pass.append(number_1)
        elif number == "":
            boolean = False
    control(list_pass)



if __name__ == "__main__":
    main()