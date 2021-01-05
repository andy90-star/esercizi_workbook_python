#!/bin/python3
def ordinal(number):
    list_number = {1:"first", 2:"second", 3:"third", 4:"fourth", 5:"fifth", 6:"sixth", 7:"seventh",\
         8:"eighth", 9:"ninth", 10:"tenth", 11:"eleventh", 12:"twelfth"}
    if number in list_number:
        print(list_number.get(number))
    else:
        print("")


def main():
    try:
        number = int(input("enter the number ( 1 to 12 ): "))
        ordinal(number)
    except:
        print("Sorry, i don't understand")
        main()

if __name__ == '__main__':
    main()