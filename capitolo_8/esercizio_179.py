#!/bin/python3
import time
def newton(number, list_number, number_moment):
    number_moment = ((number/number_moment) + number_moment)/2
    number_str = str(number_moment)
    list_number_2 = list(number_str)
    if len(list_number_2) == 4:
        print(number_moment)
    elif type(number_moment) == float:
        time.sleep(1)
        print(number_moment)
        newton(number, list_number, number_moment)
def main():
    number=int(input("Enter the number: "))
    list_number = list(str(number))
    number_moment = list_number[0] + list_number[1]
    number_moment = int(number_moment)
    newton(number,list_number, number_moment)
if __name__ == "__main__":
    main()