#!/bin/python3
def recipe(units):
    tablespoons = 0
    cup = 0
    for _ in range(0, units):
        if units > 3:
            units -= 3
            tablespoons +=1
        else:
            break
    for _ in range(0, tablespoons):
        if tablespoons >= 16:
                cup += 1
                tablespoons -= 16
        else:
            break
    print(cup, tablespoons, units)
def main():
    try:
        units = int(input("Enter the number of the teaspoon: "))
        people=int(input("Enter the number of the people: "))
        units = units*people
        recipe(units)
    except ValueError:
        print("Value not is int")
if __name__ == "__main__":
    main()