#!/bin/python3
def isPossible(sold, coins,number):
    molt = coins * number
    if molt == sold:
        return True
    else:
        return False

def main():
    try:
        sold = float(input("Enter the total: "))
        coins = float(input("Enter type of the coin: "))
        number = int(input("Enter the number of the coins"))
        first = isPossible(sold, coins, number)
        print(first)
    except ValueError:
        print("a or more values aren't int!")

if __name__ == '__main__':
    main()