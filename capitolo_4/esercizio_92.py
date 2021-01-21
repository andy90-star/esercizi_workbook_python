#!/bin/python3
def ordinalDate(day,year):
    dict_month ={
        1 : 31,
        2 : 28,
        3 : 31,
        4 : 30,
        5 : 31,
        6 : 30,
        7 : 31,
        8 : 31,
        9 : 30,
        10 : 31,
        11 : 30,
        12 : 31,
    }
    for number in range(1,12):
        sottra = dict_month.get(number)
        if day > sottra:
            day -= sottra
        else:
            break
    if year%4==0:
            if year%100==0:
                if year%400==0:
                    day += 1
                    return day
                else:
                    return day
            else:
                return day
    else:
        return day
def main():
    try:
        day=int(input("enter the day in number: "))
        year=int(input("enter the year: "))
        day_ordinal = ordinalDate(day,year)
        print(day_ordinal)
    except ValueError:
            print("It isn't int")

if __name__ == "__main__":
    main()