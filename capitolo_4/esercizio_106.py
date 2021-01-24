#!/bin/python3
def days(month, year):
    dict_days = {
        1:"31",2:"28",3:"31",4:"30",
        5:"31",6:"30",7:"31",8:"31",
        9:"30",10:"31",11:"30",12:"31"
    }
    if month in dict_days and year%4!=0:
        return dict_days.get(month)
    elif month in dict_days and year%4==0 or year%400==0:
        if month == 2:
            moment = dict_days.get(month)
            month_1 = int(moment) +1
            return month_1
        else:
            return dict_days.get(month)

            

def main():
    try:
        month=int(input("Enter the month in number: "))
        year=int(input("Enter the month in number: "))
        first = days(month,year)
        print(first)
    except ValueError:
        print("value not is int")
if __name__ == "__main__":
    main()