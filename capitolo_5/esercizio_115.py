#!/bin/python3
def list_div(number):
    list_complete = list()
    for i in range(number, 0, -1):
        if number%i == 0:
            list_complete.append(i)
    print(list_complete)
    return list_complete
def main():
    number = int(input("Enter the number"))
    list_div(number)

if __name__ == '__main__':
    main()