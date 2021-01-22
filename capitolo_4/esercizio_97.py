#!/bin/python3
def precedence(number):
    if number.startswith("+"):
        return 1
    elif number.startswith("-"):
        return 2
    elif number.startswith("*"):
        return 3
    elif number.startswith("/"):
        return 4
def main():
    number = input("Enter the number: ")
    first = precedence(number)
    print(first)
if __name__ == "__main__":
    main()