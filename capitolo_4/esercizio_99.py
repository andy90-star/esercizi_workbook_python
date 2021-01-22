#!/bin/python3
def nextPrime(number):
    if number > 1 and number%1==0 and number%2==1 and number%number==0:
        print("It's prime", number)
    elif number==2:
        print("It's prime", number)
    else:
        number += 1
        nextPrime(number)
def main():
    number = int(input("Enter the number"))
    nextPrime(number)
    

if __name__ == "__main__":
    main()