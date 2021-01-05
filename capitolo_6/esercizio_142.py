#!/bin/python3
def cont(string, dicto_string):
    for str_1 in string:
        dicto_string[str_1] = True
    print("the string contains", len(dicto_string))

def main():
    try:
        string = input("Enter a string: ")
        dicto_string = dict()
        cont(string, dicto_string)
    except:
        print("Error!")
        main()

if __name__ == '__main__':
    main()