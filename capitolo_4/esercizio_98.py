#!/bin/python3
def isPrime(number):
    if number > 1 and number%1==0 and number%2==1 and number%number==0:
        print("It's prime")
        return number
    elif number==2:
        print("It's prime")
        return number
    else:
        print("It isn't prime")
        return number
def main():
    try:
        number = int(input("Enter the number"))
        first = isPrime(number)
        print(first)
    except ValueError:
        print("It isn't int")
if __name__ == "__main__":
    main()