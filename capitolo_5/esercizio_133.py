#!/bin/python3
def isSublist(larger, smaller):
    for large in range(0, 4):
        for small in range(0,2):
            if larger[large] == smaller[small] and larger[large+1] == smaller[small+1]:
                return True
            else:
                return False

def main():
    try:
        larger = list()
        smaller = list()
        for _ in range(0,4):
            number = int(input("Enter a number: "))
            larger.append(number)
        for _ in range(0,2):
            number = int(input("Enter a sublist: "))
            smaller.append(number)
        first = isSublist(larger, smaller)
        print(first)
    except ValueError:
        print("Value is not int")


if __name__ == "__main__":
    main()