#!/bin/python3
def ordianl_date(day,month,year,moment):
    cont = 0
    final = 0
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
    if month in dict_month:
        for number in dict_month.keys():
            if number != month:
                cont += 1
            elif number == month:
                break
        for number in range(1,month+1):
            moment = dict_month.get(number)
            final += moment
        if year%4==0:
            if year%100==0:
                if year%400==0:
                    final += int(day) + 1
                    print("It is the",final)
                else:
                    final += int(day)
                    print("It is the",final)
            else:
                final += int(day)
                print("It is the",final)
        else:
            final += int(day)
            print("It is the",final)


                
def main():
    try:
        moment = 0
        day=input("Enter the number day: ")
        month=int(input("Enter the month in number: "))
        year=int(input("Enter the year: "))
        ordianl_date(day,month,year,moment)
    except ValueError:
        print("It isn't int")
    


if __name__ == "__main__":
    main()