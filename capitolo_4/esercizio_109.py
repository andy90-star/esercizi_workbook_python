#!/bin/python3
import time
def display():
    dict_days = {
        1:"31",2:"28",3:"31",4:"30",
        5:"31",6:"30",7:"31",8:"31",
        9:"30",10:"31",11:"30",12:"31"
    }
    year = 1900
    for index in range(year, 2000):
        final = str(index)
        final = final[2:4]
        for month in range(1,12):
            days = dict_days.get(month)
            for day in range(1,int(days)):
                #print(day, month)
                molti = day*month
                #print(molti)
                #print(days, month, molti)
                if molti == int(final):
                    print("days: ", days, "Month: ", month, "  ", molti, final)
def main():
    display()

if __name__ == '__main__':
    main()