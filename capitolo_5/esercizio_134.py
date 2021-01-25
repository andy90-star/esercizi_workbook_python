#!/bin/python3 
def value(larger):
    final = str(larger[2]) +","+ str(larger[3])
    print(final)
    final = str(larger[1]) +"," +str(larger[2])
    print(final)
    final = str(larger[0]) +"," +str(larger[1])
    print(final)
def main():
    try:
        larger = list()
        for _ in range(0,4):
            number = int(input("Enter a number: "))
            larger.append(number)
        value(larger)
    except ValueError:
        print("Value not is int")
if __name__ == '__main__':
    main()