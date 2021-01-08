#!/bin/python3
def main(add):
    number = int(input("Enter the number: "))
    add += number
    print(add)
    if number != 0:
        main(add)
    elif number == 0:
        print("Finish " + str(add))

if __name__ == '__main__':
    add = 0
    main(add)