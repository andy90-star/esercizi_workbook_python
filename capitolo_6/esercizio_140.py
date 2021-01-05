#!/bin/python3
def codes(code):
    dicto_zip_code = {
        "A" : "Newfoundland",
        "B" : "Nova Scotia",
        "C" : "Prince Edward Island",
        "E" : "New Bruswick",
        "G" : "Quebec",
        "H" : "Quebec",
        "J" : "Quebec",
        "K" : "Ontario",
        "L" : "Ontario",
        "M" : "Ontario",
        "N" : "Ontario",
        "P" : "Ontario",
        "R" : "Manitoba",
        "S" : "Saskatchewan",
        "T" : "Alberta",
        "V" : "British Columbia",
        "X" : "Nunavut",
        "X" : "Northwest Territories",
        "Y" : "Yukon",
    }
    list_code = list(code)
    if list_code[0] in dicto_zip_code:
        print(dicto_zip_code.get(list_code[0]))
        if list_code[3] == "0":
            print("rural")
        elif list_code[3] == "1":
            print("urban")


def main():
    try:
        code = input("Enter the zip code ").upper()
        codes(code)
    except:
        print("sorry, repeat")
        main()

if __name__ == '__main__':
    main()