#!/bin/python3
list_number = list()
def negative_zero_positive(list_number, number):
    list_number.append(number)
    list_number.sort()
    print(list_number)

def main():
    number = int(input("Enter the number "))
    negative_zero_positive(list_number, number)
    terminate = input("do you want to finish? ").lower()
    if terminate == "si":
        print("Ok")
    elif terminate == "no":
        main()

if __name__ == '__main__':
    main()