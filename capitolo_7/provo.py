#!/bin/python3
def main():
    #
    #
    try:
        boolean = True
        list_number = list()
        while boolean:
            inp_number = int(input("Enter the number: "))
            if inp_number != 0:
                list_number.append(inp_number)
            elif inp_number == 0:
                boolean = False
                break
        list_number.sort()
        for i in list_number:
            print(i)
    except:
        print("Sorry, repeat! ")
        main()


if __name__ =='__main__':
    main()